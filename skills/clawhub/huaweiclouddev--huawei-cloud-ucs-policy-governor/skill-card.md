## Description: <br>
Huawei Cloud UCS policy governance and compliance management skill using hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and cloud administrators use this skill to manage Huawei Cloud UCS policy instances, policy definitions, policy enforcement, and fleet compliance audits with hcloud CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide create, update, delete, enable, and disable actions that affect policy enforcement on Huawei Cloud UCS clusters or fleet groups. <br>
Mitigation: Use least-privilege or temporary credentials, prefer staging validation first, and require explicit confirmation before any create, update, delete, enable, or disable action. <br>
Risk: Compliance audit workflows can move from reporting into live cluster remediation, including kubeconfig generation and kubectl commands. <br>
Mitigation: Do not allow kubeconfig generation or kubectl execution unless live remediation has been separately approved; clean up sensitive kubeconfig files after use. <br>
Risk: Cloud access keys, secret keys, and security tokens may be exposed if commands print credential environment variables or examples are copied into shared logs. <br>
Mitigation: Verify credentials with masked tooling such as hcloud configure list, avoid echoing secrets, and keep AK/SK or security token values out of conversation, code, and command output. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ucs-policy-governor) <br>
- [UCS Policy API Reference Guide](references/ucs-policy-api-guide.md) <br>
- [Task: Policy Management](references/task-policy-management.md) <br>
- [Task: Compliance Audit](references/task-compliance-audit.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Common Pitfalls and Solutions](references/common-pitfalls.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline hcloud and kubectl command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON response-shape guidance and IAM policy snippets.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
