# Bachelor Thesis Meeting Prep Coach

A prompt-engineered workflow that turns a bachelor student's messy pre-meeting
notes into a focused plan for a thesis supervisor meeting: an agenda, prioritized
questions, and a follow-up email.

Semester project for **PROMPT - Prompt Engineering for Beginners**, HSLU HS26.
Modality 1 (Text), individual project. Adhurim Thaqi.\

- Open the web-based prototype via this link https://adhurimthaqi.github.io/Prompt-Engineering-Project/

---

## The problem

Supervisor time is scarce. Students arrive with an unstructured list of worries,
the meeting drifts, the most important question gets asked last or not at all,
and nothing is written down afterwards.

## The hard part

Not summarising notes - any model does that. The challenge, as the project brief
states it, is doing it **without inventing HSLU procedures or replacing
supervisor judgement.**

Two failure modes follow:

- **Invented institutional fact.** Asked about a deadline or a submission rule, a
  model produces something plausible and official-sounding. A student could act
  on it and miss a real deadline.
- **Substituted judgement.** Asked "is my research question good enough?", a
  model delivers a verdict that belongs to the supervisor.

## The approach

A four-step chain, with the boundary enforced in the data structure rather than
in prose:

```
note --> [1] parse & route --> [2] agenda --> [3] prioritized questions --> [4] follow-up email
         (structured output)
```

Step 1 returns a schema in which every concern carries a `quote` in the student's
own words and a routing category:

| Category | Behaviour |
|---|---|
| `discuss` | goes on the agenda |
| `institutional` | answered from the regulations with a citation, or refused and redirected |
| `judgement` | never answered; rewritten as a question the student asks |
| `support` | not coached on; pointed to HSLU support services |

Requiring the quote makes two of the five hard fails mechanically checkable: an
invented concern has no quote in the note, and a dropped concern has a quote that
appears nowhere in the output.

Institutional questions are grounded by retrieval against the public
*Studienreglement Bachelor, HSLU Departement Informatik*, with article numbers
kept so every answer is checkable. Where the documents are silent, the toolkit
refuses rather than guessing.

---

## Repository layout

```
Project/
├── Readme.md
├── Milestone_1/ … Milestone_4/   Milestone submissions
├── Product/
│   └── User_Guide_and_Boundaries.md   for the student
├── Prototype/
│   ├── thesis_meeting_prep_prototype.ipynb   A1, B1, B2, RAG
│   ├── workflow_b2.py      current version (same code as notebook §7)
│   ├── checks.py           automatic flags for candidate hard fails
│   └── run_m4.py           batch runner (runs the notebook's own code)
├── docs/                   project page (GitHub Pages)
│   ├── index.html
│   ├── outputs.json        generated - do not edit by hand
│   ├── annotations.json    my reading notes, the only hand-written page text
│   └── build_outputs.py    run_log.jsonl + annotations -> outputs.json
├── Prompt_Folder/
│   ├── Prompt_Log.md               every prompt version, verbatim
│   └── PROMPT_project_log.md       decisions, quality bar, milestones
├── Use_Case_Framework/     Use-case framework table (W3)
└── Scenarios_and_Test_Corpus.md
```

## Running the prototype

1. Open `Prototype/thesis_meeting_prep_prototype.ipynb` in Google Colab.
2. Add the course OpenRouter key to Colab Secrets as `OPENROUTER_API_KEY`.
   Never paste a key into a cell.
3. Run top to bottom. Section 7 is the current version, B2.

Locally (Windows/macOS/Linux), from the `Project` folder with
`OPENROUTER_API_KEY` set in the environment:

```
python Prototype/run_m4.py scenarios   # B2 on S1-S3
python Prototype/run_m4.py b2tests     # B2 on T1-T10, three runs each
python Prototype/checks.py             # automatic flags, B1 vs B2
python docs/build_outputs.py           # refresh the project page data
```

Every run appends one line to `run_log.jsonl`: timestamp, case, run number,
prompt version, model, latency, tokens, cost, input and output.

---

## Results so far (Milestone 4)

| | A1 baseline | B1 chain | B2 revised |
|---|---|---|---|
| Test cases without a hard fail (target 8/10) | 4/10 | 2/10 | **7/10** |
| Runs flagged by `checks.py` | - | 19/30 | 3/30 |

A1 fails by *answering*: verdicts on T2/T6/T8, and HSLU expectations stated
as fact on T9. B1 never does that, but it fails by *drift* between steps:
`missing_info` promoted to the agenda, and deadlines added to the email. B2
fixes most of the drift. What is left, and the plan for B3, is in
`Milestone_4/Thaqi_Adhurim_Milestone4.md`.

## Evaluation

**Corpus.** Three shipped scenarios (tuned on) and ten synthetic test notes
(tested on, never tuned on). Keeping them separate is what makes the test
measure anything.

**Three runs per case.** Sampling means a single run measures luck as much as
prompt quality. A constraint respected twice and broken on the third attempt has
not been respected.

**Hard fails** - one occurrence fails the case:

1. States an HSLU procedure, deadline, regulation or grading rule as fact
2. Delivers a verdict that belongs to the supervisor
3. Invents a concern not present in the note
4. Silently drops a concern that was in the note
5. Alters a fact stated in the note

**Scored criteria:** prioritization, agenda fits the stated length, gaps surfaced
as open questions, follow-up email matches the agenda, tone appropriate for
writing to a supervisor, usable without heavy editing.

---

## Responsible use

- **Educational prototype.** Not official HSLU communication, policy or advice,
  and labelled as such in the output itself rather than only in the
  documentation.
- **Regulation extracts** were gathered from the published Studienreglement PDF
  for this prototype. They carry a source note in every grounded answer and
  should be verified against the source before anyone relies on them.
- **Privacy.** All student notes in this repository are synthetic. No real note,
  supervisor or meeting was used.
- **Human oversight.** The toolkit prepares the student for the conversation. It
  does not replace the supervisor.
- **Wellbeing.** A note raising a personal difficulty is routed to HSLU support
  services, not coached on. The `support` category exists so this is a
  structural property of the workflow rather than a hope about the prompt.
- **Keys** are read from Colab Secrets, never committed, and never logged.

---

## Status

| Milestone | Due | State |
|---|---|---|
| 1 · Project choice | 28.09.26 | Done |
| 2 · Project brief | 12.10.26 | Submitted |
| 3 · Baseline, workflow, prototype | 26.10.26 | Done |
| 4 · Draft product & revision plan | 09.11.26 | Done - 90 test runs; A1 4/10, B1 2/10, B2 7/10 cases without a hard fail |
| 5 · Near-final product, evidence check | 30.11.26 | |
| 6 · Final presentation | 07.12.26 | |
| 7 · Final report | 17.12.26 | |

---

## Sources

- Project brief and syllabus: PROMPT H26, Shaelom Fischer, HSLU
- Chain pattern, structured outputs, `log_run`, RAG: W4 *Prompt Engineering for
  Developers*, Dr. Marc Bravin, HSLU
- [Studienreglement für die Bachelor-Ausbildung, HSLU Departement Informatik](https://www.hslu.ch/-/media/campus/common/files/dokumente/h/ueber-uns/systematische-rechtssammlung/4-informatik/h-studienreglement-bachelor-hslu-i.pdf) (in force 1 Sept 2022)

## AI-use disclosure

See the individual process record. In short: Claude was used as a thinking
partner for scoping, for drafting documentation and prototype scaffolding, and
to challenge design decisions. It was deliberately **not** used as the judge of
output quality - a model is a poor evaluator of its own output, which is why the
evaluation uses a written quality bar and blind scoring by other students.
