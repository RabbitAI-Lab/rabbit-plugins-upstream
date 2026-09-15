## Description:

逾期利息计算表逐项核对（利息复算、天数勾稽、合计复核、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, legal, and collections staff use this skill before month-end close, demand letters, or litigation preparation to check overdue-interest worksheets for arithmetic, day-count, total-row, duplicate, and blank-field issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation includes paid upgrade instructions that route users into an unreviewed installer and purchase flow.

Mitigation: Use the free local checker only, and separately verify the SkillPay installer, package version, and purchase flow before allowing an agent to run purchase or installation commands.

Risk: The free checker intentionally omits some validations, including legal rate-cap checks, date-anomaly checks, non-positive principal or rate checks, and negative-interest checks.

Mitigation: Review the reported withheld checks and have a qualified reviewer confirm legal and contractual assumptions before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/overdue-interest-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable Markdown-style console output or structured JSON findings with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, line number, message, advice, executed checks, withheld checks, and summary totals.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
