# Thesis Meeting Prep Coach - User Guide and Boundaries

*Educational prototype for the HSLU module PROMPT (HS26). Not official HSLU
communication, policy or advice.*

---

## What it does

You have a meeting with your thesis supervisor coming up and a messy list of
things on your mind. Paste that list in. You get back three things:

1. **An agenda** that fits the meeting length you gave, with a clear list of
   what will not fit.
2. **Your questions, most important first.** You may only get through the
   first two, so those are the ones that matter most.
3. **A follow-up email template** to send after the meeting. It has blanks
   like `[what we agreed on X]`, because the meeting has not happened yet.
   You fill them in afterwards.

You do not need any experience with AI tools to use it.

---

## How to use it

1. **Write your note the way you normally would.** Bullet points, half
   sentences and typos are all fine. It does not need to be tidy.
2. **Include three things if you can:**
   - how long the meeting is ("20 min", "30 min slot")
   - what you want to discuss or decide
   - where you are in the thesis (which chapters exist, what is stuck)
3. **Run it** (see "Running it" below).
4. **Read the BEFORE THE MEETING list first.** These are gaps in your own note
   that only you can fill: for example, the meeting length is missing, or you
   mention a chapter without saying where it stands.
5. **Edit before you use anything.** The output is a starting point. Cross out
   what is wrong and reorder what you disagree with. You know your situation;
   the tool only knows your note.
6. **After the meeting,** fill the blanks in the email with what was actually
   said, and only then send it.

### If your note is very short

If your note does not name anything to discuss ("meeting tomorrow help"), the
tool will not make up an agenda. It asks you for more instead. This is
deliberate: a generic agenda would look helpful and tell you nothing about
*your* meeting.

---

## Boundaries: what this tool will not do

These limits are the point of the design, not missing features.

**1 · It will not tell you HSLU deadlines, rules or procedures from memory.**
A confident wrong deadline is the worst thing this tool could produce, because
you might act on it. Questions like "when is the submission deadline?" or "do
I need re-approval?" go on your agenda as questions for your supervisor, with
a note that the official regulations are the authority. Where the grounded
version answers from the *Studienreglement*, it cites the article. Check it
against the source before you rely on it.

**2 · It will not judge your work.** "Is my research question good enough?"
and "Will I make it?" are your supervisor's judgement. The tool helps you ask
these questions clearly; it never answers them. Even if your note says "just
tell me yes or no", it will not.

**3 · It will not add concerns you did not raise, or quietly drop ones you
did.** Every item it works from carries a quote of your own words, so you can
check that each one is really yours.

**4 · It will not coach you on personal difficulties.** If your note mentions
that you are struggling, the tool will not script what to say about it. It
keeps that off the agenda and out of the email, because an email is a written
record. It reminds you that you decide whether and how much to share, and
that HSLU student support services can help.

**5 · It does not replace your supervisor.** It prepares you for the
conversation. The conversation is still between you and them.

---

## Where to get real answers

| You need | Go to |
|---|---|
| Deadlines, submission format, registration | The official regulations and the mycampus WIPRO/BAA page |
| Whether your work is on track | Your supervisor |
| Personal or wellbeing support | HSLU student support services (Beratung) |

---

## Privacy

Do not paste your supervisor's full name, your student ID or health details
into the tool. The prototype sends your note to a language model through an
external API. All notes in this project's repository are invented.

---

## Running it (prototype)

1. Open `Prototype/thesis_meeting_prep_prototype.ipynb` in Google Colab.
2. Add the course OpenRouter key to Colab Secrets as `OPENROUTER_API_KEY`.
   Never paste a key into a cell.
3. Run the setup cells, then section 7 (B2):
   `run_workflow_b2(your_note, "MY", 1)`.

Outputs from the three example scenarios are on the project page:
<https://adhurimthaqi.github.io/Prompt-Engineering-Project/>
