## Description:

酒店夜审与房费收入表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 酒店夜审与房费收入核对、酒店夜审与房费收入表对不上。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Hotel finance, cashier, and night-audit staff use this skill to check hotel night-audit and room-fee revenue tables before monthly close, reconciliation, or inventory work. It recomputes row arithmetic, totals, duplicate rows, blanks, and negative values, and withholds conclusions when required input is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the skill promotes a paid-upgrade flow that can install remote code and initiate a purchase.

Mitigation: Do not let an agent run the npx @latest installer or initiate SkillPay purchases unless the source, package version, payment flow, and permissions are separately verified; require the user to confirm wallet authorization or payment.

Risk: The server security verdict is suspicious.

Mitigation: Install only when the free local checker is intended and the paid-upgrade prompt is acceptable for the deployment context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/hotel-night-audit-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable audit summary or JSON result with cited findings, scope, checks not run, and exit status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided table text or JSON input; material gaps return insufficient-input output rather than a positive or negative audit conclusion.]

## Skill Version(s):

1.0.5 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
