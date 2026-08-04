## Description: <br>
Huawei Cloud CCE cluster lifecycle management skill using hcloud CLI for Huawei Cloud API calls and kubectl cce for Kubernetes node scheduling operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud platform engineers use this skill to manage Huawei Cloud CCE clusters, node pools, nodes, addons, EIP binding, and kubeconfig retrieval from an agent-assisted workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact Huawei Cloud and Kubernetes administration actions can create, delete, expose, or disrupt CCE resources. <br>
Mitigation: Require explicit human approval before creation, deletion, public EIP, addon, kubeconfig, and other disruptive operations. <br>
Risk: Huawei credentials and kubeconfig material may be exposed through chat, logs, command arguments, or process listings. <br>
Mitigation: Use temporary, least-privilege credentials; avoid retrieving kubeconfig into chat or logs; and prefer a configured hcloud profile or verified secret handling. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cce-cluster-management) <br>
- [CCE hcloud Operation Reference](references/cce-api-guide.md) <br>
- [Cluster Creation Parameter Reference](references/cce-cluster-parameters.md) <br>
- [CCE IAM Permission Configuration](references/iam-policies.md) <br>
- [Cluster Management Task Details](references/task-cluster-management.md) <br>
- [Node Management Task Details](references/task-node-management.md) <br>
- [Node Pool Management Task Details](references/task-nodepool-management.md) <br>
- [Common Troubleshooting Issues](references/troubleshooting.md) <br>
- [Feature Verification Steps](references/verification-method.md) <br>
- [kubectl Installation Documentation](https://kubernetes.io/docs/tasks/tools/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce high-impact cloud administration commands and kubeconfig output that should be reviewed before execution or disclosure.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
