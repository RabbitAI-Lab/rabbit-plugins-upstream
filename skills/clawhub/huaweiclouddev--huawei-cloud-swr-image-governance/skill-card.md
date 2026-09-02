## Description:

Huawei Cloud SWR image governance skill using hcloud CLI for namespace and repository permissions, retention rules, shared download domains, image sharing checks, agency delegation, and repository reference queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud platform engineers use this skill to audit and manage Huawei Cloud SWR governance controls. It helps them prepare hcloud CLI commands, confirm sensitive changes, parse SWR responses, and apply least-privilege access, retention, sharing, and agency delegation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud permission grants, updates, or revocations can create overly broad access or immediately break CI/CD and service workflows.

Mitigation: Use least-privilege Huawei Cloud credentials, review every proposed Create, Update, or Delete command, and confirm target users, resources, scope, and auth level before execution.

Risk: Retention rules can permanently delete image tags when cleanup runs.

Mitigation: Verify retention conditions carefully, protect critical tags such as latest or stable where appropriate, and confirm the repository and rule parameters before creating or updating retention rules.

Risk: Shared download domains can expose images to another Huawei Cloud account and may increase traffic costs, especially with deadline=forever.

Mitigation: Prefer explicit expiration dates, confirm the target IAM domain, audit shared domains periodically, and delete domains that are expired or no longer needed.

Risk: Creating SWR agency delegation allows SWR to perform cross-service operations on the user's behalf.

Mitigation: Check agency status first, confirm the delegation scope, and use temporary or least-privilege credentials where possible.

Risk: Huawei Cloud AK, SK, and security token values are sensitive credentials.

Mitigation: Pass credentials through environment variables, avoid printing or hardcoding secret values, and install hcloud only after verifying the CLI source.

## Reference(s):

- [SWR Governance API Reference Guide](references/swr-governance-api-guide.md)
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md)
- [IAM Permission Policies - SWR Image Governance Skill](references/iam-policies.md)
- [Verification Method - SWR Image Governance Skill](references/verification-method.md)
- [SWR Image Governance - Output Format](references/output-format.md)
- [Task: Namespace Permissions](references/task-namespace-permissions.md)
- [Task: Repository Permissions](references/task-repository-permissions.md)
- [Task: Retention Management](references/task-retention-management.md)
- [Task: Shared Domains](references/task-shared-domains.md)
- [Task: Image Sharing](references/task-image-sharing.md)
- [Common Pitfalls & Solutions](references/common-pitfalls.md)
- [Huawei Cloud SWR Documentation](https://support.huaweicloud.com/swr/index.html)
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html)
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON response summaries, tables, and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations require explicit user confirmation; hcloud CLI output is parsed into concise human-readable summaries.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
