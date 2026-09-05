## Description:

查询华为云账号下指定 Region 的弹性云服务器（ECS）实例列表，输出精简的实例名称和 ID 清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to inventory Huawei Cloud ECS instances in a selected Region before audits, maintenance, or automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud AK/SK credentials are required to call ECS and IAM APIs.

Mitigation: Use a dedicated AK/SK with only the documented read-only permissions, keep config.json local, and do not commit or share credential files.

Risk: Leaving project_id blank causes an additional IAM project-list lookup.

Mitigation: Provide project_id in config.json when possible to avoid the extra IAM request and reduce required permissions to ECS list access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yangaiwu/skills/huaweicloud-ecs-list)
- [IAM Permissions Statement](artifact/iam-policies.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration]

**Output Format:** [Plain text instance list and Markdown usage guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists only ECS instance names and IDs for one Huawei Cloud Region per run.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
