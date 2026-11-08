# Milestone 4 batch runner - runs the notebook's own code outside Colab.
#
# A1 and B1 are loaded by executing the notebook cells themselves, so the prompts
# under test are byte-for-byte the ones in thesis_meeting_prep_prototype.ipynb.
# B2 comes from workflow_b2.py (same text as the notebook's section 7).
#
# Usage, from the Project folder, with OPENROUTER_API_KEY set in the environment:
#   python Prototype/run_m4.py scenarios     B2 on S1-S3 (the product)
#   python Prototype/run_m4.py fill          A1 + B1 on the cases not yet run
#   python Prototype/run_m4.py b2tests       B2 on T1-T10, three runs each
#   python Prototype/run_m4.py rag           RAG-v1 on the five questions

import json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
assert os.environ.get("OPENROUTER_API_KEY"), "OPENROUTER_API_KEY not set"

nb = json.load(open(os.path.join(HERE, "thesis_meeting_prep_prototype.ipynb"), encoding="utf-8"))
G = {}
exec("import os, json, time, datetime, uuid\n"
     "from typing import Literal, Optional, List\n"
     "from pydantic import BaseModel, Field, ValidationError\n"
     "from litellm import completion, completion_cost\n"
     "from IPython.display import display, Markdown\n"
     'MODEL        = "openrouter/google/gemini-3.1-flash-lite"\n'
     'BIG_MODEL    = "openrouter/google/gemini-3.7-flash"\n'
     'CLAUDE_MODEL = "openrouter/anthropic/claude-haiku-4.5"\n'
     'EMBED_MODEL  = "openrouter/google/gemini-embedding-001"\n', G)

def cell_src(i):
    return "".join(nb["cells"][i]["source"])

# The notebook cells that define functions, prompts and data (no calls, no setup).
for i, c in enumerate(nb["cells"]):
    src = "".join(c["source"])
    if c["cell_type"] != "code":
        continue
    if any(k in src for k in ("def call_llm", "PROMPT_A1 =", "class Concern(BaseModel)",
                              "SYSTEM_PARSE =", "SYSTEM_AGENDA =", "SYSTEM_EMAIL =",
                              "def run_workflow(", "SCENARIOS = {", "TESTS = {",
                              "HSLU_DOCS = [", "SYSTEM_GROUNDED =")):
        exec(src, G)
    elif "def embed(" in src and sys.argv[1] == "rag":
        exec(src, G)          # also builds the index, exactly as the notebook does

exec(open(os.path.join(HERE, "workflow_b2.py"), encoding="utf-8").read(), G)

def done(version):
    c = collections.Counter()
    if os.path.exists("run_log.jsonl"):
        for l in open("run_log.jsonl", encoding="utf-8"):
            r = json.loads(l)
            if r["prompt_version"] == version and not r.get("error"):
                c[(r["case_id"], r["run_no"])] += 1
    return c

def go(label, fn):
    try:
        fn(); print(f"{label} ok", flush=True)
    except Exception as e:
        print(f"{label} FAILED: {e}", flush=True)

phase = sys.argv[1]

if phase == "scenarios":
    for sid, note in G["SCENARIOS"].items():
        go(f"B2 {sid}", lambda: G["run_workflow_b2"](note, sid, 1))

elif phase == "fill":
    a1, b1 = done("A1"), done("B1")
    for cid, note in G["TESTS"].items():
        for n in (1, 2, 3):
            if not a1[(cid, n)]:
                go(f"A1 {cid} r{n}", lambda: G["run_baseline"](note, cid, n))
            if not b1[(cid, n)]:
                go(f"B1 {cid} r{n}", lambda: G["run_workflow"](note, cid, n, verbose=False))

elif phase == "b2tests":
    b2 = done("B2")
    for cid, note in G["TESTS"].items():
        for n in (1, 2, 3):
            if not b2[(cid, n)]:
                go(f"B2 {cid} r{n}", lambda: G["run_workflow_b2"](note, cid, n))

elif phase == "rag":
    # Same loop as notebook section 6.
    QUESTIONS = [
      "How many credits do I need before I can register for the bachelor thesis?",
      "What happens if I fail the thesis - can I repeat it?",
      "I might not be able to finish the thesis. What am I supposed to do?",
      "When exactly is the submission deadline this semester and do I hand in paper copies or just a pdf?",
      "Is my research question specific enough to pass?",
    ]
    for q in QUESTIONS:
        ans, hits = G["answer_grounded"](q)
        G["log_run"]("RAG", 1, "RAG-v1", q, {"answer": ans, "retrieved": [d["id"] for d, _ in hits]})
        print("=" * 70); print("Q:", q); print("[retrieved:", [d["id"] for d, _ in hits], "]"); print(ans, flush=True)
