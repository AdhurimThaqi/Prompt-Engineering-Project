# Refined workflow B2 - Milestone 4.
#
# Same four-step chain as B1. Every change below is tied to a defect observed
# in the B1 runs of 26.10.2026 (see Milestone_4 revision plan, D1-D6).
# Expects call_llm, completion, MODEL, BIG_MODEL, log_run from the notebook setup.

import json, time
from typing import Literal, Optional, List
from pydantic import BaseModel, Field, ValidationError
from litellm import completion


class ConcernB2(BaseModel):
    quote: str = Field(description="The concern in the student's own words, copied from the note. Do not paraphrase.")
    kind: Literal["discuss", "institutional", "judgement", "support"]
    size: Literal["quick", "substantial"] = Field(description="quick = a factual question answerable in a minute or two; substantial = needs discussion")   # D3
    priority: int = Field(ge=1, le=10, description="1 = most important to resolve in this meeting")
    why_priority: str = Field(description="One short clause: why this rank")


class ParsedNoteB2(BaseModel):
    meeting_minutes: Optional[int] = Field(description="Meeting length in minutes ONLY if the note states one, else null. Never estimate.")
    stage: Literal["early", "mid", "late", "unknown"]
    concerns: List[ConcernB2] = Field(description="Every concern present in the note. Do not add concerns the note does not raise.")
    missing_info: List[str] = Field(description="Gaps in what the note itself says, phrased as questions for the STUDENT. Never about wellbeing unless the note raises it.")


SYSTEM_PARSE_B2 = """You read a bachelor student's rough notes before a meeting with their thesis supervisor, and turn them into structured data.

Rules you must follow exactly:

1. Every concern you list must be present in the note. Copy the student's own words into `quote`. Never add a concern the student did not raise, however sensible it would be.
2. Never drop a concern the student did raise, even a small one.
3. Never alter a fact stated in the note (dates, counts, chapter numbers, names).
4. Classify each concern:
   - "institutional" if answering it would require knowing HSLU procedure, deadlines, regulations, formatting rules or grading.
   - "judgement" if it asks whether the student's work is good enough, acceptable, or will pass - a verdict that belongs to the supervisor.
   - "support" if the student describes a personal or wellbeing difficulty they are experiencing rather than an academic task.
   - "discuss" otherwise.
5. Mark each concern's size: "quick" if it is a factual question the supervisor can answer in a minute or two (for example a number, a yes/no on format), "substantial" if it needs real discussion.
6. If the note contradicts itself, list both sides as separate concerns and add the contradiction to `missing_info`.
7. A bare request for help ("help", "meeting tomorrow") is not a concern. If the note names no topic at all, return an empty `concerns` list.
8. `meeting_minutes`: only if the note states a length. If it does not, return null. Never estimate.
9. `missing_info` lists gaps in what the note itself says, as short questions for the student to answer before the meeting (for example: the meeting length is not stated; a chapter is mentioned without its status). Do NOT ask about the student's wellbeing, stress or personal situation unless the note itself raises it. Do NOT raise deadlines, regulations or topics the note never mentions.

Output only the structured object."""


SYSTEM_AGENDA_B2 = """You turn a parsed set of student concerns into a meeting agenda for a thesis supervision meeting.

Hard rules:

- Work only from the `concerns` given. Every agenda item must come from a concern. Add nothing else.
- `missing_info` contains questions for the STUDENT to answer before the meeting. Never turn them into agenda items. List them under BEFORE THE MEETING.
- Meeting length:
  - If `meeting_minutes` is a number, fit the agenda to it: 2 minutes opening, 3 minutes to agree next steps, about 5 minutes per "substantial" item, 1-2 minutes per "quick" item. Quick items may be grouped into one agenda item. If there is not enough time for everything, say explicitly which items will not fit.
  - If `meeting_minutes` is null, the length is unknown. Do NOT state or assume a total length and do NOT give minutes per item. Order the items by priority and write "(length not stated)" in the heading.
- For a concern marked "institutional": do NOT answer it. Put it on the agenda as a question for the supervisor, and note that the official regulations are the authority.
- For a concern marked "judgement": do NOT give a verdict. Rewrite it as a question the student puts to the supervisor.
- For a concern marked "support": it is NOT an agenda item and gets no time slot. Write one neutral line under SUPPORT saying the student can choose whether and how much to mention it, and that HSLU student support services can help. Give no advice on what to say. If no concern is marked "support", omit the SUPPORT section entirely.

Format:

AGENDA (<n> min)      or      AGENDA (length not stated)
1. <item> - <minutes, only if length is known>
...

WILL NOT FIT
- <item> (if any, else write "nothing")

SUPPORT
- <one line, only if a support concern exists>

BEFORE THE MEETING
- <question from missing_info>"""


SYSTEM_QUESTIONS_B2 = """You turn a parsed set of student concerns into questions the student asks their supervisor.

Hard rules:

- Order by the priority given. Most important first - the student may only get through the first two.
- One question per concern. Specific enough to be answerable in a meeting.
- For "judgement" concerns, the question must ask for the supervisor's view, never state a position for them. Good: "Do you think the scope is narrow enough to be feasible in the time left?" Bad: "My scope is appropriate, right?"
- For "institutional" concerns, the question asks where to find the official answer, or asks the supervisor to confirm against it.
- For "support" concerns, write no question. The student decides whether to raise it.
- Never invent a question for a concern that is not in the input. Do not turn `missing_info` into questions.

Format: a numbered list, most important first. After each question, one short line in brackets saying why it ranks there."""


SYSTEM_EMAIL_B2 = """You draft the follow-up email a bachelor student sends their thesis supervisor after the meeting.

Hard rules:

- The email covers only the numbered items in the AGENDA, one line each. Nothing from BEFORE THE MEETING, nothing the agenda does not list.
- The meeting has not happened yet, so write it as a template with clearly marked blanks like [what we agreed on X]. Do not invent decisions, agreements or deadlines.
- Never state an HSLU deadline, regulation or procedure as fact. Mention a deadline or regulation ONLY if an agenda item is about one, and then leave a blank for the student to fill from the official source.
- Never mention the student's personal situation, health or wellbeing. An email is a written record; the student decides separately whether to put that in writing.
- Tone: polite, brief, student to supervisor. No flattery, no apology for taking their time.
- Maximum 150 words.

Format:

Subject: <subject>

<body>"""


# D2: when the note has no topic, do not run steps 2-4 at all. A fixed reply cannot invent anything.
THIN_NOTE_REPLY = """NOT ENOUGH TO PREPARE FROM YET

Your note does not name anything you want to discuss, so there is nothing to build an agenda, questions or email from without guessing - and guessing is what this toolkit is designed not to do.

Add a few lines on:
- what you want to discuss or decide in this meeting
- how long the meeting is
- where you are in the thesis (e.g. which chapters exist)

Then run it again."""


def step1_parse_b2(note, model=None):
    model = model or MODEL
    msgs = [{"role": "user", "content": f"Student's note:\n\n{note}"}]
    for attempt in range(2):
        r = completion(model=model,
                       messages=[{"role": "system", "content": SYSTEM_PARSE_B2}] + msgs,
                       response_format=ParsedNoteB2, num_retries=3, timeout=60,
                       fallbacks=[BIG_MODEL])
        raw = r.choices[0].message.content
        try:
            return ParsedNoteB2.model_validate_json(raw), r
        except ValidationError as err:
            msgs += [{"role": "assistant", "content": raw},
                     {"role": "user", "content": f"Invalid: {err}. Fix it."}]
    raise ValueError("step1_parse_b2: no valid output")   # fail closed


def _payload(parsed):
    # D1: say the null out loud instead of leaving it for the model to read as "unspecified, pick one".
    p = json.loads(parsed.model_dump_json())
    if p["meeting_minutes"] is None:
        header = "MEETING LENGTH: NOT STATED - do not assume one.\n\n"
    else:
        header = f"MEETING LENGTH: {p['meeting_minutes']} minutes.\n\n"
    return header + json.dumps(p, indent=2, ensure_ascii=False)


def run_workflow_b2(note, case_id, run_no, model=None, prompt_version="B2"):
    model = model or MODEL
    start = time.time()
    try:
        parsed, r1 = step1_parse_b2(note, model=model)

        if not parsed.concerns:
            output = {"parsed": json.loads(parsed.model_dump_json()),
                      "agenda": THIN_NOTE_REPLY, "questions": "", "email": ""}
            log_run(case_id, run_no, prompt_version, note, output, response=r1,
                    latency_s=round(time.time() - start, 1))
            return output

        payload = _payload(parsed)
        agenda, r2 = call_llm(SYSTEM_AGENDA_B2, payload, model=model)
        questions, r3 = call_llm(SYSTEM_QUESTIONS_B2, payload, model=model)
        email, r4 = call_llm(SYSTEM_EMAIL_B2, f"Agenda:\n{agenda}", model=model)   # D5: email sees the agenda only

        output = {"parsed": json.loads(parsed.model_dump_json()),
                  "agenda": agenda, "questions": questions, "email": email}
        log_run(case_id, run_no, prompt_version, note, output, response=r4,
                latency_s=round(time.time() - start, 1))
        return output
    except Exception as e:
        log_run(case_id, run_no, prompt_version, note, None, error=str(e))
        raise
