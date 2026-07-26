## Description: <br>
Huawei Cloud SWR (Software Repository for Container) image lifecycle management skill using hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud platform engineers use this skill to manage Huawei Cloud SWR namespaces, image repositories, tags, login credentials, and quotas through hcloud CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Registry credentials, AK/SK values, security tokens, and decoded Docker login passwords may be exposed in chat, logs, shell history, or committed files. <br>
Mitigation: Use least-privilege IAM identities, prefer temporary credentials, avoid printing secrets, store credentials in secret managers or environment variables, and rotate long-term credentials regularly. <br>
Risk: Namespace, repository, and tag deletion operations can permanently remove SWR resources or image versions. <br>
Mitigation: Confirm namespace, repository, and tag targets with the user before destructive commands, inspect resource details first, and run post-deletion verification only after explicit approval. <br>


## Reference(s): <br>
- [Common Pitfalls](references/common-pitfalls.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [SWR API Reference Guide](references/swr-api-guide.md) <br>
- [Task: Auth Management](references/task-auth-management.md) <br>
- [Task: Namespace Management](references/task-namespace-management.md) <br>
- [Task: Quota Management](references/task-quota-management.md) <br>
- [Task: Repository Management](references/task-repository-management.md) <br>
- [Task: Tag Management](references/task-tag-management.md) <br>
- [Verification Method](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hcloud CLI commands, IAM policy guidance, Docker login steps, and verification checklists.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
