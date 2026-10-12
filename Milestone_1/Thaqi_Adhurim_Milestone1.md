# PROMPT H26 - Milestone 1: Project Choice

**Student:** Adhurim Thaqi
**Date:** 28.09.2026
**Format:** Individual project

---

## Project selected

**Modality 1 - Text: Bachelor Thesis Meeting Prep Coach**

Taken as written in the project brief, not adapted.

**What I will create (per the brief):** a reusable prompt-based
meeting-preparation toolkit - three realistic student scenarios; a meeting
agenda, prioritized questions and follow-up email for each; a short user
guide and a clear boundaries statement.

**Core AI challenge (per the brief):** turn a messy student note into a
focused, useful meeting plan without inventing HSLU procedures or replacing
supervisor judgement.

---

## Stakeholder and intended user

**Primary user:** an HSLU bachelor student preparing for a supervisor
meeting - typically holding 20-30 minutes of a supervisor's time and a
half-formed list of worries.

**Need:** supervisor time is scarce and students arrive with an unstructured
set of concerns. The meeting drifts, the most important question gets asked
last or not at all, and nothing is written down afterwards.

**Scope:** preparing for and following up on one meeting. Not thesis writing,
not research advice, not supervision itself.

Per the project brief, this is a simulated scenario: no real supervisor or
student is contacted, and the toolkit is an educational prototype, not
official HSLU communication, policy or advice.

---

## Prompt / workflow challenge

The brief names the challenge directly. Two distinct failure modes follow
from it.

**1. Invented institutional fact.** Asked about deadlines, formatting rules,
submission procedure or grading, a model will produce something that sounds
plausible and official. A student could act on it. The workflow must route
these to "ask your supervisor" or "check the official regulations" instead
of answering.

**2. Substituted judgement.** Asked "is my research question good enough?",
the toolkit should help the student *formulate that question for the
supervisor*, not deliver a verdict that displaces the supervisor's.

A third, quieter challenge: student notes are incomplete, and the model's
default is to close gaps with plausible invention rather than flag them.

---

## Evaluation plan

**Method:** 10-case / 80% test (option a), supported by comparative blind
review (option c). The task has objective pass/fail properties - an invented
HSLU deadline is unambiguously a failure - which is what makes the 10-case
test appropriate here.

**Test corpus:** ten synthetic student notes written by me, kept separate
from the three scenarios that ship as the product. No real student notes are
used; real notes describe identifiable supervisors and personal
circumstances.

Edge cases built in deliberately:

- a note asking directly about a submission deadline
- a note asking "is my topic good enough?"
- a three-word note
- a note containing an internal contradiction
- a note raising a personal difficulty alongside the academic one

**Hard fails** (one occurrence fails the case):

1. States an HSLU procedure, deadline, regulation or grading rule as fact
2. Delivers a verdict that belongs to the supervisor
3. Invents a concern or topic not present in the student's note
4. Silently drops a concern the student did raise
5. Alters a fact stated in the note

**Scored criteria:** questions genuinely prioritized rather than listed;
agenda fits the stated meeting length; gaps surfaced as open questions;
follow-up email accurately reflects the agenda; tone appropriate for writing
to a supervisor; usable without heavy editing.

**Baseline comparison:** one simple out-of-the-box prompt, then at least two
meaningful refinements, run across the same ten cases.

**Repeat runs:** because sampling makes the same prompt produce different
answers, each case is run three times rather than once. A constraint the
model respects twice and breaks on the third attempt has not been respected.
A single run would measure luck alongside prompt quality.

**Independent review:** two or three HSLU students who have had supervisor
meetings score a sample of outputs blind, without being told which version
came from which prompt. This addresses the risk, named in the brief, of
evaluating only my own preferred outputs in an individual project.

---

## Responsible use

- **Accuracy:** the highest-consequence failure is a confident, invented
  HSLU rule, because a student could miss a deadline acting on it. The
  boundaries statement and the routing behaviour both exist for this.
- **Not official HSLU communication:** the toolkit is labelled an
  educational prototype, per the project brief.
- **Privacy:** synthetic test notes only. Real notes would describe
  identifiable supervisors and personal circumstances.
- **Human oversight:** the toolkit prepares the student for the
  conversation; it does not replace the supervisor. The boundaries statement
  says this in plain language to the user, not only in the report.
- **Scope of support:** if a note raises a personal or wellbeing difficulty,
  the toolkit does not coach on it. It points to the appropriate HSLU
  support service instead of generating advice.
- **Accessibility:** outputs are plain-text and screen-reader friendly; the
  user guide avoids assuming prior familiarity with AI tools.
- **Disclosure:** full AI-use disclosure in the individual process record.

---

## Early baseline probe

Ahead of Milestone 3, a zero-shot baseline ("help me prepare for my thesis
supervisor meeting, here are my notes") is run on a small number of rough
notes, to check that the failure modes above are real rather than assumed.

*Observations to be completed after the probe:*

- Case 1 - note used:
- Case 2 - note used:
- Case 3 - note used:
- Institutional facts the baseline invented:
- Judgements it made that belong to the supervisor:
- What it omitted:

---

## Working mode

Individual. External reviewers are involved at the evaluation stage only;
they do not contribute to design or production.
