## Description:

课时核销表逐项核对（逐行算术、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations staff use this skill during monthly reconciliation or closing to check lesson-hour cancellation tables for arithmetic errors, total-row mismatches, duplicates, and blank or placeholder values. It is intended for local table checking and does not provide legal, tax, refund-policy, attendance, or pricing advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes an upgrade prompt that asks an agent to run an unpinned online installer and proceed through a purchase flow, which can execute remote code or install additional skills outside this review.

Mitigation: Use only the free local checker unless the payment tooling, exact package version, source, and purchase terms have been separately verified; require the user to confirm any wallet authorization or payment.

Risk: The free checker omits several financial checks, including overuse, zero-price-with-usage, amount-cap, and inconsistent unit-price checks.

Mitigation: Treat a clean result as limited to the executed checks and review the withheld and out-of-scope checks before relying on the table for refund, pricing, legal, tax, or attendance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/lesson-hour-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Console text or JSON containing findings, line references, summary totals, executed checks, and checks not run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local Node.js inputs; insufficient input returns missing material guidance instead of a conclusion.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
