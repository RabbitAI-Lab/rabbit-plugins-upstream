## Description:

分期方案核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Business, procurement, and finance users use this skill to check installment worksheets for nominal fee, repayment, annualized rate, total-row, duplicate, and blank-field issues. It is intended as a local arithmetic audit of supplied worksheet text, not as financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill text points users and agents toward an unpinned online install-and-purchase flow for a paid product.

Mitigation: Use only the bundled local checker for the free worksheet audit unless you separately verify the package source and version and intentionally want to begin a payment-related workflow.

Risk: Worksheet outputs may be mistaken for broader financial advice or complete coverage of every installment-plan issue.

Mitigation: Treat results as arithmetic worksheet checks under the stated IRR and nominal-rate formulas, and review the listed withheld and out-of-scope checks before relying on the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/installment-rate-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON containing worksheet findings, summaries, executed checks, withheld checks, and cited source lines.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; sample and input-file modes; no API key or network required for the bundled checker.]

## Skill Version(s):

1.0.11 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
