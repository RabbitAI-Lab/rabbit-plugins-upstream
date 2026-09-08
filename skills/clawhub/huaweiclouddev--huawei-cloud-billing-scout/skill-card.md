## Description:

Helps agents answer Huawei Cloud BSS billing questions about balance, spend, charge attribution, reconciliation, coupons, stored-value cards, and enterprise or partner billing using read-only hcloud evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, FinOps practitioners, and cloud operators use this skill to investigate Huawei Cloud billing, spend attribution, reconciliation gaps, discounts, stored-value cards, and enterprise or partner account billing. The skill is intended for read-only evidence gathering and concise billing briefings, not payments, renewals, refunds, identity review, or non-billing account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation guide recommends latest remote installers, including optional sudo and non-interactive execution.

Mitigation: Prefer an already trusted hcloud installation or verify installer provenance, version, and checksum or signature before execution; avoid non-interactive -y and sudo bash unless the impact is understood.

Risk: Billing queries can expose sensitive spend data, account context, identifiers, and current hcloud profile details.

Mitigation: Use a read-only Huawei Cloud IAM profile and redact credentials, full identifiers, raw output, profile names, and region details from responses.

Risk: Partial billing periods, pagination, sampling, or low-amount results can lead to misleading whole-account conclusions.

Mitigation: State scope, billing period, money basis, and evidence gaps explicitly; do not extrapolate beyond the queried evidence.

## Reference(s):

- [Huawei Cloud Billing Scout on ClawHub](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-billing-scout)
- [Semantic Catalog](references/semantic/catalog.yml)
- [Billing Ontology](references/semantic/billing-ontology.yml)
- [Related Commands](references/related-commands.md)
- [IAM Minimum Permissions](references/iam-policies.md)
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md)
- [Huawei Cloud KooCLI Release Notes](https://support.huaweicloud.com/wtsnew-hcli/index.html)
- [Huawei Cloud IAM Permission Best Practices](https://support.huaweicloud.com/bestpractice-iam/iam_0426.html)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/overview)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise Markdown or plain-text briefing with optional inline hcloud command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses read-only Huawei Cloud BSS evidence; avoids raw command output, credentials, complete business identifiers, profile names, and regions.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
