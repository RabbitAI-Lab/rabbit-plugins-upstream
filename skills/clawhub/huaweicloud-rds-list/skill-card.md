## Description:

Queries Huawei Cloud RDS instances in a specified region and returns a concise inventory with instance name, ID, status, engine type, and specification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and database administrators use this skill to inventory Huawei Cloud RDS resources, support operations checks, troubleshoot incidents, and prepare automation that needs an instance list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Huawei Cloud AK/SK credentials in a local config.json file.

Mitigation: Use a least-privilege credential, keep config.json local and unshared, and rotate the key regularly.

Risk: If project_id is omitted, the skill also calls IAM project listing to resolve the selected region.

Mitigation: Provide project_id explicitly when possible; otherwise grant only iam:projects:listProjects in addition to rds:instances:list.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/huaweicloud-rds-list)
- [IAM permission guidance](iam-policies.md)
- [Huawei Cloud RDS ListInstances endpoint](https://rds.{region}.myhuaweicloud.com/v3/{project_id}/instances)
- [Huawei Cloud IAM projects endpoint](https://iam.myhuaweicloud.com/v3/projects)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions and plain-text command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs one region at a time and lists name, id, status, engine, and spec fields.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
