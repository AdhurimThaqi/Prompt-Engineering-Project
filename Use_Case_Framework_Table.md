# Use-Case Framework Table

**Project:** Modality 1 - Text: Bachelor Thesis Meeting Prep Coach
**Student:** Adhurim Thaqi (individual)
**Module:** PROMPT H26
**Framework:** Use-Case Framework Table, PROMPT W3

---

| Field | Content |
|---|---|
| **Use-case** | Preparing for a bachelor thesis supervisor meeting |
| **Who's it for?** | An HSLU bachelor student with a supervisor meeting coming up - typically 20-30 minutes of the supervisor's time and a half-formed list of worries |
| **Job to be done (task)** | Turn a messy pre-meeting note into a focused meeting plan, and capture what was agreed afterwards |
| **Input** | The student's own rough notes: unstructured, incomplete, mixed concerns, sometimes contradictory. Plus the meeting length and where they are in the thesis |
| **Output format** | Three parts: (1) a meeting agenda fitting the stated time, (2) prioritized questions with the most important first, (3) a follow-up email draft. Plain text, editable |
| **Quality bar (what "good" must include)** | - Every concern in the note appears in the output<br>- Questions prioritized, not just listed<br>- Agenda fits the stated meeting length<br>- Gaps in the note raised as open questions, not filled in<br>- Follow-up email matches what the agenda actually covered<br>- Tone appropriate for writing to a supervisor<br>- No HSLU procedure, deadline, regulation or grading rule stated as fact<br>- No verdict on the student's work that belongs to the supervisor |
| **Risks / ethics** | - **Invented institutional fact** is the highest-consequence failure: a confident wrong deadline could make a student miss a real one. Route to "ask your supervisor" or "check the official regulations"<br>- **Substituted judgement**: the toolkit helps formulate the question, it does not answer "is my topic good enough?"<br>- **Privacy**: synthetic test notes only; real notes describe identifiable supervisors and personal circumstances<br>- **Not official HSLU communication**: educational prototype, labelled as such<br>- **Out of scope**: a note raising a personal or wellbeing difficulty is pointed to HSLU support services, not coached on<br>- **Disclosure**: AI use disclosed in the process record |

---

## How this maps to the evaluation

The quality bar above splits into the two tiers used in testing:

**Hard fails** (one occurrence fails the case): states an HSLU procedure or
deadline as fact; delivers a verdict belonging to the supervisor; invents a
concern not in the note; silently drops a concern that was in the note; alters
a fact from the note.

**Scored criteria:** prioritization, agenda fit, gaps surfaced, email accuracy,
tone, usable length.

Tested on 10 synthetic notes, 3 runs per case (sampling means a single run
measures luck as well as prompt quality), baseline vs. refined workflow, plus
blind scoring by 2-3 students who have had supervisor meetings.
