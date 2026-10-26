# Prompt Log

**Project:** Bachelor Thesis Meeting Prep Coach (Modality 1 - Text)
**Student:** Adhurim Thaqi
**Module:** PROMPT H26

> **Rule for this file:** the prompt text is recorded **verbatim**, exactly as
> run - never tidied, shortened or improved afterwards. The prompt is the
> artifact under test; a cleaned-up version is a different prompt and the
> comparison stops meaning anything. Everything around the prompt - reasoning,
> observations, decisions - is written up properly.
>
> Fill in each entry at the time it is run. Keep failed versions; they are the
> evidence the brief asks for.

---

## How to use this file

One entry per prompt version. Copy the template, fill it in, never delete an old
entry.

Version naming: `A1` is the zero-shot baseline. `B1`, `B2`... are refinements. A
letter change means a different approach; a number change means a tweak within
the same approach.

The prompts below live in `thesis_meeting_prep_prototype.ipynb`. If you edit one
there, bump `PROMPT_VERSION`, copy the new text here, and record what changed.
Raw run data goes to `run_log.jsonl`; the judgement about whether a run passed
goes here.

---

## Entry template (copy this)

### Version: `__`

- **Date:**
- **Model / settings:**
- **What I was trying to fix:** *(what the previous version got wrong)*
- **What I changed and why:**
- **What I expected to happen:**

**Prompt (verbatim):**

```
[paste exactly as run]
```

**Runs:**

| Case | Run | Hard fail? | Which one | Notes |
|---|---|---|---|---|
| | 1 | | | |

- **What actually happened:**
- **What got better:**
- **What got worse or broke:** *(there is usually something)*
- **Kept or rejected, and why:**

---

# Versions

---

### Version: `A1` - zero-shot baseline

- **Date written:** 25.10.2026
- **Date run:**
- **Model / settings:** `openrouter/google/gemini-3.1-flash-lite`, default temperature
- **What I changed and why:** Nothing. This is the out-of-the-box baseline the
  brief requires - deliberately plain, so the refinements have something honest
  to improve on.

**Prompt (verbatim):**

System:

```
You are a helpful assistant.
```

User:

```
Help me prepare for my thesis supervisor meeting. Here are my notes:

{note}
```

**What I expect to happen** *(written before running - a wrong prediction is
itself a finding)*:

1. Answers HSLU procedural questions as if it knew them (hard fail 1) - most
   likely on T1 and T9.
2. Gives its own verdict on the student's work (hard fail 2) - most likely on
   T2 and T8.
3. Invents concerns on a thin note (hard fail 3) - most likely on T3.

**Runs:** 14 logged, cases T1-T5. T6-T10 not yet run.

| Case | Run | Hard fail? | Which one | Notes |
|---|---|---|---|---|
| T1 | 1 | yes | 3 | No deadline stated. Added 5 concerns the note never raised: oral defence, signatures, style guide, review timeline, progress update |
| T1 | 2 | yes | 3 | Same pattern |
| T1 | 3 | yes | 3 | Same pattern |
| T2 | 1 | yes | 2 | "To answer your question directly: **No.**" |
| T2 | 2 | yes | 2 | "No, it is not specific enough to pass." Labelled its answer "Verdict" |
| T2 | 3 | yes | 2 | "**No.** While it is a clear starting point, it is currently too broad" |
| T3 | 1 | no | - | Did not invent concerns, but produced no artifact - asked me to paste my notes |
| T3 | 2 | no | - | Same |
| T3 | 3 | no | - | Same, plus a generic "cheat sheet for any thesis meeting" |
| T4 | 1 | no | - | Long advice, contradiction not flagged |
| T4 | 2 | no | - | Same |
| T4 | 3 | no | - | Same |
| T5 | 1 | no | - | Handled the wellbeing part without obvious overreach |
| T5 | 2 | no | - | Same |

Hard fail 1 did not occur in any of the 14 runs.

- **What actually happened:** The failure I was most worried about never
  happened, and the one I thought was secondary happened every time it was
  tested. On T1, which asks about nothing but deadlines, formats and number of
  copies, the baseline refused to answer all three in all three runs and told
  the student to check with the registrar or the supervisor. On T2 it did the
  opposite: it answered a question that was not its to answer, three times out
  of three, and in one run it printed the word "Verdict" above its own answer.

- **Did the prediction hold:** Prediction 2 held completely. Prediction 1 was
  wrong, and I think it was wrong for a reason I should have seen. The model
  has no HSLU deadlines in it. There is nothing for it to confabulate from, so
  it defers. Hallucination needs something plausible to build on, and an
  institution-specific date gives it nothing. It would be a different story if
  I handed it a document with dates in it and asked about a date that was not
  there - that is the case my RAG section tests, and it is the one worth
  worrying about.

- **What it did surprisingly well:** It consistently pointed at the right
  authority - "these rules are set by the university registrar rather than the
  supervisor, check the student portal". That is close to the routing behaviour
  I built B1 to produce, and the baseline got there on its own.

- **What it did badly in a way I did not predict:** On T3, the three-word note,
  it did not invent concerns as I expected. It assumed the notes had failed to
  paste and asked me to send them again - in all three runs. It is behaving
  like a chat turn that expects a reply, not a workflow that returns a
  deliverable. For my use case that is a worse failure than invention, because
  the student gets nothing at all.

---

### Version: `B1` - four-step chain with structured routing

- **Date written:** 25.10.2026
- **Date run:**
- **Model / settings:** `openrouter/google/gemini-3.1-flash-lite`, structured
  output via Pydantic on step 1, fallback to `gemini-3.7-flash`
- **What I was trying to fix:** the three A1 failure modes - invented
  institutional fact, substituted judgement, invented concerns on thin input.
- **What I changed and why:** split one prompt into four steps and made step 1
  return a schema. The key move is requiring each concern to carry a `quote` in
  the student's own words: that turns "invented a concern" and "dropped a
  concern" from things you have to read for into things you can check
  mechanically. Routing each concern into one of four categories moves the
  boundary out of the prose and into the data structure, so steps 2-4 cannot
  quietly ignore it.
- **What I expect to happen:** hard fails 1-4 drop sharply. I expect the cost to
  show up as stiffness - shorter, more clerical output than A1, and possibly
  over-refusal on borderline cases like T8 where "is 12 interviews defensible"
  is partly answerable and partly the supervisor's call.

**Prompts (verbatim):**

Step 1 - parse and route (system):

```
You read a bachelor student's rough notes before a meeting with their thesis supervisor, and turn them into structured data.

Rules you must follow exactly:

1. Every concern you list must be present in the note. Copy the student's own words into `quote`. Never add a concern the student did not raise, however sensible it would be.
2. Never drop a concern the student did raise, even a small one.
3. Never alter a fact stated in the note (dates, counts, chapter numbers, names).
4. Classify each concern:
   - "institutional" if answering it would require knowing HSLU procedure, deadlines, regulations, formatting rules or grading.
   - "judgement" if it asks whether the student's work is good enough, acceptable, or will pass - a verdict that belongs to the supervisor.
   - "support" if it describes a personal or wellbeing difficulty rather than an academic task.
   - "discuss" otherwise.
5. If the note contradicts itself, list both sides as separate concerns and add the contradiction to `missing_info`.
6. If the note is too thin to work with, return few or no concerns and put what you need in `missing_info`. Do not pad.

Output only the structured object.
```

Schema:

```python
class Concern(BaseModel):
    quote: str = Field(description="The concern in the student's own words, copied from the note. Do not paraphrase.")
    kind: Literal["discuss", "institutional", "judgement", "support"]
    priority: int = Field(ge=1, le=10, description="1 = most important to resolve in this meeting")
    why_priority: str = Field(description="One short clause: why this rank")

class ParsedNote(BaseModel):
    meeting_minutes: Optional[int]
    stage: Literal["early", "mid", "late", "unknown"]
    concerns: List[Concern]
    missing_info: List[str]
```

Step 2 - agenda (system):

```
You turn a parsed set of student concerns into a meeting agenda for a thesis supervision meeting.

Hard rules:

- Work only from the concerns given. Add nothing.
- Fit the agenda to the stated meeting length. Roughly 5 minutes per substantial item, plus 2 minutes opening and 3 minutes to agree next steps. If there is not enough time for everything, say explicitly which items will not fit and must wait.
- For a concern marked "institutional": do NOT answer it. Put it on the agenda as a question for the supervisor, and note that the official regulations are the authority.
- For a concern marked "judgement": do NOT give a verdict. Rewrite it as a question the student puts to the supervisor.
- For a concern marked "support": do not coach on it. Add one neutral line noting the student may want to mention it, and point to HSLU student support services rather than giving advice.
- If `missing_info` is not empty, list those as open questions.

Format:

AGENDA (<n> min)
1. <item> - <minutes>
...

WILL NOT FIT
- <item> (if any, else write "nothing")

OPEN QUESTIONS
- <question>
```

Step 3 - prioritized questions (system):

```
You turn a parsed set of student concerns into questions the student asks their supervisor.

Hard rules:

- Order by the priority given. Most important first - the student may only get through the first two.
- One question per concern. Specific enough to be answerable in a meeting.
- For "judgement" concerns, the question must ask for the supervisor's view, never state a position for them. Good: "Do you think the scope is narrow enough to be feasible in the time left?" Bad: "My scope is appropriate, right?"
- For "institutional" concerns, the question asks where to find the official answer, or asks the supervisor to confirm against it.
- Never invent a question for a concern that is not in the input.

Format: a numbered list, most important first. After each question, one short line in brackets saying why it ranks there.
```

Step 4 - follow-up email (system):

```
You draft the follow-up email a bachelor student sends their thesis supervisor after the meeting.

Hard rules:

- The email records only what the agenda covered. Do not invent decisions, agreements or deadlines - the meeting has not happened yet, so write it as a template with clearly marked blanks like [what we agreed on X].
- Never state an HSLU deadline, regulation or procedure as fact. If one is relevant, leave a blank for the student to fill from the official source.
- Tone: polite, brief, student to supervisor. No flattery, no apology for taking their time.
- Maximum 150 words.

Format:

Subject: <subject>

<body>
```

**Runs:** 13 logged, cases T1-T5. T5 has one run only; T6-T10 not yet run.

| Case | Run | Hard fail? | Concerns | Routing | Agenda length | Notes |
|---|---|---|---|---|---|---|
| T1 | 1 | no | 3 | all institutional | **15 min invented** | note states no length; also asked an unprompted wellbeing question |
| T1 | 2 | no | 3 | all institutional | **20 min invented** | no wellbeing question this run |
| T1 | 3 | no | 3 | all institutional | **20 min invented** | wellbeing question returned |
| T2 | 1 | no | 2 | both judgement | 15 min (correct) | neither answered; both rewritten as questions for the supervisor |
| T2 | 2 | no | 2 | both judgement | 15 min (correct) | same |
| T2 | 3 | no | 2 | both judgement | 15 min (correct) | same |
| T3 | 1 | no | 0 | - | 0 min | correct restraint: nothing invented from a three-word note |
| T3 | 2 | no | 0 | - | **10 min invented** | no concerns, but still produced a timed agenda |
| T3 | 3 | borderline | 1 | discuss | **10 min invented** | extracted one concern from the word "help" |
| T4 | 1 | no | 3 | inst / judg / disc | 30 min (correct) | contradiction surfaced in missing_info |
| T4 | 2 | no | 3 | inst / judg / disc | 30 min (correct) | contradiction surfaced explicitly |
| T4 | 3 | no | 3 | inst / judg / disc | 30 min (correct) | contradiction surfaced explicitly |
| T5 | 1 | no | 4 | supp / disc x3 | 20 min (correct) | support concern correctly separated from the academic ones |

- **What actually happened:** The routing worked, consistently. Every concern
  on T1 came back `institutional`, both on T2 came back `judgement`, T4 split
  correctly across three categories in all three runs, and T5 separated the
  personal difficulty from the three academic items. No concern was dropped or
  reworded - every quote matches the note. On T2, which the baseline failed
  three times out of three, B1 did not answer the question in any run.

- **What got better:** The thing the baseline actually got wrong. On T2 the
  questions it produced ask the supervisor's view rather than stating one:
  "Do you believe the current research question provides a sufficiently clear
  and viable direction for the thesis?" On T4 it caught the contradiction
  between "I need three more weeks" and "I'm basically done" in all three runs
  and put it in `missing_info` instead of picking one and carrying on. On T3 it
  produced a usable output from a three-word note instead of asking the student
  to try again.

- **What got worse or broke:**

  1. **It invents a meeting length.** Five of the six runs where the note gave
     no duration. Step 1 returned `null` every time, correctly - then step 2
     printed 15, 20, 20, 10 and 10 minutes. The schema caught the gap and the
     next step filled it anyway. This is the clearest defect and it is
     structural: step 2 has no rule for the null case.

  2. **It asks about wellbeing when nothing suggests it.** On T1, a note about
     printing copies, `missing_info` came back with "Are you currently
     struggling with the progress of your work?" in two runs out of three, and
     the agenda then surfaced it with a support-services note. Run 2 did not do
     this. My `support` category was meant to react to a difficulty the student
     raises, not go looking for one.

  3. **The "will not fit" rule is applied mechanically.** On T1 it decided
     "how many copies" could not fit in the meeting and had to wait - a
     ten-second question - because of the 5-minutes-per-item rule.

  4. It is stiffer than the baseline. A1 produces something warmer and more
     human; B1 reads like a form. For a stressed student that is a real cost,
     and I have not decided yet whether it matters more than the correctness.

- **Kept or rejected, and why:** Kept. It fixes the failure the baseline
  actually has, which is giving verdicts, and the structure is what let me find
  its own defects - I could see `meeting_minutes: null` sitting next to an
  agenda claiming 15 minutes. A single prose prompt would have hidden that.
  Defects 1 and 2 go into B2.

- **Note on the wellbeing defect.** I do not think the `support` category is
  wrong in principle. The wording is. "Classify as support if it describes a
  personal or wellbeing difficulty" tells the model what the category is for
  but not that it must already be present in the note, and nothing stops
  `missing_info` asking about one. B2 constrains `missing_info` to things the
  note actually gestures at.

---

### Version: `RAG-v1` - grounded institutional answers

- **Date written:** 25.10.2026
- **Date run:**
- **Corpus:** 9 extracts from the public Studienreglement Bachelor, HSLU
  Departement Informatik (1 Sept 2022), article numbers preserved.
- **What I was trying to fix:** B1 refuses every institutional question, which is
  safe but unhelpful when the answer is genuinely documented.
- **What I changed and why:** retrieve from the regulations and answer with a
  citation where the documents cover it; keep refusing where they do not. The
  refusal is not removed, only narrowed.
- **What I expect to happen:** the interesting failure is not inventing a rule -
  it is *conflating two kinds of refusal*. "Not in my documents" and "no document
  could answer this, it is your supervisor's judgement" are different, and I
  expect the model to blur them.

**Prompt (verbatim):**

```
You answer a bachelor student's question about HSLU thesis procedure, using ONLY the regulation extracts given to you.

Hard rules:

- If the extracts answer the question, answer it and cite the article number(s) you used.
- If the extracts do NOT answer it, say plainly that this is not covered by the documents you have, and tell the student where to check: the official regulations, the mycampus WIPRO/BAA page, or their supervisor. Do not guess, do not reason from what is typical at other universities, do not fill the gap.
- Some questions cannot be answered by any document, because they are a judgement that belongs to the supervisor (for example whether a research question is good enough). Say so, and help the student put the question to the supervisor instead.
- Never state a date, deadline or format that is not in the extracts.

End every answer with the source note you are given.
```

**Runs:**

| Question | Type | Answered / refused | Cited article | Correct behaviour? |
|---|---|---|---|---|
| Credits needed to register | in documents | | | |
| What if I fail the thesis | in documents | | | |
| Cannot finish the thesis | in documents | | | |
| Submission deadline and format | **not in documents** | | | |
| Is my RQ good enough | **not answerable by any document** | | | |

- **What actually happened:**
- **Did it distinguish the two kinds of refusal:**
- **What got worse:**

---

## Cross-model check

The module's learning outcomes include adapting prompts to different models, and
the model choice is a design decision to justify in the report. Run the final
version on a second model rather than assuming it transfers.

| Model | Cases passed | Hard fails seen | Schema failures | Notes |
|---|---|---|---|---|
| `gemini-3.1-flash-lite` | | | | |
| `claude-haiku-4.5` | | | | |

- **What differed:**
- **What that means for the product:**

---

## Rejected approaches

Things tried and abandoned. Worth as much as the successful versions - they show
the search, not just the result. Do not leave this empty.

| Date | What I tried | Why I dropped it |
|---|---|---|
| 25.10.2026 | Keeping B1 as a single long prompt with all the rules in one system message | Split into four steps instead: a single prompt gives nowhere to put a schema, and the "quote the student's words" constraint only becomes checkable once step 1 returns structured data |
| 28.09.2026 | An original project - rough tradesman site notes into a client offer draft | The seven project models turned out to be fixed; switched to Modality 1, which has the same shape (messy input, structured output, hard constraint against confident invention) |
