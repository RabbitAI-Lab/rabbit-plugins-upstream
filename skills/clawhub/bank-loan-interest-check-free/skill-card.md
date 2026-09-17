## Description:

银行贷款利息与还款计划核对表逐项核对，覆盖逐行复算、合计勾稽、重复与空缺检测，并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury users can use this skill during monthly close, reconciliation, or inventory checks to review bank loan interest and repayment schedule tables. It helps check arithmetic, total-row consistency, duplicate rows, blanks, placeholders, and negative values within the free edition's stated scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags an external paid installation and purchase workflow outside the audited package.

Mitigation: Treat upgrade prompts as optional, review payment instructions independently, and require explicit user confirmation before installing or purchasing the paid edition.

Risk: The free edition omits several checks that are listed as paid-edition coverage.

Mitigation: Use the results only for the executed free checks and do not treat omitted checks as cleared.

Risk: Insufficient or malformed input can prevent the checker from reaching a conclusion.

Mitigation: Provide the repayment schedule with required headers and review any missing-material guidance before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bank-loan-interest-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional paid edition public page](https://skillpay.alipay.com/public/tokendidi)
- [Optional paid edition purchase guide](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON with cited findings and source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on Node.js according to artifact evidence; insufficient input returns missing-material guidance instead of a conclusion.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
