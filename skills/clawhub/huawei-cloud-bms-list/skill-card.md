## Description:

Lists Huawei Cloud Bare Metal Server instances in a selected region, with optional filters and table, JSON, or names-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect, inventory, and reconcile Huawei Cloud BMS instances in a tenant region. It supports filtered server listings and can provide a server ID for follow-on tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Execution and connection settings are less restricted than the skill's read-only safety claims suggest.

Mitigation: Review endpoint validation and execution overrides before installing, and confirm the selected region and listing operation.

Risk: The SDK fallback uses access keys provided through the environment.

Mitigation: Use credentials restricted to BMS listing and keep access keys out of chat and skill inputs.

Risk: An unverified KooCLI download could introduce unwanted code.

Mitigation: Install KooCLI only from verified official Huawei downloads.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-bms-list)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [KooCLI installation and credential guide](references/cli-installation-guide.md)
- [BMS IAM policies](references/iam-policies.md)
- [BMS verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Readable table, JSON array, or compact server-name list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports name, server ID, and status filters; results may be paginated.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
