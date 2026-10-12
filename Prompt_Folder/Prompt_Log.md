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

One entry per prompt version. Copy the template, fill it in, never delete an
old entry.

Version naming: `A1` is the zero-shot baseline. `B1`, `B2`... are refinements.
A letter change means a different approach; a number change means a tweak
within the same approach.

Models: record which model produced each run, since the same prompt behaves
differently across them.

---

## Entry template (copy this)

### Version: `__`

- **Date:**
- **Model / settings:**
- **What I was trying to fix:** *(what the previous version got wrong - skip for A1)*
- **What I changed and why:** *(the reasoning, in your own words)*
- **What I expected to happen:**

**Prompt (verbatim):**

```
[paste exactly as run]
```

**Runs:**

| Case | Run | Hard fail? | Which one | Notes |
|---|---|---|---|---|
| | 1 | | | |
| | 2 | | | |
| | 3 | | | |

- **What actually happened:**
- **What got better:**
- **What got worse or broke:** *(there is usually something - record it)*
- **Kept or rejected, and why:**

---

# Versions

---

### Version: `A1` - zero-shot baseline

- **Date:**
- **Model / settings:**
- **What I changed and why:** Nothing - this is the out-of-the-box baseline the
  brief requires. Deliberately plain, no role, no constraints, no format
  instructions, so that later refinements have something honest to improve on.
- **What I expected to happen:** Based on the two failure modes identified in
  the project definition, I expect it to (a) answer procedural questions about
  HSLU as if it knew the answer, and (b) give its own verdict on the quality of
  the student's work rather than helping them ask about it.

**Prompt (verbatim):**

```
[paste exactly as run]
```

**Runs:**

| Case | Run | Hard fail? | Which one | Notes |
|---|---|---|---|---|
| | 1 | | | |
| | 2 | | | |
| | 3 | | | |

- **What actually happened:**
- **Where it failed:**
- **What it did surprisingly well:** *(worth recording - it sets the bar the
  refinements have to beat)*

---

## Cross-model check

The module's learning outcomes include adapting prompts to different models.
Run the final version on a second model and record the difference here rather
than assuming it transfers.

| Model | Cases passed | Hard fails seen | Notes |
|---|---|---|---|
| | | | |
| | | | |

- **What differed:**
- **What that means for the product:**

---

## Rejected approaches

Things tried and abandoned. Worth as much as the successful versions - they
show the search, not just the result.

| Date | What I tried | Why I dropped it |
|---|---|---|
| | | |
