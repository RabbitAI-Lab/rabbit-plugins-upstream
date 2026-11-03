## Description:

Queries Huawei Cloud Elastic Cloud Server (ECS) instances and their status across regions using AK/SK or token authentication, with table or JSON results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and developers use this skill to list ECS instances, inspect a server, and check its status in configured regions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud credentials in the configuration file could expose ECS access if disclosed.

Mitigation: Use a dedicated identity with ECS ReadOnlyAccess, restrict access to the credential file, and keep it out of version control.

Risk: The optional CLI installation path runs a downloaded installer.

Mitigation: Verify the download using Huawei Cloud's official installation guidance before running it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-ecs-query)
- [ECS API reference](references/api-reference.md)
- [Huawei Cloud ECS API documentation](https://support.huaweicloud.com/api-ecs/)
- [IAM policies](references/iam-policies.md)
- [CLI installation guide](references/cli-installation-guide.md)
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/usermanual-hcli/hcli_01_001.html)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration guidance]

**Output Format:** [Markdown tables or JSON query results, with shell commands and configuration guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the configured Huawei Cloud account, permissions, region, and API response.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
