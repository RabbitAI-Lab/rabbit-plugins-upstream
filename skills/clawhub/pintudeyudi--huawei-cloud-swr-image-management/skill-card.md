## Description:

Huawei Cloud SWR (Software Repository for Container) image lifecycle management skill using hcloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pintudeyudi](https://clawhub.ai/user/pintudeyudi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to manage Huawei Cloud SWR namespaces, image repositories, image tags, registry login credentials, and quota checks through hcloud CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registry credentials and long-lived SWR secrets can be exposed through command history, logs, or conversation if handled carelessly.

Mitigation: Use read-only IAM unless management actions are required, prefer temporary credentials, store secrets in a secret manager, and use docker login --password-stdin instead of placing passwords on the command line.

Risk: Management workflows can perform high-impact cloud operations, including deleting namespaces, repositories, or image tags.

Mitigation: Run destructive commands only after confirming the target namespace, repository, or tag, and avoid full verification runs against production accounts.

## Reference(s):

- [SWR API Reference Guide](references/swr-api-guide.md)
- [IAM Permission Policies - SWR Image Management Skill](references/iam-policies.md)
- [Verification Method - SWR Image Management Skill](references/verification-method.md)
- [Common Pitfalls & Solutions](references/common-pitfalls.md)
- [Task: Namespace Management](references/task-namespace-management.md)
- [Task: Repository Management](references/task-repository-management.md)
- [Task: Tag Management](references/task-tag-management.md)
- [Task: Auth Management](references/task-auth-management.md)
- [Task: Quota Management](references/task-quota-management.md)
- [Huawei Cloud SWR Documentation](https://support.huaweicloud.com/swr/index.html)
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html)
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include hcloud CLI commands and credential-handling instructions; no executable files are produced.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
