## Description:

Lists Huawei Cloud MapReduce Service clusters in a selected region using a read-only KooCLI operation, with optional filters and text or JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect regional MRS cluster inventory, filter clusters by state or name, and retrieve cluster identifiers for follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the active Huawei Cloud KooCLI profile to access MRS cluster inventory.

Mitigation: Use a least-privilege profile with mrs:cluster:list or MRS ReadOnlyAccess; configure credentials outside chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-mrs-list)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [IAM policies](references/iam-policies.md)
- [KooCLI installation and credential guide](references/cli-installation-guide.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text table, JSON array, or cluster-name list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Region-scoped; supports cluster-state and cluster-name filters and automatic pagination.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
