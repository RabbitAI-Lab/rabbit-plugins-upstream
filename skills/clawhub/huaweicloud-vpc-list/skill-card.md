## Description:

Lists VPCs in a specified Huawei Cloud Region and returns a compact inventory of VPC names and IDs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to inventory Huawei Cloud VPC resources, run operational checks, or gather inputs for automation scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud AK/SK credentials are stored in a local config.json and could be exposed if the file is shared or committed.

Mitigation: Use a dedicated key, keep config.json out of version control, and rotate the key regularly.

Risk: Leaving project_id empty requires IAM project-list access in addition to VPC list access.

Mitigation: Provide project_id when possible and grant only the documented read-only permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/huaweicloud-vpc-list)
- [IAM permissions reference](artifact/iam-policies.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text VPC inventory with Markdown setup and permission guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local Huawei Cloud AK/SK configuration; providing project_id avoids the IAM project-list lookup.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
