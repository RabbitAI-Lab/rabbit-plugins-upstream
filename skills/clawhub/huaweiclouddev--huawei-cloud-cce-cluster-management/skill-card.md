## Description:

Manages Huawei Cloud CCE cluster lifecycle, node pools, nodes, addons, public endpoint binding, and kubeconfig retrieval through hcloud/KooCLI, kubectl cce, and selected Python SDK fallbacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud administrators use this skill to operate Huawei Cloud CCE clusters, node pools, nodes, addons, EIP bindings, and kubeconfig retrieval from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform disruptive Huawei Cloud CCE operations such as deleting clusters or nodes, hibernating clusters, resizing node pools, uninstalling addons, and draining nodes.

Mitigation: Install only for trusted Huawei Cloud administrators, preview dangerous operations first, require explicit `confirm=true` before execution, and review the target resource and impact before approval.

Risk: The skill can retrieve kubeconfig data and create or bind public EIPs, which can expand administrative or network exposure.

Mitigation: Review every kubeconfig retrieval and public IP operation, restrict use to intended clusters, and prefer the narrowest operational access needed for the task.

Risk: Huawei Cloud credentials may be exposed if passed through command arguments or overly broad long-lived credentials are used.

Mitigation: Use narrowly scoped temporary credentials where possible and prefer configured environment or hcloud credentials so AK/SK values do not need to be passed in argv.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cce-cluster-management)
- [CCE hcloud Operation Reference](references/cce-api-guide.md)
- [Cluster Creation Parameter Reference](references/cce-cluster-parameters.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [CCE IAM Permission Configuration](references/iam-policies.md)
- [Cluster Management Task Details](references/task-cluster-management.md)
- [Node Management Task Details](references/task-node-management.md)
- [Node Pool Management Task Details](references/task-nodepool-management.md)
- [Common Troubleshooting Issues](references/troubleshooting.md)
- [Feature Verification Steps](references/verification-method.md)
- [CCE API Reference](https://support.huaweicloud.com/api-cce/cce_02_0082.html)
- [hcloud KooCLI Documentation](https://support.huaweicloud.com/zh-cn/cli/index.html)
- [kubectl Documentation](https://kubernetes.io/docs/reference/kubectl/)
- [kubectl-cce Plugin](https://support.huaweicloud.com/engineer/cloudeye/cce_03_0123.html)
- [CCE Password Salting and Encryption](https://support.huaweicloud.com/api-cce/add-salt.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, parameter tables, and JSON-like command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Huawei Cloud APIs, kubectl cce operations, and Python SDK fallbacks when prerequisites and credentials are provided.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter declares 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
