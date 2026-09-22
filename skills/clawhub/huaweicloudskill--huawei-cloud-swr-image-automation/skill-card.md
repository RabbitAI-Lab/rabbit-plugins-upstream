## Description:

Huawei Cloud SWR (Software Repository for Container) image automation and operations skill using hcloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to configure Huawei Cloud SWR cross-region image sync, manage trigger-based CCE/CCI auto-deployment, inspect sync status, and troubleshoot hcloud CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can propose cloud-changing SWR sync and trigger operations with broad operational impact.

Mitigation: Use temporary least-privilege Huawei Cloud credentials, restrict IAM scope where possible, require explicit user confirmation for write operations, and test workflows against non-production repositories and workloads unless a live deployment change is intended.

Risk: hcloud installation examples download and run installer assets.

Mitigation: Review install commands before running them and prefer pinned or otherwise verified hcloud installation methods.

Risk: Cross-region sync, override settings, and auto-deploy triggers can create costs, overwrite target images, or update CCE/CCI workloads unexpectedly.

Mitigation: Confirm billing implications, target repositories, target regions, namespaces, override settings, trigger conditions, and target workloads before execution.

Risk: Some hcloud SWR commands may return API errors while the CLI process exits successfully.

Mitigation: Inspect command output for error_code and error_msg fields instead of relying only on the shell exit code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-swr-image-automation)
- [SWR Automation API Guide](references/swr-automation-api-guide.md)
- [Task: Image Sync](references/task-image-sync.md)
- [Task: Trigger Management](references/task-trigger-management.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Common Pitfalls & Solutions](references/common-pitfalls.md)
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud SWR documentation](https://support.huaweicloud.com/swr/index.html)
- [Huawei Cloud hcloud CLI documentation](https://support.huaweicloud.com/cli/index.html)
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/)
- [Huawei Cloud SWR Quick Start](https://support.huaweicloud.com/qs-swr/index.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with hcloud CLI command examples and JSON policy snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Huawei Cloud hcloud CLI and user-confirmed credentials for live operations.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
