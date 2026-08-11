## Description: <br>
Huawei Cloud SWR (Software Repository for Container) image lifecycle management skill using hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to manage Huawei Cloud SWR container image namespaces, repositories, tags, login credentials, and quotas through hcloud CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reusable Docker login secrets could be exposed in chat, logs, or stored output. <br>
Mitigation: Do not print, paste, decode, or store SWR auth tokens or long-term secrets in chat; have users run credential commands locally and store secrets in a protected secret manager or CI/CD credential store. <br>
Risk: Create, update, and delete operations can modify or permanently remove SWR namespaces, repositories, and tags. <br>
Mitigation: Use least-privilege Huawei Cloud IAM permissions and require explicit user confirmation after showing the exact hcloud command and target resource. <br>
Risk: Changing a repository to public can expose container images to unintended users. <br>
Mitigation: Display a security warning before setting repository visibility to public and proceed only after explicit confirmation. <br>


## Reference(s): <br>
- [SWR API Reference Guide](references/swr-api-guide.md) <br>
- [Parameter Reference](references/parameter-reference.md) <br>
- [Output Format Reference](references/output-format.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Common Pitfalls](references/common-pitfalls.md) <br>
- [Task: Namespace Management](references/task-namespace-management.md) <br>
- [Task: Repository Management](references/task-repository-management.md) <br>
- [Task: Tag Management](references/task-tag-management.md) <br>
- [Task: Auth Management](references/task-auth-management.md) <br>
- [Task: Quota Management](references/task-quota-management.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Huawei Cloud SWR API documentation](https://support.huaweicloud.com/api-swr2/swr_03_0701.html) <br>
- [Huawei Cloud KooCLI updates](https://support.huaweicloud.com/wtsnew-hcli/index.html) <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-swr-image-management) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts for explicit confirmation before create, update, and delete operations; avoids decoding or exposing SWR auth secrets.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
