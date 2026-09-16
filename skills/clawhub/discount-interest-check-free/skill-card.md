## Description:

票据贴现计算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。触发词包括 贴现利息核对、贴现算错、票据贴现、计息天数。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business and finance users use this skill to locally check bill discount interest worksheets before a discounting transaction. It recalculates stated interest, net proceeds, day counts, totals, duplicate bill numbers, and blank placeholders while citing source line numbers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes paid-upgrade instructions that steer users or agents toward external installation and purchase steps outside the reviewed skill.

Mitigation: Use only the bundled free local checker unless the SkillPay package, merchant, product ID, payment details, and installation source have been independently verified and the user personally approves payment.

Risk: Financial worksheet findings may be mistaken for transaction approval or professional financial or legal advice.

Mitigation: Treat results as calculation checks, review the cited source lines, confirm the day-count basis with the discounting institution, and obtain qualified review before making transaction decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/discount-interest-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON findings with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; materials that are insufficient or missing required table fields return missing-input guidance instead of a conclusion.]

## Skill Version(s):

1.0.14 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
