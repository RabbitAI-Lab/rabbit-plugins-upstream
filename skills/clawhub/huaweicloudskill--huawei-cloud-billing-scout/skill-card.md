## Description:

Helps Huawei Cloud users investigate BSS balances, spend, charge attribution, reconciliation, and billing entitlements with scoped, read-only queries and evidence-based briefings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Huawei Cloud account owners, FinOps teams, and support staff use the skill to check balances and charges, reconcile billing evidence, and identify missing information through read-only queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Container setup examples can give a container unnecessarily broad access to saved cloud credentials.

Mitigation: Prefer an existing CLI with a dedicated billing-only profile. If container access is needed, use a verified image and narrowly scoped credentials, and avoid sharing the full cloud configuration folder.

Risk: Remote installers and container contents have not been verified.

Mitigation: Verify installation downloads before use.

## Reference(s):

- [Huawei Cloud Billing Scout release page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-billing-scout)
- [Billing query routing catalog](artifact/references/semantic/catalog.yml)
- [Billing ontology](artifact/references/semantic/billing-ontology.yml)
- [Copyable BSS command templates](artifact/references/related-commands.md)
- [Huawei Cloud CLI installation guide](artifact/references/cli-installation-guide.md)
- [Huawei Cloud IAM guidance](artifact/references/iam-policies.md)
- [Huawei Cloud CLI documentation](https://support.huaweicloud.com/wtsnew-hcli/index.html)
- [Huawei Cloud IAM best practices](https://support.huaweicloud.com/bestpractice-iam/iam_0426.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [One-page Markdown billing brief with evidence points, gaps, and copyable hcloud command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud BSS billing guidance; avoids exposing credentials and complete business identifiers.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
