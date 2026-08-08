## Description: <br>
Huawei Cloud SWR (Software Repository for Container) image automation and operations skill using hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to configure Huawei Cloud SWR cross-region image replication, query sync regions and jobs, and manage CCE/CCI auto-deploy triggers through hcloud CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide real Huawei Cloud SWR replication, trigger changes, overrides, image pushes, and auto-deploy behavior that may alter cloud resources or workloads. <br>
Mitigation: Use temporary least-privilege credentials, prefer test repositories and non-production clusters for verification, and require explicit confirmation before create, update, delete, override, image push, or trigger-enable actions. <br>
Risk: The skill references remote hcloud CLI installers and binaries, and the security summary notes insufficient local integrity warnings. <br>
Mitigation: Verify downloaded installers or binaries before running them and install only from the official Huawei Cloud sources identified by the skill. <br>


## Reference(s): <br>
- [Acceptance Criteria: Correct/Error Pattern Comparison](references/acceptance-criteria.md) <br>
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [Common Pitfalls & Solutions](references/common-pitfalls.md) <br>
- [IAM Permission Policies - SWR Image Automation Skill](references/iam-policies.md) <br>
- [SWR Automation API Reference Guide](references/swr-automation-api-guide.md) <br>
- [Task: Image Sync](references/task-image-sync.md) <br>
- [Task: Trigger Management](references/task-trigger-management.md) <br>
- [Verification Method - SWR Image Automation Skill](references/verification-method.md) <br>
- [Huawei Cloud SWR Quick Start](https://support.huaweicloud.com/qs-swr/index.html) <br>
- [Huawei Cloud SWR Documentation](https://support.huaweicloud.com/swr/index.html) <br>
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html) <br>
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline hcloud CLI commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are intended to be reviewed with explicit user confirmation before write operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
