## Description: <br>
Huawei Cloud SWR image governance skill that helps agents manage namespace permissions, repository permissions, retention rules, shared download domains, image sharing, agency delegation, and related SWR references through hcloud CLI workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DevOps engineers, and cloud administrators use this skill to audit and change Huawei Cloud SWR access, retention, sharing, and agency settings while receiving command guidance and confirmation prompts for write operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated hcloud commands can change live SWR access, retention, sharing, or agency settings. <br>
Mitigation: Install only for users expected to administer Huawei Cloud SWR and require review of every generated hcloud command before confirmation. <br>
Risk: Retention rules can delete container image tags automatically and may affect production repositories. <br>
Mitigation: Test retention rules on non-production repositories before applying them broadly. <br>
Risk: Shared download domains can create long-lived cross-organization access. <br>
Mitigation: Avoid permanent shared domains unless intentionally approved and use explicit expiration where possible. <br>
Risk: Cloud credentials and installer provenance affect account security. <br>
Mitigation: Verify the hcloud installer or binary from official sources and prefer temporary, least-privilege credentials. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-swr-image-governance) <br>
- [SWR Governance API Reference Guide](references/swr-governance-api-guide.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Output Format](references/output-format.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Common Pitfalls](references/common-pitfalls.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown guidance with hcloud CLI commands, JSON-oriented output summaries, tables, and confirmation prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Write operations require explicit user confirmation before execution; read operations may be executed directly when prerequisites are met.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
