## Description:

Queries Huawei Cloud ECS instance lists, instance details, and server status through read-only API calls with AK/SK or token authentication and table or JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators, DevOps engineers, and support teams use this skill to inspect Huawei Cloud ECS inventories, instance details, and lifecycle status. The documented scope is read-only and excludes create, delete, power, and resize operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads Huawei Cloud credentials from a local configuration file.

Mitigation: Use least-privilege ECS ReadOnlyAccess credentials, store the config outside source control, and protect ~/.huawei-ecs/config.yaml with appropriate file permissions.

Risk: Query results can expose sensitive infrastructure metadata such as instance IDs, IP addresses, tags, tenant or project IDs, and descriptions.

Mitigation: Review and redact ECS outputs before sharing logs, tickets, chat transcripts, or generated reports outside the authorized operations context.

Risk: Incorrect region or project settings can produce incomplete or misleading inventory results.

Mitigation: Confirm the configured region and project_id before relying on results, and use the verification method reference for environment checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-ecs-query)
- [API reference](references/api-reference.md)
- [CLI installation guide](references/cli-installation-guide.md)
- [IAM policies](references/iam-policies.md)
- [Troubleshooting](references/troubleshooting.md)
- [Verification method](references/verification-method.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Huawei Cloud ECS API reference](https://support.huaweicloud.com/api-ecs/)
- [Huawei Cloud API signing guide](https://support.huaweicloud.com/devg-apisign/api-sign-provide01.html)
- [Huawei Cloud access key guide](https://support.huaweicloud.com/usermanual-iam/iam_02_0003.html)
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/usermanual-hcli/hcli_01_001.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell and YAML examples; runtime command output is table text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ECS instance IDs, IP addresses, tags, project or tenant identifiers, and server descriptions.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
