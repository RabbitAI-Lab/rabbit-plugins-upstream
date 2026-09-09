## Description:

Guides agents through Huawei Cloud CCE cluster lifecycle, node pool, node, addon, EIP, and kubeconfig operations using hcloud and kubectl cce.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud platform engineers use this skill to operate Huawei Cloud CCE clusters, node pools, nodes, addons, public access, and kubeconfig retrieval from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make high-impact Huawei Cloud CCE changes, including deleting or hibernating clusters, resizing or deleting node pools, draining or deleting nodes, uninstalling addons, and creating public EIPs.

Mitigation: Use the documented two-step confirmation flow, require manual review before setting confirm=true, and avoid running destructive or capacity-changing operations against production without an approved maintenance plan.

Risk: Credentials and returned kubeconfig data can grant access to real cloud infrastructure.

Mitigation: Use least-privilege or temporary Huawei Cloud credentials, keep kubeconfig output secret, avoid broad administrator permissions, and rotate credentials after sensitive workflows.

Risk: The skill depends on external CLI tooling and remote installers for hcloud, kubectl, and kubectl-cce.

Mitigation: Verify installers and tool versions before use, install from trusted Huawei Cloud and Kubernetes sources, and rerun the documented verification checklist in each new environment.

## Reference(s):

- [CCE hcloud Operation Reference](references/cce-api-guide.md)
- [CCE Cluster Parameters](references/cce-cluster-parameters.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Cluster Management Tasks](references/task-cluster-management.md)
- [Node Pool Management Tasks](references/task-nodepool-management.md)
- [Node Management Tasks](references/task-node-management.md)
- [Troubleshooting](references/troubleshooting.md)
- [Feature Verification Steps](references/verification-method.md)
- [Huawei Cloud CCE API Reference](https://support.huaweicloud.com/api-cce/cce_02_0082.html)
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/zh-cn/cli/index.html)
- [kubectl Documentation](https://kubernetes.io/docs/reference/kubectl/)
- [kubectl-cce Plugin](https://support.huaweicloud.com/engineer/cloudeye/cce_03_0123.html)
- [CCE Password Salting and Encryption](https://support.huaweicloud.com/api-cce/add-salt.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue real Huawei Cloud API and kubectl-cce operations when invoked with valid credentials and explicit confirmation for dangerous actions.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
