## Description:

Read-only Huawei Cloud BSS billing analysis for balances, spend, attribution, reconciliation, coupons, stored-value cards, and enterprise or partner billing; it refuses pricing quotes, identity reviews, financial changes, and non-billing or other-cloud requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud finance teams and Huawei Cloud account administrators use the skill to inspect read-only BSS billing evidence, explain spend and charges, and identify gaps in reconciliation while keeping account, billing period, and money basis explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured credentials can expose sensitive billing records.

Mitigation: Use a dedicated read-only IAM account and never paste access keys into chat.

Risk: An incorrect account or billing period can produce misleading billing conclusions.

Mitigation: Confirm the intended account and billing period before querying, and keep scope and money basis explicit in the briefing.

Risk: Installing a separately downloaded CLI introduces software integrity risk.

Mitigation: Install it yourself using Huawei's current instructions and verify the download checksum.

## Reference(s):

- [CLI installation and credential guidance](artifact/references/cli-installation.md)
- [IAM least privilege guidance](artifact/references/iam-policies.md)
- [Billing entry point catalog](artifact/references/semantic/catalog.yml)
- [Billing ontology and evidence boundaries](artifact/references/semantic/billing-ontology.yml)
- [Huawei Cloud KooCLI quick installation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Concise Markdown billing briefing with verified facts, scope, billing period, money basis, evidence gaps, and read-only next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps billing facts separate by grain and money basis; does not expose credentials, full business IDs, profiles, regions, raw responses, or commands.]

## Skill Version(s):

2.3.12 (source: frontmatter; release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
