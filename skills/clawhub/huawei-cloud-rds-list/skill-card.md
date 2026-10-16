## Description:

Lists Huawei Cloud RDS instances in a selected region for read-only inventory, with table, JSON, and name-only output options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect regional Huawei Cloud RDS inventories and find instance IDs for follow-up tasks without changing instances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Listing RDS instances requires access to a Huawei Cloud credential profile or Huawei-prefixed AK/SK environment variables.

Mitigation: Use least-privilege read-only IAM permissions such as rds:instance:list or RDS ReadOnlyAccess, and keep credentials out of chat.

Risk: Setting up KooCLI or the SDK may involve running installation commands.

Mitigation: Review installation commands before running them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-rds-list)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Least-privilege IAM policy](references/iam-policies.md)
- [KooCLI installation and credential guide](references/cli-installation-guide.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text table or instance-name list; JSON array with --json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Region-scoped results; optional instance filters and automatic paging.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
