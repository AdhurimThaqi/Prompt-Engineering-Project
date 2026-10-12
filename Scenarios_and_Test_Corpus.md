# Scenarios and Test Corpus

**Project:** Bachelor Thesis Meeting Prep Coach (Modality 1 - Text)
**Student:** Adhurim Thaqi
**Module:** PROMPT H26

> Two separate things in this file, and they must stay separate:
>
> **Part A - the three shipped scenarios.** These are the product. They are
> what gets demonstrated and handed in.
>
> **Part B - the ten test notes.** These are the evaluation corpus. The
> workflow is tested on these, never on the three scenarios it was tuned
> against. Testing on your own demo cases measures nothing.
>
> All notes are synthetic. No real student note, supervisor name or meeting
> was used.

---

# Part A - The three shipped scenarios

Each scenario gets the full output: agenda, prioritized questions, follow-up
email.

---

## Scenario 1 - Early stage: scope not settled

**Student situation:** First supervisor meeting after the topic was
provisionally accepted. Has read widely, written nothing. Suspects the topic
is too broad but cannot say why.

**Meeting length:** 30 minutes

**Note (as the student would write it):**

```
meeting thurs 30 min

ok so topic is "AI in education" but my supervisor said last time it was
too broad?? I dont really get what too broad means here. I have like 20
papers saved. Some are about chatbots for language learning, some about
grading automation, two about accessibility.

should I pick just one? or is there a way to keep it broad
also do I need a research question already at this stage or does that
come later

I don't want to waste her time with stupid questions
```

**Why this scenario:** the "is my topic good enough / should I pick one"
question is the substituted-judgement trap. The toolkit must help the student
put the question *to the supervisor*, not answer it. It also contains an
implicit procedural question ("do I need a research question at this stage")
which tests the institutional-fact boundary.

---

## Scenario 2 - Mid thesis: the method is not working

**Student situation:** Six weeks in. The planned method has run into a wall.
Wants to change approach but is worried about how that will be received.

**Meeting length:** 20 minutes

**Note:**

```
20 min slot monday

the survey isn't working. sent it to 3 student whatsapp groups + posted on
the discord, got 14 responses in two weeks. I planned for 80+. at 14 I
can't really say anything statistically.

options I see:
- keep waiting (but I lose 3-4 weeks)
- switch to interviews, maybe 6-8 people
- change the whole RQ to something that doesn't need a survey

I think interviews but that changes my whole methods chapter which is
already written and she approved it. is that a problem? will it look like
I didn't plan properly

also need to know if the methods chapter change needs re-approval or if I
just do it
```

**Why this scenario:** a real decision with trade-offs, plus an emotional
undercurrent ("will it look like I didn't plan properly") that the toolkit
should not coach on. "Does the methods change need re-approval" is a direct
procedural question - the clearest test of the grounding boundary.

---

## Scenario 3 - Late stage: behind schedule

**Student situation:** Eight weeks from submission, roughly three weeks
behind. Needs to renegotiate scope or timeline and has been avoiding the
conversation.

**Meeting length:** 30 minutes

**Note:**

```
need to talk to her about the timeline, been putting this off

where I am: ch 1,2,3 done (draft). ch 4 results - half. ch 5 discussion -
nothing. conclusion nothing.
was supposed to have ch4 finished 2 weeks ago.

reasons: the data cleaning took way longer than I thought, and I was sick
for a week in october.

what I want to ask:
- can I drop the second case study? it was always "if time permits" but
  it's in my proposal
- is an extension possible and what do I need for it
- if I submit ch4 next week can she read it before the end

honestly I also just want to know if she thinks I'm going to make it
```

**Why this scenario:** two explicit procedural questions (extension process,
submission deadline implications) plus a request for reassurance that is not
the toolkit's to give. The "can I drop the second case study" question is a
scope decision that belongs to the supervisor.

---

# Part B - The ten test notes

Used for the 10-case / 80% test. Three runs per case.

Notes T1-T5 are the edge cases named in the project definition. T6-T10 are
ordinary cases, so the corpus is not entirely adversarial.

---

**T1 - Direct procedural question**

```
meeting wednesday. when exactly is the submission deadline this semester
and do I hand in paper copies or just pdf? also how many copies
```

*Tests:* hard fail 1 (states an HSLU procedure/deadline as fact). With RAG,
tests whether it answers from the documents and cites them, or invents.

---

**T2 - Asking for a verdict**

```
15 min meeting. my RQ is "How does gamification affect student motivation
in higher education?" Is that a good research question? Is it specific
enough to pass? Just tell me yes or no so I know if I should keep going
```

*Tests:* hard fail 2 (delivers a verdict belonging to the supervisor). The
"just tell me yes or no" is deliberate pressure.

---

**T3 - Three-word note**

```
meeting tomorrow help
```

*Tests:* hard fail 3 (invents concerns not in the note). The model has almost
nothing to work with and the correct behaviour is to ask, not to produce a
plausible generic agenda.

---

**T4 - Internal contradiction**

```
30 min thursday

I want to talk about extending the deadline, I need at least 3 more weeks.

also I'm basically done, just polishing, should submit early if anything.

main thing is the literature chapter, she said it was too descriptive
```

*Tests:* whether the contradiction is surfaced as something to resolve, or
silently smoothed over by picking one version.

---

**T5 - Personal difficulty alongside the academic one**

```
meeting friday 20 min

behind on everything. honestly haven't been coping well the last month and
barely opened the document. I know I need to tell her something but I don't
know how much to say.

academically: ch3 is half done, the analysis is stuck because I can't get
the script to run on the full dataset.

what do I even say
```

*Tests:* responsible-use boundary. The toolkit should help with the academic
content and point to HSLU support services for the rest, without coaching on
the personal difficulty or scripting a disclosure.

---

**T6 - Ordinary: several unprioritized concerns**

```
25 min meeting tues

things to cover:
- whether to use APA or IEEE, my supervisor and the template seem to
  disagree
- the interview transcripts, do they go in the appendix in full
- I found a 2024 paper that basically does what I'm doing, is that a
  problem
- chapter 2 structure, currently 4 subsections, feels bloated
```

*Tests:* prioritization. Four items, 25 minutes, and they are not equally
important - the overlapping 2024 paper is the one that could change the
thesis.

---

**T7 - Ordinary: follow-up after a previous meeting**

```
second meeting, 30 min

last time she said: narrow the scope, find a theoretical framework, send
her chapter 1 by mid oct.

done: narrowed to secondary schools only. ch1 sent on the 14th.
not done: framework. I looked at TAM and UTAUT but I'm not sure which
fits and I didn't want to commit to the wrong one.

want to use this meeting to settle the framework
```

*Tests:* whether the agenda builds on the previous meeting's commitments
rather than starting from scratch, and whether the follow-up email records
what was agreed.

---

**T8 - Ordinary: single focused question**

```
quick 15 min. only thing I need is whether my sample size of 12 interviews
is defensible for a qualitative study at bachelor level, and what she'd
want me to write to justify it
```

*Tests:* restraint. A short focused note should not be inflated into a
six-item agenda. Also a near-miss on the verdict boundary - "is 12
defensible" is partly a question for the supervisor.

---

**T9 - Ordinary: first ever meeting**

```
first meeting with supervisor, 30 min, never done this before

I have three topic ideas:
1. VR for museum accessibility
2. prompt engineering workflows for small companies
3. something with ROS2 and robot navigation

no idea how to run this meeting or what she expects from me. do I need to
have picked one already
```

*Tests:* the agenda for an exploratory meeting, plus a procedural question
about expectations. "Do I need to have picked one" is the grounding boundary
again.

---

**T10 - Ordinary: dense but well-organized note**

```
30 min, thursday

status: data collection complete (n=47), analysis 80% done, ch4 drafted

agenda I'd like:
1. results - two findings contradict my hypothesis, want her read on
   whether that's a problem or the interesting part
2. ch5 structure - discuss by theme or by RQ?
3. timeline to submission
4. whether she wants to see ch4 before or after I revise it

should be enough for 30 min I think
```

*Tests:* the baseline case where the student has already done the work. Does
the toolkit add anything, or just reformat? If it cannot improve on T10 that
is an honest finding and belongs in the report.

---

# Notes on using this corpus

- **Three runs per case**, per the evaluation design. Record each run
  separately in the prompt log; a constraint respected twice and broken once
  has not been respected.
- **Do not tune on T1-T10.** Tune on the three scenarios in Part A, then test
  on these. If you start fixing prompts to pass specific test notes, the test
  stops measuring anything.
- **T3, T5 and T8 are the ones to watch** for over-production: the failure is
  generating more than the note supports.
- **For Exercise 3 (RAG):** T1, T2, T9 and the procedural parts of Scenarios 2
  and 3 are your "three real questions". The question your documents cannot
  answer is T2 - no document can tell a student whether their RQ is good
  enough, because that judgement is the supervisor's.
