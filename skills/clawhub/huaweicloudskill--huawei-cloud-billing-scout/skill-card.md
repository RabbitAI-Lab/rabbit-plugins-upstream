## Description:

Guides agents through read-only Huawei Cloud BSS billing checks for balances, spend, charge attribution, reconciliation, coupons, stored-value cards, and enterprise or partner billing while refusing payment, refund, renewal, deletion, pricing, identity-review, and non-billing requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, FinOps practitioners, and cloud account operators use this skill to collect and explain Huawei Cloud BSS billing evidence from a configured hcloud profile. It supports read-only investigations of balances, monthly spend, charge attribution, reconciliation gaps, discounts, stored-value cards, and enterprise or partner billing scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use the current hcloud profile to gather billing evidence.

Mitigation: Verify the active account and profile before use, and grant only the minimum read-only BSS permissions needed for the billing question.

Risk: Setup references include one-line remote installer and non-interactive installation examples.

Mitigation: Independently verify installer sources and downloaded artifacts before running installation commands, especially examples using unattended flags.

Risk: Some setup references include broader KooCLI or cloud-service examples outside the billing workflow.

Mitigation: Treat off-scope KooCLI, ECS, setup, and maintenance examples as general documentation, not skill-authorized billing actions.

Risk: Billing evidence can contain sensitive account, customer, order, resource, coupon, card, or partner identifiers.

Mitigation: Keep identifiers desensitized in outputs and avoid exposing credentials, full business IDs, profile names, or raw command responses.

## Reference(s):

- [Semantic routing catalog](references/semantic/catalog.yml)
- [Billing ontology](references/semantic/billing-ontology.yml)
- [Command contract appendix](references/related-commands.md)
- [IAM minimum permissions](references/iam-policies.md)
- [Huawei Cloud KooCLI installation guide](references/cli-installation-guide.md)
- [Huawei Cloud KooCLI release notes](https://support.huaweicloud.com/wtsnew-hcli/index.html)
- [Huawei Cloud IAM permission best practices](https://support.huaweicloud.com/bestpractice-iam/iam_0426.html)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/overview)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown briefing with concise prose and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should avoid raw command responses, credentials, full business identifiers, profile names, and regions.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
