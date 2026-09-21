## Description:

Read-only Huawei Cloud BSS billing analysis for balance, spend, attribution, reconciliation, coupons, stored-value cards, and enterprise or partner billing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud-finance operators use this skill to inspect Huawei Cloud BSS billing evidence, explain spend, reconcile figures, and identify missing read-only evidence without changing the account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: KooCLI installation or credential setup can expose account credentials or install unverified software if handled casually.

Mitigation: Install KooCLI only from Huawei Cloud's official source, prefer a pinned or verified download when available, use an existing local profile or temporary environment variables, and never paste AK/SK secrets into chat.

Risk: Broad account credentials or write-capable IAM permissions could allow billing, resource, or identity changes outside the skill's intended scope.

Mitigation: Grant only read-only BSS permissions to an IAM user and route payment, renewal, refund, deletion, identity, and other write requests away from this skill.

Risk: Partial billing evidence can lead to overconfident spend or reconciliation conclusions.

Mitigation: Require scope, billing period, and money basis before querying; report evidence gaps instead of extrapolating from partial pages, samples, or missing permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/huawei-cloud-billing-scout)
- [Source homepage](https://github.com/concept-git/cloud-concept-skills/tree/main/skills/en/huawei-cloud-billing-scout)
- [KooCLI installation guide](references/cli-installation.md)
- [IAM minimum permissions](references/iam-policies.md)
- [Related BSS command templates](references/related-commands.md)
- [Billing ontology](references/semantic/billing-ontology.yml)
- [Billing semantic catalog](references/semantic/catalog.yml)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Concise Markdown briefing with guarded read-only command guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Avoids raw command output, full identifiers, credentials, profile names, and regions in user-facing responses.]

## Skill Version(s):

2.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
