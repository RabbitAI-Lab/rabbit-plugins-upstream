## Description:

Helps operators query, diagnose, audit, and manage Huawei Cloud security groups and their rules through the hcloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inspect Huawei Cloud security-group rules, diagnose connectivity and exposure, and preview and confirm rule or group changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changing or deleting security-group rules can disrupt live network access or expose services.

Mitigation: Grant only necessary IAM permissions, omit delete permissions unless needed, and require explicit approval after reviewing each change preview.

Risk: A separate quality-reporting wrapper installs persistent local tooling and adds a telemetry reporting path.

Mitigation: Decide whether to accept the wrapper and its telemetry before installation; if not, remove or disable the wrapper path before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-sg-manage)
- [Huawei Cloud security-group documentation](https://support.huaweicloud.com/usermanual-vpc/vpc_SecurityGroup_0001.html)
- [Huawei Cloud VPC API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/VPC/doc)
- [Security-group rule reference](references/sg-rule-reference.md)
- [Least-privilege IAM policies](references/iam-policies.md)
- [CLI installation and authentication](references/cli-installation-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [JSON results with readable summaries and command previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries and analysis can run automatically; changes require a preview and explicit confirmation.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
