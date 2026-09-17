## Description:

季度预缴所得税计算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 预缴企业所得税核对、季度预缴所得税计算表对不上。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill before quarterly corporate income tax prepayment filing to check table arithmetic, totals, duplicate periods, blanks, and negative base or rate values. The free version only covers the checks it lists and does not determine tax-rate legality, incentive eligibility, tax adjustments, loss carryforward, or e-tax filing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes an external paid-upgrade flow that asks an agent to install and follow mutable third-party onboarding code.

Mitigation: Do not let an agent run the payment installer or follow newly installed onboarding instructions unless a human independently verifies the package, source, version, and payment flow and approves each step.

Risk: The free checker may be mistaken for complete tax validation even though several checks and tax-law determinations are explicitly outside scope.

Mitigation: Treat results as limited to the listed local arithmetic and consistency checks; review withheld checks and tax-law questions with authoritative tax guidance or a qualified reviewer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cit-prepay-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs a local Node.js checker against provided table text or JSON input; reports executed and withheld checks, insufficient input, findings, summary counts, and scope notes.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
