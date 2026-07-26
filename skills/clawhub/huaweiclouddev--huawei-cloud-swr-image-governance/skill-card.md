## Description: <br>
Huawei Cloud SWR image governance skill that helps agents use the hcloud CLI to manage permissions, retention rules, shared domains, image sharing, and agency delegation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud platform operators use this skill to audit and change Huawei Cloud SWR namespace and repository permissions, image retention rules, shared download domains, image sharing settings, and agency delegation through hcloud CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose broad cloud-changing operations, including create, update, delete, permission, retention, shared domain, and agency delegation commands. <br>
Mitigation: Prefer the read-only IAM policy by default, require explicit user confirmation before create/update/delete commands, and use least-privilege credentials for the requested operation. <br>
Risk: Real Huawei Cloud credentials could authorize destructive or privilege-affecting SWR changes. <br>
Mitigation: Use temporary credentials where possible, avoid exposing credential values in commands or conversation, and test workflows in non-production before applying them to production resources. <br>
Risk: Agency delegation and shared download domains can expand access beyond a single repository workflow. <br>
Mitigation: Review agency delegation and shared domain changes with a cloud administrator before execution. <br>


## Reference(s): <br>
- [SWR Governance API Reference Guide](references/swr-governance-api-guide.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Output Format](references/output-format.md) <br>
- [Common Pitfalls](references/common-pitfalls.md) <br>
- [Task: Namespace Permissions](references/task-namespace-permissions.md) <br>
- [Task: Repository Permissions](references/task-repository-permissions.md) <br>
- [Task: Retention Management](references/task-retention-management.md) <br>
- [Task: Shared Domains](references/task-shared-domains.md) <br>
- [Task: Image Sharing](references/task-image-sharing.md) <br>
- [Huawei Cloud SWR Documentation](https://support.huaweicloud.com/swr/index.html) <br>
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html) <br>
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with hcloud CLI command examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires hcloud CLI, Huawei Cloud region selection, and Huawei Cloud credentials supplied outside the skill content.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
