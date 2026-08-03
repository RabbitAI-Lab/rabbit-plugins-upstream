## Description: <br>
Provides Huawei Cloud UCS policy governance and compliance management guidance using the hcloud CLI for policy instances, definitions, enforcement, and audit workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud platform engineers, and cluster administrators use this skill to manage Huawei Cloud UCS policy instances, enable or disable policy enforcement, and audit compliance across clusters or fleet groups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill supports administrative UCS governance actions, including policy creation, update, deletion, and enable or disable operations. <br>
Mitigation: Use least-privilege or temporary Huawei Cloud credentials and require explicit approval before production or fleet-wide changes. <br>
Risk: Some guidance can involve privileged cluster credential generation and live cluster mutation steps. <br>
Mitigation: Review the target cluster, commands, and manifests before execution, and securely delete generated kubeconfig files after use. <br>


## Reference(s): <br>
- [UCS Policy API Reference Guide](references/ucs-policy-api-guide.md) <br>
- [Task: Policy Management](references/task-policy-management.md) <br>
- [Task: Compliance Audit](references/task-compliance-audit.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Common Pitfalls & Solutions](references/common-pitfalls.md) <br>
- [hcloud CLI installer](https://obs.cn-north-4.myhuaweicloud.com/hcloud/client/hcloud_install.sh) <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ucs-policy-governor) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline hcloud CLI commands and JSON policy examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include administrative UCS commands that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
