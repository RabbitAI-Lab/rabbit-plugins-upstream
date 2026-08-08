## Description: <br>
Huawei Cloud SWR image governance skill using hcloud CLI for managing namespace and repository permissions, image retention rules, shared download domains, image sharing, agency delegation, and repository references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DevOps engineers, and cloud platform operators use this skill to audit and manage Huawei Cloud SWR access, retention, sharing, and agency settings through reviewed hcloud CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose write operations that immediately change SWR permissions, retention policies, shared domains, or agency delegation. <br>
Mitigation: Review the exact hcloud command, target resource, and requested change before confirming any create, update, or delete operation. <br>
Risk: Cloud credentials or security tokens could be exposed if users print or paste credential values. <br>
Mitigation: Use temporary or least-privilege credentials through environment variables, verify configuration with masked CLI output, and avoid echoing AK, SK, or security token values. <br>
Risk: Retention rules can delete image tags when they execute, and deleted tags may be unrecoverable. <br>
Mitigation: List existing retention rules, verify selectors and retention windows, and start with conservative policies before creating or updating cleanup rules. <br>
Risk: Shared download domains can broaden image access, especially when configured with permanent access. <br>
Mitigation: Prefer expiring read-only shared domains, audit active domains regularly, and delete stale or unnecessary shares. <br>


## Reference(s): <br>
- [ClawHub Release Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-swr-image-governance) <br>
- [SWR Governance API Reference Guide](references/swr-governance-api-guide.md) <br>
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [SWR Image Governance Output Format](references/output-format.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Common Pitfalls and Solutions](references/common-pitfalls.md) <br>
- [Huawei Cloud SWR Documentation](https://support.huaweicloud.com/swr/index.html) <br>
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html) <br>
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown] <br>
**Output Format:** [Markdown with inline shell commands and JSON response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Write operations require explicit user confirmation with command preview and risk context.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
