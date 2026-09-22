## Description:

Huawei Cloud SWR Image Management helps an agent manage Huawei Cloud Software Repository for Container namespaces, repositories, image tags, Docker login credentials, and quota checks using the hcloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect and manage Huawei Cloud SWR container image resources, including namespaces, repositories, tags, Docker login credentials, and quota usage. It is intended for agent-assisted cloud operations where commands and sensitive changes are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through create, update, delete, visibility-change, and quota-affecting SWR operations that may have billing, availability, or data-loss impact.

Mitigation: Require explicit billing confirmation before any operation and explicit command-level confirmation before every create, update, delete, or private-to-public repository visibility change.

Risk: The skill handles cloud access keys, security tokens, Docker auth values, and generated registry passwords.

Mitigation: Use least-privileged IAM permissions, prefer short-lived tokens when practical, treat decoded Docker credentials as passwords, and do not expose credential values in conversation, logs, code, or shell history.

Risk: The artifact includes one-line remote installer guidance for the hcloud CLI, which can be risky if executed without source verification.

Mitigation: Install only from Huawei Cloud sources after independently verifying the source, and avoid unattended remote installer execution in shared or production environments.

Risk: Using docker login with command-line password flags can expose credentials in process lists or command history on shared systems.

Mitigation: Prefer safer Docker credential handling in shared environments and avoid passing registry passwords directly on the command line where they may be observed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-swr-image-management)
- [SWR API Guide](references/swr-api-guide.md)
- [Huawei Cloud SWR API documentation](https://support.huaweicloud.com/api-swr2/swr_03_0701.html)
- [Huawei Cloud KooCLI release notes](https://support.huaweicloud.com/wtsnew-hcli/index.html)
- [Parameter Reference](references/parameter-reference.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Task: Namespace Management](references/task-namespace-management.md)
- [Task: Repository Management](references/task-repository-management.md)
- [Task: Tag Management](references/task-tag-management.md)
- [Task: Auth Management](references/task-auth-management.md)
- [Task: Quota Management](references/task-quota-management.md)
- [Output Format Reference](references/output-format.md)
- [Verification Method](references/verification-method.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands, tables, and summarized JSON fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation for billing implications and create, update, or delete operations; may summarize hcloud JSON responses for readability.]

## Skill Version(s):

1.0.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
