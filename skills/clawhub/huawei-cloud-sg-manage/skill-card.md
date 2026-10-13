## Description:

Helps cloud operators query, diagnose, audit, and manage Huawei Cloud VPC security groups and rules using the hcloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inspect Huawei Cloud security groups, diagnose connectivity and risky rules, and preview and confirm security-group changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A remotely downloaded telemetry CLI is installed persistently, and its reporting scope is unclear.

Mitigation: Review the installer and reporting behavior before use; disable reporting with SKILL_QUALITY_REPORT=0 if telemetry is not acceptable.

Risk: Creating, updating, or deleting security groups and rules can alter live connectivity or expose services.

Mitigation: Use least-privilege IAM access, check the region, project, group and rule IDs, review each preview, and confirm changes only after assessing the impact.

## Reference(s):

- [Huawei Cloud VPC security groups documentation](https://support.huaweicloud.com/usermanual-vpc/vpc_SecurityGroup_0001.html)
- [Huawei Cloud VPC API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/VPC/doc)
- [KooCLI documentation](https://support.huaweicloud.com/cli/index.html)
- [Least-privilege IAM policies](references/iam-policies.md)
- [Security-group rule reference](references/sg-rule-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Structured JSON results with readable summaries and command previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only analyses can run automatically; changes require preview and explicit confirmation.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
