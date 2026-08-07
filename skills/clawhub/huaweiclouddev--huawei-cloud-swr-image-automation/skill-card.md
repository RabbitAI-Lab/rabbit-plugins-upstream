## Description: <br>
Huawei Cloud SWR image automation and operations skill using hcloud CLI for cross-region image sync, trigger-based CCE/CCI auto-deployment, sync-region queries, sync-job status checks, and trigger configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to configure and verify Huawei Cloud SWR image replication and deployment triggers through hcloud CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide cloud write operations that create, update, or delete SWR sync settings and deployment triggers. <br>
Mitigation: Confirm every write command, target resource, and intended change with the user before execution, and prefer test or named resources for verification. <br>
Risk: Cross-region sync with override enabled can replace existing images in the target region. <br>
Mitigation: Default to override=false unless replacement is intentional, and verify existing target images before using override=true. <br>
Risk: Broad trigger conditions can cause automatic deployments on image pushes beyond the intended scope. <br>
Mitigation: Review trigger type, condition, enable state, and target CCE/CCI workload before creating or updating triggers. <br>
Risk: Huawei Cloud credentials and permissions are required for CLI operations. <br>
Mitigation: Use temporary or least-privilege IAM credentials where possible, keep secrets in environment variables, and avoid exposing AK/SK or security tokens in commands or conversation. <br>


## Reference(s): <br>
- [SWR Automation API Reference Guide](references/swr-automation-api-guide.md) <br>
- [Task: Image Sync](references/task-image-sync.md) <br>
- [Task: Trigger Management](references/task-trigger-management.md) <br>
- [IAM Permission Policies - SWR Image Automation Skill](references/iam-policies.md) <br>
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [Verification Method - SWR Image Automation Skill](references/verification-method.md) <br>
- [Acceptance Criteria: Correct/Error Pattern Comparison](references/acceptance-criteria.md) <br>
- [Common Pitfalls & Solutions](references/common-pitfalls.md) <br>
- [Huawei Cloud SWR Quick Start](https://support.huaweicloud.com/qs-swr/index.html) <br>
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/cli/index.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline hcloud CLI commands and JSON-oriented command output instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Write operations require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
