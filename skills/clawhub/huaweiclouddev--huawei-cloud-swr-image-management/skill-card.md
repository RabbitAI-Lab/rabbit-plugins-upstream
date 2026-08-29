## Description:

Huawei Cloud SWR image lifecycle management skill using the hcloud CLI for namespaces, repositories, tags, login credentials, and quota checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to manage Huawei Cloud SWR container-image namespaces, repositories, tags, authentication, and quota status through guided hcloud CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve SWR registry login credentials, and security evidence flags that live registry secrets may be handled or relayed in chat.

Mitigation: Prefer temporary tokens, avoid pasting or displaying decoded credentials in chat, keep secrets in local terminals or secret stores, and rotate long-term credentials periodically.

Risk: The skill can delete namespaces, repositories, and tags, which can permanently remove SWR resources and image versions.

Mitigation: Require explicit user confirmation, show the exact target and command before execution, verify targets with read-only commands first, and use least-privilege IAM permissions.

Risk: Installation guidance includes remote hcloud installer commands.

Mitigation: Inspect remote installers before running them and prefer trusted Huawei Cloud distribution channels.

## Reference(s):

- [SWR API Reference Guide](artifact/references/swr-api-guide.md)
- [Huawei Cloud KooCLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Permission Policies](artifact/references/iam-policies.md)
- [Task: Namespace Management](artifact/references/task-namespace-management.md)
- [Task: Repository Management](artifact/references/task-repository-management.md)
- [Task: Tag Management](artifact/references/task-tag-management.md)
- [Task: Auth Management](artifact/references/task-auth-management.md)
- [Task: Quota Management](artifact/references/task-quota-management.md)
- [Parameter Reference](artifact/references/parameter-reference.md)
- [SWR Output Format Reference](artifact/references/output-format.md)
- [Verification Method](artifact/references/verification-method.md)
- [Common Pitfalls and Solutions](artifact/references/common-pitfalls.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Huawei Cloud SWR API documentation](https://support.huaweicloud.com/api-swr2/swr_03_0701.html)
- [Huawei Cloud KooCLI updates](https://support.huaweicloud.com/wtsnew-hcli/index.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with hcloud CLI commands, JSON output interpretation, and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured tables, command snippets, and safety confirmations for write, billing, and credential-related operations.]

## Skill Version(s):

1.0.3 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
