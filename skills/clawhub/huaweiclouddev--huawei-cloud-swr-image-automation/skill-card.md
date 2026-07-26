## Description: <br>
Huawei Cloud SWR image automation and operations skill using hcloud CLI for cross-region image sync, sync status checks, and trigger-based deployment management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud platform engineers use this skill to draft and verify hcloud CLI commands for Huawei Cloud SWR cross-region image replication, manual image sync, sync job checks, and CCE/CCI auto-deploy trigger lifecycle management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can create, update, delete, or enable live SWR sync and auto-deploy behavior. <br>
Mitigation: Use a test repository and namespace first, confirm all source and target resources before execution, and require explicit approval before write, delete, manual sync, or enabled auto-deploy commands. <br>
Risk: Broad write permissions can modify image sync and trigger configuration across repositories. <br>
Mitigation: Start with the read-only IAM policy, grant the full automation policy only when needed, and prefer temporary least-privilege credentials. <br>
Risk: Incorrect regions, namespaces, repositories, cluster IDs, trigger conditions, or override settings can replicate or deploy unintended images. <br>
Mitigation: Run read-only verification commands first, keep override disabled unless intentional, and review exact region, namespace, repository, cluster, application, and trigger values before execution. <br>
Risk: Credential exposure could occur if access keys or security tokens are printed or embedded in commands. <br>
Mitigation: Use environment variables or masked hcloud configuration, avoid echoing secrets, and rotate credentials after testing or production use. <br>


## Reference(s): <br>
- [SWR Automation API Guide](references/swr-automation-api-guide.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Task: Image Sync](references/task-image-sync.md) <br>
- [Task: Trigger Management](references/task-trigger-management.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Common Pitfalls](references/common-pitfalls.md) <br>
- [Huawei Cloud SWR Documentation](https://support.huaweicloud.com/swr/index.html) <br>
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html) <br>
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and command explanations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include hcloud SWR commands, IAM policy guidance, pre-run verification steps, and cleanup instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
