## Description:

Huawei Cloud SWR (Software Repository for Container) image automation and operations skill using hcloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud platform engineers use this skill to configure and inspect Huawei Cloud SWR cross-region image sync, sync jobs, and CCE/CCI auto-deploy triggers through hcloud CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create persistent image sync or auto-deploy trigger behavior that affects live Huawei Cloud workloads.

Mitigation: Use least-privilege temporary credentials, test in non-production namespaces first, and require explicit review before creating sync configs or enabling CCE/CCI triggers.

Risk: Using override=true can overwrite existing images in a target region.

Mitigation: Avoid override=true unless the target images are intentionally replaceable, and require explicit confirmation before running the command.

Risk: All-push production triggers can deploy unintended image versions.

Mitigation: Prefer tag or regex conditions aligned to release controls, and review trigger conditions before enabling production auto-deploy.

Risk: Credential or installer handling can expose cloud access or execute unverified installer content.

Mitigation: Use temporary least-privilege credentials, do not reveal AK/SK or security tokens, and verify the hcloud installer before execution.

## Reference(s):

- [Huawei Cloud SWR Image Automation Skill](artifact/SKILL.md)
- [SWR Automation API Reference Guide](artifact/references/swr-automation-api-guide.md)
- [Task: Image Sync](artifact/references/task-image-sync.md)
- [Task: Trigger Management](artifact/references/task-trigger-management.md)
- [IAM Permission Policies - SWR Image Automation Skill](artifact/references/iam-policies.md)
- [Huawei Cloud KooCLI Installation Guide](artifact/references/cli-installation-guide.md)
- [Acceptance Criteria: Correct/Error Pattern Comparison](artifact/references/acceptance-criteria.md)
- [Common Pitfalls & Solutions](artifact/references/common-pitfalls.md)
- [Verification Method - SWR Image Automation Skill](artifact/references/verification-method.md)
- [Huawei Cloud SWR Documentation](https://support.huaweicloud.com/swr/index.html)
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html)
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/)
- [Huawei Cloud SWR Quick Start](https://support.huaweicloud.com/qs-swr/index.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hcloud commands, IAM policy snippets, verification checklists, and user confirmation prompts.]

## Skill Version(s):

1.0.3 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
