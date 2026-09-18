## Description:

教培课消与预收学费核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations staff at training or tutoring organizations use this skill during monthly closing, reconciliation, or inventory checks to verify training-hour consumption and prepaid-tuition tables. The skill runs local deterministic checks, reports line-level findings with source evidence, and withholds conclusions when required table data is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation and normal output steer users toward an unpinned package install and paid-skill purchase workflow.

Mitigation: Treat paid-upgrade instructions separately; verify the package, source, version, and payment flow before running purchase commands, preferably in an isolated environment.

Risk: The free checker omits some checks that are described as available only in the paid version.

Mitigation: Review the executed and withheld check lists in the output before relying on results, and do not treat omitted checks as completed.

Risk: The skill performs table reconciliation only and does not make contract, accounting, tax, or refund-policy judgments.

Mitigation: Use the findings as table-level evidence and route accounting, contract, tax, or refund-policy decisions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/training-hour-consumption-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade purchase information](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay storefront](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON with executed checks, omitted checks, table-scope summary, and line-level findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; results depend on user-provided table text or JSON input.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
