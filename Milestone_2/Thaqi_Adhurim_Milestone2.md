# PROMPT H26 - Milestone 2: Project Brief

**Student:** Adhurim Thaqi
**Project:** Modality 1 (Text) - Bachelor Thesis Meeting Prep Coach
**Date:** 12.10.2026
**Format:** Individual project

---

## 1 · Stakeholder and target audience

**Primary user:** an HSLU bachelor student preparing for a meeting with their
thesis supervisor - typically holding 20-30 minutes of the supervisor's time and
a half-formed list of worries.

**Secondary beneficiary:** the supervisor, who gets a meeting with a structure
and a written follow-up instead of a drifting conversation.

Per the project brief, the models are simulated scenarios: no real supervisor or
student is contacted, and the toolkit is an educational prototype, not official
HSLU communication, policy or advice.

---

## 2 · The real-world need

Supervision time is scarce and unevenly used. Students arrive with an
unstructured set of concerns, so:

- the meeting drifts and runs out of time
- the most important question gets asked last, or not at all
- nothing is written down, so the next meeting re-opens settled ground
- procedural uncertainty ("is an extension possible?") eats time that could go
  to the actual work

None of this is a knowledge problem. The student usually knows what is wrong.
The problem is shape: an unordered list of worries is not a plan for a
twenty-minute conversation.

---

## 3 · The task

Take the student's rough, unstructured pre-meeting note and produce:

1. a **meeting agenda** fitted to the stated meeting length
2. **prioritized questions**, most important first
3. a **follow-up email** draft recording what was covered

Plus, shipped with the toolkit: a short **user guide** and a **boundaries
statement** written for the student, in plain language.

---

## 4 · Scope

**In scope:** preparing for, and following up on, one supervisor meeting.

**Out of scope, deliberately:**

| Not doing | Why |
|---|---|
| Thesis writing or editing | A different task with different failure modes |
| Research or methods advice | Belongs to the supervisor |
| Judging the quality of the student's work | Belongs to the supervisor |
| Answering HSLU procedure from memory | The model cannot know it, and a confident wrong answer is the worst outcome in this project |

The last two are not omissions. They are the design.

---

## 5 · The prompt / workflow challenge

The brief states it directly: turn a messy student note into a focused, useful
meeting plan **without inventing HSLU procedures or replacing supervisor
judgement.**

Three failure modes follow.

**1 · Invented institutional fact.** Asked about deadlines, formatting rules,
submission procedure or grading, a model produces something plausible and
official-sounding. A student could act on it and miss a real deadline. This is
the highest-consequence failure in the project.

**2 · Substituted judgement.** Asked "is my research question good enough?", the
model should help the student *put that question to the supervisor*, not deliver
a verdict that displaces it. Notes often apply pressure here - "just tell me yes
or no".

**3 · Invention on thin input.** Student notes are incomplete. The model's
default is to close gaps with plausible content rather than flag them, because a
generic agenda is easier to produce than an admission that there is not enough
to work with.

---

## 6 · Evaluation plan

**Method:** 10-case / 80% test (brief option a), supported by comparative blind
review (option c). The task has objective pass/fail properties - an invented
HSLU deadline is unambiguously a failure - which is what makes the 10-case test
appropriate here rather than a purely qualitative rubric.

**Corpus.** Two separate sets, and keeping them separate is what makes the test
measure anything:

- **three shipped scenarios** - the product, tuned against
- **ten synthetic test notes** - the evaluation set, never tuned against

Edge cases built into the test set deliberately: a direct procedural question; a
demand for a verdict; a three-word note; a note that contradicts itself; a note
raising a personal difficulty alongside the academic one.

**Hard fails** - one occurrence fails the case:

1. States an HSLU procedure, deadline, regulation or grading rule as fact
2. Delivers a verdict that belongs to the supervisor
3. Invents a concern not present in the note
4. Silently drops a concern that was in the note
5. Alters a fact stated in the note

**Scored criteria:** questions genuinely prioritized rather than listed; agenda
fits the stated meeting length; gaps surfaced as open questions; follow-up email
accurately reflects the agenda; tone appropriate for writing to a supervisor;
usable without heavy editing.

**Baseline comparison:** one simple out-of-the-box prompt, then at least two
meaningful refinements, across the same ten cases.

**Three runs per case.** W2 established that sampling makes the same prompt
produce different answers. A constraint respected twice and broken on the third
attempt has not been respected; a single run would measure luck alongside prompt
quality.

**Independent review:** two or three HSLU students who have had supervisor
meetings score a sample of outputs blind, without being told which version came
from which prompt. This addresses the risk, named in the brief, of evaluating
only my own preferred outputs in an individual project.

---

## 7 · Ethical risks and responsible use

| Risk | Response |
|---|---|
| **Invented institutional fact** - a student misses a real deadline acting on a confident wrong answer | Never answered from model memory. Either grounded in the real regulations with a citation, or refused and redirected to the official source |
| **Displacing the supervisor** - the student takes the tool's verdict instead of asking | Judgement questions are structurally rerouted into questions the student asks. Stated to the user in the boundaries statement, not only in the report |
| **Mistaken for official HSLU material** | Labelled an educational prototype in the output itself |
| **Privacy** - real notes describe identifiable supervisors and personal circumstances | Synthetic test notes only. No real note, supervisor or meeting is used |
| **Wellbeing** - a note may raise a personal difficulty | Not coached on. Routed to HSLU student support services |
| **Accessibility** | Plain-text, screen-reader-friendly output; user guide assumes no prior familiarity with AI tools |

**Disclosure:** full AI-use disclosure in the individual process record.

---

## 8 · One open design decision

W4 introduced retrieval, which changes the options for failure mode 1.

Milestone 1 committed to **refusing** every institutional question, on the
grounds that an ungrounded model asked about a deadline can only guess. With
RAG there is a third option: **ground** the toolkit in the real HSLU regulations
so it answers what is documented, cites it, and refuses only what lies outside
the documents.

Grounding is the better product if a usable document set exists. It is also the
more interesting evaluation, because it splits one refusal into two:

- *not in my documents* - go and check the official source
- *no document could answer this* - it is your supervisor's judgement

Those are different answers and a toolkit that conflates them is worse than one
that separates them.

**To be settled by Milestone 3**, once it is clear what documentation is
actually available. The refusal behaviour is kept either way; the question is
only how wide its scope is.

---

## 9 · Deliverables

| Deliverable | Form |
|---|---|
| Three realistic student scenarios | Written cases, with agenda + questions + follow-up email for each |
| Prototype | Python chain following the W4 pattern, runnable in Colab |
| User guide | Short, plain language |
| Boundaries statement | What the toolkit will not do, written for the student |
| Evidence | Prompt log (verbatim prompts, every version), run log, scored test results |
| Report + process record | Per the module deliverables sheet |

---

## 10 · Feasibility

The W3 criteria for a feasible idea were a defined user, a specific task, and a
product that can realistically be built.

- **Defined user:** a bachelor student with a supervisor meeting this week.
- **Specific task:** one note in, three artifacts out.
- **Realistic product:** text only, no interface required beyond a notebook, and
  the evaluation runs on ten synthetic cases I write myself. Nothing in the plan
  depends on recruiting participants or on access I do not have.

The main risk is not technical. It is leaving the test runs until late, when the
iteration evidence needs weeks of accumulation to be worth anything.
