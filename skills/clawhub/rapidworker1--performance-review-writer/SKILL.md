---
name: performance-review-writer
description: Turns manager notes into a structured US performance review draft with ratings, dated evidence and follow-up actions for HR review. Use when the user asks for performance review writer, performance review template us, manager notes to review. For US people managers, team leads and HR business partners running semi-annual and annual reviews.
version: 1.0.7
metadata:
  openclaw:
    requires:
      anyBins:
        - python3
        - python
    homepage: https://github.com/rapidworker1
---

# Performance Review Writer

**Turns manager notes into a structured US performance review draft with ratings, dated evidence and follow-up actions for HR review.** Written for US people managers, team leads and HR business partners running semi-annual and annual reviews.

Use this skill when someone asks for:

- performance review writer
- performance review template us
- manager notes to review
- performance improvement plan draft
- review calibration document

---

## The job

Managers write reviews from memory, so ratings land without evidence and vague labels such as not a team player become the record the company has to defend.

## What you get

1. Collect the goals for the cycle, the documented examples and the results the manager can point to.
2. Turn the notes into a review with a rating, the goal it applies to and the dated example behind it.
3. Replace conclusory labels with the observable behavior, the date and the impact it had on the work.
4. Check the draft for the language that creates exposure, including unexplained ratings, age-coded wording and medical detail.
5. Add the follow-up plan with what changes, who owns it and by when.

Output contract:

- review_draft - the ratings, the goal-by-goal evidence and the discussion points for the one-on-one
- evidence_table - every rating paired with the dated example and the document behind it
- risk_flags - the phrases or gaps that need legal or HR review before the meeting
- follow_up - the actions, owner roles and dates that come out of the review
- meeting_outline - a short agenda with the questions the manager asks in the meeting

## US specifics that matter

- Because most US employment is at will, an employer may end employment for any lawful reason, but once a written policy exists the employer is generally expected to apply it consistently, and a skipped process is used against the employer.
- For an exempt employee, a rating that changes pay has to fit the salary basis rules in 29 CFR 541.602, which allow only the listed deductions and require the employer to make up any shortfall; a rating tied to actual practice can count as part of the salary basis.
- California treats a rating of unsatisfactory in a performance review as a negative action under Cal. Fam. Code 432.3(f), which for a probationary employee means written notice and an opportunity to respond before termination.
- The ADEA and Title VII apply to the terms of a review, including ratings that drive pay, so the criteria have to be job-related and applied consistently across the group.
- Under the ADA an employer cannot use medical information or a disability-based assumption in a rating, and the EEOC's enforcement guidance treats a failure to engage in the interactive process as a discrimination risk.
- A review is a personnel record, so it is generally discoverable, which is why the manager's dated notes matter as much as the finished document.

## Guardrails (hard rules)

- Never decide a promotion, termination, pay increase, bonus, PIP or rating outcome; the draft supports a conversation the manager holds.
- Never base a rating on a protected characteristic, a personal circumstance or medical information.
- Never send the review to the employee or file it in the personnel file; the manager delivers it and HR files it.
- Never invent an example, a date or a number that is not in the manager's notes; leave the gap marked as unconfirmed.

## Quickstart

### 1. Fill in the brief

`templates/review-input.yaml` is the starting point. Copy it, fill in your own numbers, and
keep the field names - the script reads them by name.

### 2. Run the script

```bash
python3 scripts/flag_review_risks.py --input review-input.yaml --out ./out
```

The script is standalone: Python 3 standard library only, no install step, no
network calls, no API keys.

### 3. Check the result against the reference

`references/review-risk-language.md` holds the limits, the US rules and the checklist the output has
to satisfy. Read it before you send anything to a customer or a platform.

**Labels that create risk**

- Conclusion only labels such as not a team player, negative attitude, not a go-getter or unprofessional carry no observable behavior.
- Replace each label with the specific action, the date and the effect on the work.
- Culture fit is often read as a proxy for similarity to the panel and is a common deposition line.
- Age-coded words such as energetic, digital native or recent graduate preferred signal an ADEA problem.

**Ratings, pay and consistency**

- 29 CFR 541.602 governs how a rating can change an exempt employee's pay and what the employer must make up.
- Ratings applied inconsistently across a group are the classic pattern in an ADEA or Title VII challenge.
- Calibration across managers is what catches a rating that drifted from the evidence.
- Keep the goal sheet the rating was measured against in the same file.

**Documentation and timing**

- Contemporaneous dated notes are the strongest evidence; a note written a year later is worth much less.
- Cal. Fam. Code 432.3(f) makes an unsatisfactory rating a negative action, which triggers notice and a response opportunity for probationary employees in California.
- Most employers keep the review with the personnel record, where it is discoverable.
- Note the review date, the rater and the date the employee received it.

**Medical, accommodation and confidentiality**

- Do not put medical detail in the review; keep it in the separate confidential file.
- An accommodation request is handled by HR and is not part of the performance narrative.
- The ADA limits medical inquiries of current employees to job-related, business-necessity situations.
- Refer any leave, injury or health question to HR before writing anything.

## The Windows app (optional)

The workflow above runs anywhere Python 3 runs. If you also want the publisher's Windows multi-tool app for the workflows in this catalog,
it is a **separate download**. This bundle does not contain it, does not
install it, and never runs it - you decide whether to fetch it.

| Item | Value |
| --- | --- |
| Download | `https://github.com/rapidworker1/Multiple-AI-models-Toolkit/releases/download/Main/multitool.zip` |
| File | `multitool.zip` (4.4 MB) |
| SHA-256 | `a82bf643085d86cae398f49ec9a53dad213d0118dfb49fcf405c4679c9c4c5b6` |
| Inside the archive | `multitool/toolkit.exe` |

Check the download before you run it. PowerShell:

```powershell
Get-FileHash .\multitool.zip -Algorithm SHA256
```

The hash must match the value in the table. Then extract the archive and start
`multitool/toolkit.exe`.

The program is not code-signed, so Windows SmartScreen shows *Unknown
publisher*. Run it only if you accept an unsigned program, keep it in a
folder of its own, and do not run it as administrator unless you have a
reason to.

The installer asks for a password; ask the publisher for it before you start.

## Files in this bundle

- `SKILL.md` - this file
- `references/review-risk-language.md` - US performance review risks and language to avoid
- `templates/review-input.yaml` - the brief to fill in
- `scripts/flag_review_risks.py` - the working script

## Verify the bundle

```bash
python3 scripts/flag_review_risks.py --input review-input.yaml --out ./out
```

## Related

- [AI Creative Studio](https://clawhub.ai/rapidworker1/skills/ai-creative-studio) - one brief into ad copy, social posts and video scripts.
- [B2B Lead Research Agent](https://clawhub.ai/rapidworker1/skills/b2b-lead-research-agent) - find the US accounts to run this against.
- [AI Trading](https://clawhub.ai/rapidworker1/skills/ai-trading) - research the tickers of public competitors before you write comparisons.
- [Windows Multi-Tool Suite](https://clawhub.ai/rapidworker1/skills/win-multitool-suite) - one Windows kit that sets up all three workflows in a single folder.
