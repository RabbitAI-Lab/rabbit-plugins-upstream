## Description:

Lists Huawei Cloud Virtual Private Cloud (VPC) instances in a tenant region through KooCLI, with an SDK fallback when KooCLI is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud developers and operators use this skill to inspect regional Huawei Cloud VPC inventories, filter by VPC or enterprise project, and save a Markdown inventory for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically installs and runs a telemetry wrapper whose downloaded code and data collection are not included in this release.

Mitigation: Review and pin the wrapper after checking its code and reporting policy; prefer an inventory-only workflow where possible. Disabling reporting does not prevent installation or execution.

Risk: Querying VPC inventory requires cloud credentials.

Mitigation: Use credentials limited to the VPC listing permission (vpc:vpcs:list).

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-vpc-list)
- [KooCLI Installation & Credential Guide](references/cli-installation-guide.md)
- [Least-Privilege IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud KooCLI Official Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Files]

**Output Format:** [Terminal table, JSON array, VPC name list, or local Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only regional inventory with VPC and enterprise project filters, automatic paging, and region selection.]

## Skill Version(s):

1.0.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
