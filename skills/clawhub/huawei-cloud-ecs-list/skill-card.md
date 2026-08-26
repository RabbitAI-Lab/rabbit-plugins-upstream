## Description:

Queries Huawei Cloud ECS instance lists and details with read-only hcloud CLI calls, optional filters, and JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory Huawei Cloud ECS instances, inspect server details, and support routine checks, troubleshooting, and resource verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs Huawei Cloud AK/SK credentials and can expose ECS inventory to the agent session.

Mitigation: Use a dedicated least-privilege AK/SK with only ECS read permissions, prefer a clean session with exact credential environment variables, and unset credentials after use.

Risk: Command output may include cloud inventory details that should not be shared broadly.

Mitigation: Avoid shared logs for command output and review results before pasting or publishing them.

Risk: The hcloud installer path should be trusted before installation.

Mitigation: Verify the hcloud CLI installer through a trusted Huawei Cloud distribution path before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/huawei-cloud-ecs-list)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud ECS API reference](https://support.huaweicloud.com/api-ecs/ecs_02_0001.html)
- [IAM permissions policy](artifact/iam-policies.md)
- [hcloud CLI installation guide](artifact/cli-installation-guide.md)
- [Verification method](artifact/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Code, Guidance]

**Output Format:** [JSON command output and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only list, show, and capability-list operations; stdout contains JSON results and stderr contains JSON errors.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
