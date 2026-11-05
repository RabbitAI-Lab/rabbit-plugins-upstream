## Description:

Manage Huawei Cloud ECS instances by querying details and guiding creation, power-state changes, renaming, operating system changes, resizing, and deletion, with preflight checks and confirmation for mutations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to inspect Huawei Cloud ECS instances and carry out requested lifecycle operations. It checks the CLI environment first and requires explicit confirmation before changes that can affect cloud resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic quality reporting can expose sensitive server data or cloud credentials when unsafe transport settings are used.

Mitigation: Keep SKILL_QUALITY_DISABLE=1 unless reporting is explicitly approved. Use approved HTTPS destinations, narrowly scoped authentication, and allowlisted metrics; do not send raw inputs, results, or exceptions.

Risk: Deleting instances, releasing attached resources, reinstalling or changing an operating system, and resizing can cause data loss, charges, or service interruption.

Mitigation: Review the exact target and parameters, preserve needed data, and obtain explicit user confirmation before applying a mutation. Run the resize dry-run check first.

Risk: Installing the KooCLI binary from a download can introduce an untrusted executable if its integrity is not checked.

Mitigation: Verify the download SHA256 against Huawei Cloud's published checksum before installing, and review the exact server targets before mutations.

## Reference(s):

- [Huawei Cloud ECS Lifecycle skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-ecs-lifecycle)
- [KooCLI installation and authentication guide](artifact/references/cli-installation-guide.md)
- [ECS IAM policies](artifact/references/iam-policies.md)
- [Lifecycle change operations](artifact/references/lifecycle-change-operations.md)
- [Operation verification method](artifact/references/verification-method.md)
- [Official Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with ECS operation summaries and KooCLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests explicit confirmation before mutating operations.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
