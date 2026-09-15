## Description:

Read-only Huawei Cloud BSS billing analysis for balances, spend, attribution, reconciliation, coupons, stored-value cards, and enterprise or partner billing when Huawei Cloud or BSS billing is explicit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud finance, operations, and engineering users use this skill to inspect Huawei Cloud BSS billing evidence, explain spend and charge attribution, reconcile billing figures, and identify missing evidence without modifying accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Command templates and CLI installation guidance may lead to unsafe local execution if reviewed casually.

Mitigation: Review command templates and downloaded CLI artifacts before use; the agent should only run allowed read-only checks or BSS queries.

Risk: Huawei Cloud AK/SK credentials, account IDs, resource IDs, coupon IDs, or region text could be exposed or interpolated into shell commands.

Mitigation: Use least-privilege read-only BSS IAM credentials, avoid pasting AK/SK into chat, mask sensitive identifiers, and validate and safely quote user-supplied values.

Risk: Partial billing windows, pagination, missing permissions, or unsupported account relationships can produce incomplete billing conclusions.

Mitigation: State scope, billing period, money basis, pagination, and permission gaps explicitly; do not present partial or zero results as proof of the whole account state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/huawei-cloud-billing-scout)
- [Skill homepage](https://github.com/concept-git/cloud-concept-skills/tree/main/skills/en/huawei-cloud-billing-scout)
- [KooCLI installation guide](references/cli-installation.md)
- [IAM minimum permissions](references/iam-policies.md)
- [Command contract appendix](references/related-commands.md)
- [Billing semantic catalog](references/semantic/catalog.yml)
- [Billing ontology](references/semantic/billing-ontology.yml)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise Markdown briefing with read-only command guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Huawei Cloud BSS evidence boundaries and avoids exposing raw responses, credentials, full IDs, profiles, or regions.]

## Skill Version(s):

2.3.10 (source: server release evidence; artifact frontmatter says 2.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
