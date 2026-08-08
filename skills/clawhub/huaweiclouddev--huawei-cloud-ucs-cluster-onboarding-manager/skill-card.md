## Description: <br>
Huawei Cloud UCS cluster onboarding, lifecycle, and fleet management via hcloud CLI. Register/query/remove clusters, manage fleet groups, obtain kubeconfig, check quotas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud platform engineers use this skill to register, inspect, update, group, access, and remove Huawei Cloud UCS-managed Kubernetes clusters through hcloud CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide operations using powerful Huawei Cloud and Kubernetes credentials. <br>
Mitigation: Use least-privilege Huawei Cloud and Kubernetes identities, prefer temporary credentials, and avoid exposing AK/SK, security tokens, or kubeconfig contents in chats, command histories, or files. <br>
Risk: Cluster registration, update, deletion, fleet, and federation kubeconfig operations can change cloud resources, affect access, or incur costs. <br>
Mitigation: Require explicit user confirmation before paid, destructive, or state-changing operations and confirm target cluster, fleet, region, and account identifiers before execution. <br>
Risk: Generated kubeconfigs and federation kubeconfigs can grant access to managed clusters. <br>
Mitigation: Store generated kubeconfigs with restrictive file permissions, prefer short-lived credentials where supported, and remove temporary files when no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ucs-cluster-onboarding-manager) <br>
- [Publisher profile](https://clawhub.ai/user/huaweiclouddev) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [KooCLI Command Format Standard](references/kocli-command-format.md) <br>
- [Parameter Reference](references/parameter-reference.md) <br>
- [UCS Cluster Onboarding API Reference Guide](references/ucs-cluster-onboarding-api-guide.md) <br>
- [Task: Cluster Registration & Deregistration](references/task-cluster-registration.md) <br>
- [Task: Fleet Management](references/task-fleet-management.md) <br>
- [Task: Access Management](references/task-access-management.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Common Pitfalls & Solutions](references/common-pitfalls.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown with inline bash commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hcloud CLI commands, IAM policy guidance, kubeconfig handling guidance, and confirmation prompts for paid, destructive, or state-changing operations.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
