## Description:

Lists and filters Huawei Cloud RDS instances through the read-only ListInstances API, using KooCLI or an SDK fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use it to inspect RDS inventory in a selected Huawei Cloud region, filter instances, and retrieve instance IDs for related workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Environment settings can bypass the read-only safeguards.

Mitigation: Review and restrict executable overrides, use a trusted hcloud installation, and limit credentials to rds:instance:list.

Risk: The skill's instructions misstate how credentials are read.

Mitigation: Obtain KooCLI through Huawei's official installation instructions, verify its checksum, and configure dedicated credentials outside chat.

Risk: Inventory output contains private infrastructure information.

Mitigation: Treat results as private and restrict where they are stored or shared.

## Reference(s):

- [KooCLI Installation & Credential Guide](references/cli-installation-guide.md)
- [Least-Privilege IAM Policy](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [ClawHub Skill Page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-rds-list)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Full-field table, JSON array, or instance-name list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are scoped to a region and may be filtered by status, name, database engine, or instance ID.]

## Skill Version(s):

1.0.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
