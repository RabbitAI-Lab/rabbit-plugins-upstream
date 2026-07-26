## Description: <br>
Huawei Cloud UCS Policy Governor helps agents manage Huawei Cloud UCS policy instances, policy definitions, enforcement state, enforcement jobs, and compliance audits through hcloud CLI guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud platform engineers, and compliance operators use this skill to create, update, enable, disable, delete, and audit Huawei Cloud UCS policy instances across clusters and fleet groups. It is intended for UCS policy governance workflows that require hcloud CLI commands, IAM permissions, and compliance review steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit workflows and administrative write workflows are both present, which can lead an agent from observation into live UCS policy changes. <br>
Mitigation: Use read-only IAM permissions for audit sessions and grant write permissions only for explicitly approved create, update, delete, enable, disable, or deny operations. <br>
Risk: Delete, disable, enable, and deny policy commands can change enforcement behavior for clusters or fleet groups. <br>
Mitigation: Require explicit user confirmation before these commands, prefer staging validation first, and start with warn enforcement before switching to deny in production. <br>
Risk: Generated kubeconfig files and Huawei Cloud AK/SK or security token values are sensitive credentials. <br>
Mitigation: Keep credentials out of chat and source control, use masked verification commands, apply restrictive file permissions to kubeconfig files, and remove temporary credential files after use. <br>


## Reference(s): <br>
- [UCS Policy API Guide](references/ucs-policy-api-guide.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Common Pitfalls](references/common-pitfalls.md) <br>
- [Task: Policy Management](references/task-policy-management.md) <br>
- [Task: Compliance Audit](references/task-compliance-audit.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ucs-policy-governor) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown] <br>
**Output Format:** [Markdown guidance with inline hcloud CLI commands and JSON IAM policy examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include read-only audit steps and privileged UCS write operations; requires hcloud CLI and Huawei Cloud credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
