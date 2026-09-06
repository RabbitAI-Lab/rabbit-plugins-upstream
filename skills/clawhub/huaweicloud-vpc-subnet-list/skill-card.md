## Description:

Lists subnets for a specified Huawei Cloud VPC and region, returning a concise inventory of subnet names and IDs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to inventory subnets inside a Huawei Cloud VPC before audits, operations, or automation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud AK/SK credentials are required in a local config.json file.

Mitigation: Use a dedicated read-only AK/SK, keep config.json local, avoid committing credentials, and rotate credentials periodically.

Risk: Leaving project_id empty requires an extra IAM project-list lookup.

Mitigation: Provide project_id when possible to avoid the extra IAM permission and limit access to vpc:subnets:get.

Risk: The skill makes live Huawei Cloud API calls and can fail because of authentication, permission, region, or network errors.

Mitigation: Review command output and errors before using results in downstream automation.

## Reference(s):

- [IAM permissions for Huawei Cloud subnet listing](artifact/iam-policies.md)
- [ClawHub release page](https://clawhub.ai/yangaiwu/skills/huaweicloud-vpc-subnet-list)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Plain text subnet name and ID list, with Markdown setup and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local Huawei Cloud AK/SK credentials and queries one VPC in one region per run.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
