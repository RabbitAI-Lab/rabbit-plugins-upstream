## Description:

Helps agents list, inspect, create, start, stop, reboot, rename, and delete Huawei Cloud ECS instances and answer basic ECS questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to query and manage Huawei Cloud ECS instances through KooCLI, with a Python SDK fallback. It also provides basic ECS usage guidance.

### Deployment Geography for Use:

Global; operations target the region configured for the Huawei Cloud account.

## Known Risks and Mitigations:

Risk: When credentials are available, quality reporting can send execution details to a remote, configurable service by default.

Mitigation: Set SKILL_QUALITY_DISABLE=1 unless reporting is required; review SKILL_QUALITY_ENDPOINT before using the reporting SDK or self-check.

Risk: ECS changes can incur charges, interrupt workloads, or delete data.

Mitigation: Use least-privilege credentials, review target instances and parameters, and require explicit confirmation before each change.

Risk: Cloud access keys may be exposed in shared terminals or chats.

Mitigation: Use a protected CLI profile or environment and avoid pasting access and secret keys into shared terminals or chats.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-ecs-lifecycle)
- [KooCLI installation and authentication](references/cli-installation-guide.md)
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [ECS IAM permissions](references/iam-policies.md)
- [Operation verification](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mutating operations require explicit user confirmation; results may include job IDs and instance details.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
