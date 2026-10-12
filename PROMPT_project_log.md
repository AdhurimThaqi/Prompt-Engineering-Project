# PROMPT H26 - Project Log

**Student:** Adhurim Thaqi
**Module:** Prompt Engineering for Beginners (PROMPT), HS26 - Shaelom Fischer
**Mode:** Individual project
**Project:** Modality 1 - Text: Bachelor Thesis Meeting Prep Coach

> Living document. Update after every working session. Everything in the
> report and the individual process record gets built from this file.

---

## 1. Project definition (Milestone 1 - due W3, 28.09.2026)

| Item | Decision |
|---|---|
| Project | Modality 1, Bachelor Thesis Meeting Prep Coach, taken as written |
| Intended user | HSLU bachelor student preparing for a supervisor meeting |
| Input | Messy, unstructured pre-meeting notes |
| Output | Meeting agenda, prioritized questions, follow-up email - for three scenarios |
| Also delivered | Short user guide; clear boundaries statement |
| Working language | English |
| Test corpus | 10 synthetic student notes, written by me, separate from the three shipped scenarios |
| Evaluation | 10-case / 80% test against hard fails + scored criteria; 3 runs per case; blind review by 2-3 students |

### What the AI is and is not doing

In scope: turning a messy note into a focused meeting plan - agenda,
prioritized questions, follow-up email.

Explicitly out of scope: answering questions about HSLU procedure, deadlines,
regulations or grading, and judging the quality of the student's research.
Both are routed to the supervisor or the official regulations. This boundary
is the core design decision, not an omission.

---

## 2. Decision log

Format: date - decision - reasoning - alternatives rejected.

**14.09.2026 - Individual project, not pair.**
Preference for working solo; established working pattern.
*Rejected:* pair work. *Mitigation for the known risk (evaluating only my own
preferred outputs):* external reviewers at the evaluation stage.

**21.09.2026 - Reconsidered pairing after syllabus V2.**
V2 allows groups of 2-3 and adds contribution-based mark adjustment. Asked one
classmate whether she wanted to pair. Set a decision deadline rather than
waiting indefinitely.

**28.09.2026 - Confirmed solo.** No response by the deadline. Proceeding
individually with external reviewers at the evaluation stage.

**28.09.2026 - Switched from an original project to Modality 1.**
Had scoped an original project: turning a tradesman's rough site notes into a
client offer draft. Confirmed in the W3 session that the seven project models
are fixed and original proposals are not being taken this semester, so the
original idea was dropped.
*Chose Modality 1 (Bachelor Thesis Meeting Prep Coach)* because it is the
closest structural match to the design work already done: messy unstructured
input, structured multi-part output, and a hard constraint against confident
invention. The evaluation design, hard-fail/scored-criteria split and
responsible-use reasoning transferred directly.
*Rejected:* Modality 7 (Course Communication Checker) - viable, but the
evaluation is harder to make objective.
*Carried over unchanged:* synthetic test corpus, 3 runs per case, blind
external review, hard fails vs. scored criteria.

**28.09.2026 - Synthetic test corpus, separate from the shipped scenarios.**
Real student notes describe identifiable supervisors and personal
circumstances. The project brief states the models are simulated scenarios and
that the named stakeholder need not be contacted. Synthetic notes also give
full control over edge cases.
*Rejected:* collecting real notes from classmates.

**28.09.2026 - Three runs per test case, not one.**
W2 established that sampling makes the same prompt produce different answers. A
constraint respected twice and broken on the third attempt has not been
respected. A single run per case would measure luck alongside prompt quality.

---

## 3. Quality bar - what makes an output PASS

### Hard fails (one occurrence fails the case)

- [ ] States an HSLU procedure, deadline, regulation or grading rule as fact
- [ ] Delivers a verdict that belongs to the supervisor
- [ ] Invents a concern or topic not present in the student's note
- [ ] Silently drops a concern the student did raise
- [ ] Alters a fact stated in the note

### Scored criteria

- [ ] Questions genuinely prioritized, not just listed
- [ ] Agenda fits the stated meeting length
- [ ] Gaps in the note surfaced as open questions, not filled in
- [ ] Follow-up email accurately reflects the agenda
- [ ] Tone appropriate for writing to a supervisor
- [ ] Usable without heavy editing

*(Refine the scored criteria into something a blind reviewer can apply
consistently - each needs to be judgeable without seeing the prompt.)*

---

## 4. Prompt log

Kept in its own file: **Prompt_Log.md** (same folder).

Rule for that file: prompt text is recorded verbatim, exactly as run. The
prompt is the artifact under test, so a tidied-up version is a different
prompt and the baseline/refined comparison stops meaning anything. The
reasoning around each prompt is written up properly.

The brief requires a baseline plus at least two meaningful refinements.

---

## 5. Evidence collected

The brief requires at least one weak, failed, unexpected or edge-case result.
Log these as they happen rather than hunting for them in December.

| # | Case | Prompt version | Run | Issue observed |
|---|---|---|---|---|
| | | | | |

Edge cases to build into the corpus:

- a note asking directly about a submission deadline
- a note asking "is my topic good enough?"
- a three-word note
- a note containing an internal contradiction
- a note raising a personal difficulty alongside the academic one

---

## 6. Responsible use

- **Accuracy:** the highest-consequence failure is a confident, invented HSLU
  rule - a student could miss a deadline acting on it.
- **Not official HSLU communication:** educational prototype, labelled as
  such, per the project brief.
- **Privacy:** synthetic test notes only; real notes would describe
  identifiable supervisors and personal circumstances.
- **Human oversight:** the toolkit prepares the student for the conversation;
  it does not replace the supervisor. Stated in plain language to the user in
  the boundaries statement, not only in the report.
- **Scope of support:** a note raising a personal or wellbeing difficulty is
  pointed to the appropriate HSLU support service, not coached on.
- **Accessibility:** plain-text, screen-reader-friendly output; user guide
  assumes no prior familiarity with AI tools.
- **Disclosure:** see section 8.

---

## 7. Milestones

| # | Deliverable | Due | Status |
|---|---|---|---|
| 1 | Project choice & team | 28.09.26 | Done - Modality 1, solo |
| 2 | Project brief | 12.10.26 | |
| 3 | Baseline, workflow design, first prototype | 26.10.26 | |
| 4 | Draft product & revision plan | 09.11.26 | |
| 5 | Near-final product, evidence check | 30.11.26 | |
| 6 | Final presentation | 07.12.26 | |
| 7 | Final report (1,500-2,000 words) | 17.12.26 | |

---

## 8. AI-use disclosure (draft - rewrite in own words before submission)

Tools used, what for, and which decisions were mine. To be completed honestly
and specifically; "used AI for brainstorming" is not sufficient.

Points to cover: Claude was used as a thinking partner for project scoping and
to challenge my own assumptions, and was deliberately **not** used as the
judge of output quality, because a model is a poor evaluator of its own output
- hence the blind external review. Note also which models were used for
generation vs. testing, and where their behaviour differed.

---

## 9. Open items

- [ ] Write the three shipped student scenarios
- [ ] Write the 10 synthetic test notes, including the edge cases in §5
- [ ] Turn the scored criteria into a reviewer-usable rubric
- [ ] Run the zero-shot baseline and log it
- [ ] Recruit 2-3 students for the blind review (ask early)
- [ ] Decide delivery surface for the toolkit (structured chat workflow vs.
      small prototype)
- [ ] Decide which second model to cross-test on, and why
