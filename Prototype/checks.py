# Automatic flags for the B-series runs - Milestone 4.
#
# These do NOT score a run. They point a human reader at places to look.
# A flag is a candidate hard fail; the verdict is still made by reading.
#
#   python Prototype/checks.py            (from the Project folder)

import json, re, sys, collections

WELLBEING = re.compile(r"\b(wellbeing|well-being|coping|mental|personal (challenge|situation|difficult)|"
                       r"my (current )?situation|support services|struggl)", re.I)
DEADLINE  = re.compile(r"deadline|submission date|extension", re.I)   # "regulations are the authority" is the intended wording for institutional items, so it is not flagged
OFFICIAL  = re.compile(r"HSLU|official|regulation|submission (date|deadline)", re.I)
MINUTES   = re.compile(r"\b[1-9]\d*\s*min", re.I)


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def flags_for(row):
    note, out = row["input"], row["output"]
    if not out or not isinstance(out, dict):
        return ["no structured output"]
    f = []
    p = out["parsed"]
    n = norm(note)
    text = "\n".join(out.get(k, "") or "" for k in ("agenda", "questions", "email"))

    # Hard fail 3 at step 1: a quote that is not in the note was invented (or paraphrased).
    for c in p["concerns"]:
        if norm(c["quote"]) not in n:
            f.append(f"quote not in note: {c['quote'][:60]!r}")

    # D1: a duration in the agenda when the note gives none.
    if p["meeting_minutes"] is None and MINUTES.search(out.get("agenda") or ""):
        f.append("meeting length invented")

    # D4/D6: wellbeing language when the note raises no support concern.
    has_support = any(c["kind"] == "support" for c in p["concerns"])
    if not has_support and WELLBEING.search(text + " ".join(p["missing_info"])):
        f.append("wellbeing raised but note has no support concern")

    # D6: personal situation written into the email.
    if has_support and WELLBEING.search(out.get("email") or ""):
        f.append("wellbeing written into the email")

    # D5: an HSLU/official deadline or regulation brought into the email when the note raises none.
    # A generic "[next steps and deadlines]" blank means task deadlines and is not flagged.
    has_inst = any(c["kind"] == "institutional" for c in p["concerns"])
    if not has_inst and not DEADLINE.search(note) and OFFICIAL.search(out.get("email") or ""):
        f.append("HSLU deadline/regulation added to email, not in note")

    # D2: zero concerns but an agenda/email was produced anyway.
    if not p["concerns"] and (out.get("email") or "").strip():
        f.append("email produced from an empty note")

    return f


def main(path="run_log.jsonl", versions=("B1", "B2")):
    rows = [json.loads(l) for l in open(path, encoding="utf-8")]
    seen, table = set(), collections.defaultdict(dict)
    for r in rows:
        v = r["prompt_version"]
        if v not in versions or r["case_id"] == "RAG":
            continue
        key = (v, r["case_id"], r["run_no"])
        if key in seen:          # the log has a duplicate T1/1 from the first session; keep the first
            continue
        seen.add(key)
        table[(r["case_id"], r["run_no"])][v] = flags_for(r)

    order = lambda k: (k[0][0], int(re.sub(r"\D", "", k[0]) or 0), k[1])
    totals = collections.Counter()
    for (case, run) in sorted(table, key=order):
        for v in versions:
            if v in table[(case, run)]:
                fl = table[(case, run)][v]
                totals[(v, "runs")] += 1
                totals[(v, "flagged")] += bool(fl)
                print(f"{case:4} r{run} {v}: {'; '.join(fl) if fl else '-'}")
    print()
    for v in versions:
        print(f"{v}: {totals[(v,'flagged')]} of {totals[(v,'runs')]} runs flagged")


if __name__ == "__main__":
    main(*sys.argv[1:2])
