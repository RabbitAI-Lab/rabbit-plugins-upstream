## Description: <br>
Huawei Cloud UCS (Universal Cloud Service) cluster onboarding, lifecycle, and fleet grouping management skill using hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud platform engineers use this skill to register Huawei Cloud CCE and self-managed Kubernetes clusters with UCS, manage cluster lifecycle and fleet groups, retrieve kubeconfig access, and check UCS quotas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles powerful Huawei Cloud UCS administration workflows, including cluster credentials and destructive cluster-management commands. <br>
Mitigation: Use temporary or least-privilege IAM credentials, avoid cluster-admin kubeconfigs unless required, and manually confirm every delete or deregistration command against the exact target IDs. <br>
Risk: Kubeconfig and federation kubeconfig output can expose cluster access if pasted into chat, command arguments, logs, or public repositories. <br>
Mitigation: Do not paste kubeconfig content into chat or command arguments; write kubeconfig output only to protected files and restrict file permissions. <br>


## Reference(s): <br>
- [UCS Cluster Onboarding API Guide](references/ucs-cluster-onboarding-api-guide.md) <br>
- [Task: Cluster Registration](references/task-cluster-registration.md) <br>
- [Task: Fleet Management](references/task-fleet-management.md) <br>
- [Task: Access Management](references/task-access-management.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Output Format](references/output-format.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Common Pitfalls](references/common-pitfalls.md) <br>
- [Huawei Cloud UCS Documentation](https://support.huaweicloud.com/ucs/index.html) <br>
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html) <br>
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash commands and JSON/YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose hcloud CLI commands that create, update, delete, or retrieve UCS cluster, fleet, quota, and kubeconfig resources.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
