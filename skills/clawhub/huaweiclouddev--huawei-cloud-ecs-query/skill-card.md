## Description:

Queries Huawei Cloud ECS instance lists, instance details, and instance status using read-only operations with AK/SK or token authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators, developers, and support engineers use this skill to inspect Huawei Cloud ECS fleets, retrieve single-server details, check runtime status, and guide read-only troubleshooting without creating, deleting, or modifying ECS resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Huawei Cloud credentials such as AK/SK values, tokens, usernames, passwords, project IDs, and domain IDs.

Mitigation: Store credentials only in the documented local configuration file, protect that file, and avoid committing it to version control.

Risk: Overly broad cloud permissions could expose more ECS information than needed for read-only troubleshooting.

Mitigation: Use a least-privilege IAM user with ECS ReadOnlyAccess for normal operation.

Risk: The optional hcloud/KooCLI installation path uses a remote installer script.

Mitigation: Review the installer before running it, and prefer the Python read-only commands when the CLI is not already trusted in the environment.

Risk: Incorrect region, project, or endpoint settings can cause failed queries or misleading empty results.

Mitigation: Validate the configured region, project ID, network access, and ECS endpoint before relying on query results.

## Reference(s):

- [Huawei Cloud ECS Query skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ecs-query)
- [API Reference](artifact/references/api-reference.md)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Verification Method](artifact/references/verification-method.md)
- [Huawei Cloud ECS API documentation](https://support.huaweicloud.com/api-ecs/)
- [Huawei Cloud API signing guide](https://support.huaweicloud.com/devg-apisign/api-sign-provide01.html)
- [Huawei Cloud access key guide](https://support.huaweicloud.com/usermanual-iam/iam_02_0003.html)
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/usermanual-hcli/hcli_01_001.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands plus table or JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud ECS queries; output can be filtered by region, status, name, flavor, limit, and offset.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
