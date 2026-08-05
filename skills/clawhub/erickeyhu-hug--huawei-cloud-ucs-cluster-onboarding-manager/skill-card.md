## Description: <br>
Huawei Cloud UCS cluster onboarding, lifecycle, and fleet management via hcloud CLI for registering, querying, removing, grouping, quota-checking, and kubeconfig workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud platform engineers use this skill to administer Huawei Cloud UCS clusters through hcloud CLI workflows, including onboarding CCE or self-managed clusters, organizing fleet groups, retrieving access configuration, and checking quotas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill supports administration of powerful Huawei Cloud UCS resources and cluster credentials. <br>
Mitigation: Install only when UCS administration is needed, use least-privilege IAM, prefer temporary credentials, and protect hcloud configuration files. <br>
Risk: Some examples may be unsafe or under-scoped for production environments, including broad Resource "*" policies. <br>
Mitigation: Review proposed commands and policies before use, and narrow IAM resources and permissions wherever possible. <br>
Risk: Kubeconfig and federation-kubeconfig workflows can expose sensitive cluster access material. <br>
Mitigation: Do not paste kubeconfig contents into chats, logs, shell history, or CI output; store generated files with strict permissions. <br>
Risk: Register, update, join or leave, delete, kubeconfig generation, and federation-kubeconfig retrieval operations can change cloud state or expose access. <br>
Mitigation: Require explicit user confirmation before executing those operations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ucs-cluster-onboarding-manager) <br>
- [Huawei Cloud UCS Documentation](https://support.huaweicloud.com/ucs/index.html) <br>
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html) <br>
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/) <br>
- [UCS Cluster Onboarding API Reference Guide](references/ucs-cluster-onboarding-api-guide.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Task: Cluster Registration & Deregistration](references/task-cluster-registration.md) <br>
- [Task: Fleet Management](references/task-fleet-management.md) <br>
- [Task: Access Management](references/task-access-management.md) <br>
- [Verification Method](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown with inline hcloud and kubectl command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce cloud operation steps that require explicit user confirmation and secure handling of credentials or kubeconfig content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
