## Description:

中标通知书与合同草案逐项核对，检查金额、文本要素、必备要素、重复项、空白和占位符，并为结论提供原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, procurement, and contract operations users can run this local checker before contract signing or reconciliation to compare a tabular award notice against a draft contract. It reports only evidence-backed consistency findings and lists missing input when materials are insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes paid-upgrade instructions that ask an AI assistant to install external payment tooling and start a purchase flow.

Mitigation: Treat the paid-upgrade path as optional and user-confirmed; manually verify the package, version, merchant, product identifier, and payment links before running any payment-related command.

Risk: The free checker does not perform the withheld paid checks, full arithmetic cross-footing, legal validity review, or document parsing from original PDF or DOCX files.

Mitigation: Use the free checker only for the listed local tabular comparisons, and require human review or a separate vetted process for legal conclusions, complete contract review, and unavailable checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/award-contract-consistency-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay storefront](https://skillpay.alipay.com/public/tokendidi)
- [Purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [analysis, json, markdown, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON containing executed checks, withheld checks, findings, summary, scope, and disclaimers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library according to the artifact; no API key or network is required for the free checker.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
