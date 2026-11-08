# Builds docs/outputs.json for the project page from run_log.jsonl.
#
# Model outputs are copied verbatim from the log. The only hand-written text is
# in docs/annotations.json (case descriptions, short reading notes, revision plan),
# so it is always clear which words came from a model and which from me.
#
#   python docs/build_outputs.py        (from the Project folder)

import json, os, sys, collections, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "Prototype"))
from checks import flags_for

rows = [json.loads(l) for l in open(os.path.join(ROOT, "run_log.jsonl"), encoding="utf-8") if l.strip()]
ann = json.load(open(os.path.join(ROOT, "docs", "annotations.json"), encoding="utf-8"))

# first logged run per (version, case, run_no); the log has one duplicate T1/1 from 26.10
runs = {}
for r in rows:
    if r.get("error") or r["output"] is None:
        continue
    runs.setdefault((r["prompt_version"], r["case_id"], r["run_no"]), r)

def chain(r):
    o = r["output"]
    return {"parsed": o["parsed"], "agenda": o["agenda"], "questions": o["questions"], "email": o["email"]}

def version_block(v, cid):
    rs = [runs[(v, cid, n)] for n in (1, 2, 3) if (v, cid, n) in runs]
    if not rs:
        return None
    if v == "A1":
        return {"runs": len(rs), "output": rs[0]["output"]}
    return {"runs": len(rs), **chain(rs[0]), "flags": [flags_for(r) for r in rs]}

cases = []
for cid, a in ann["cases"].items():
    note = next((r["input"] for r in rows if r["case_id"] == cid), None)
    cases.append({"id": cid, **a, "note": note,
                  "A1": version_block("A1", cid), "B1": version_block("B1", cid), "B2": version_block("B2", cid)})

scenarios = []
for sid, a in ann["scenarios"].items():
    r = runs.get(("B2", sid, 1))
    scenarios.append({"id": sid, **a, "note": r["input"] if r else None, **(chain(r) if r else {}),
                      "flags": flags_for(r) if r else []})

rag = []
for r in rows:
    if r["prompt_version"] == "RAG-v1" and isinstance(r["output"], dict):
        q = r["input"]
        rag.append({"q": q, **ann["rag"].get(q, {}), "answer": r["output"]["answer"],
                    "retrieved": r["output"]["retrieved"]})

# scoreboard: share of runs with at least one automatic flag, per version (B-series only)
board = collections.defaultdict(lambda: [0, 0])
for (v, cid, n), r in runs.items():
    if v in ("B1", "B2") and cid.startswith("T"):
        board[v][0] += 1
        board[v][1] += bool(flags_for(r))
count = collections.Counter(v for (v, cid, n) in runs if cid.startswith("T"))

out = {
    "meta": {"generatedOn": datetime.date.today().strftime("%d.%m.%Y"),
             "model": "openrouter/google/gemini-3.1-flash-lite",
             "runs": {v: count[v] for v in ("A1", "B1", "B2")},
             "flagged": {v: {"runs": board[v][0], "flagged": board[v][1]} for v in ("B1", "B2")}},
    "findings": ann["findings"],
    "scoreboard": ann["scoreboard"],
    "cases": cases,
    "scenarios": scenarios,
    "rag": rag,
    "revision": ann["revision"],
}
json.dump(out, open(os.path.join(ROOT, "docs", "outputs.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("cases", len(cases), "scenarios", len(scenarios), "rag", len(rag), "runs", dict(count), "flagged", dict(board))
