## Description:

Manages Huawei Cloud CCE cluster lifecycle, node pools, nodes, addons, EIP binding, and kubeconfig retrieval using hcloud CLI, kubectl-cce, and limited Python SDK fallbacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to administer Huawei Cloud CCE clusters, node pools, nodes, addons, network access, and kubeconfig retrieval from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer high-impact Huawei CCE resources, including deleting clusters, scaling node pools, draining nodes, and changing addons.

Mitigation: Use temporary, least-privilege IAM credentials and require explicit review before confirming destructive or service-affecting operations.

Risk: Kubeconfig retrieval can expose cluster access material.

Mitigation: Avoid pasting or logging returned kubeconfig data, keep its validity short, and treat returned credentials as sensitive.

Risk: Security evidence reports under-scoped confirmation safeguards for cluster awakening and kubeconfig retrieval.

Mitigation: Patch or manually enforce confirmation for cluster awakening and kubeconfig retrieval before use against important clusters.

Risk: The CLI installer is fetched remotely as part of the documented setup path.

Mitigation: Review the remote installer before execution and install dependencies from trusted environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cce-cluster-management)
- [CCE hcloud Operation Reference](references/cce-api-guide.md)
- [Cluster Creation Parameter Reference](references/cce-cluster-parameters.md)
- [CCE IAM Permission Configuration](references/iam-policies.md)
- [Cluster Management Task Details](references/task-cluster-management.md)
- [Node Pool Management Task Details](references/task-nodepool-management.md)
- [Node Management Task Details](references/task-node-management.md)
- [Feature Verification Steps](references/verification-method.md)
- [Common Troubleshooting Issues](references/troubleshooting.md)
- [Huawei Cloud CCE API Reference](https://support.huaweicloud.com/api-cce/cce_02_0082.html)
- [hcloud KooCLI Documentation](https://support.huaweicloud.com/zh-cn/cli/index.html)
- [kubectl Documentation](https://kubernetes.io/docs/reference/kubectl/)
- [kubectl-cce Plugin](https://support.huaweicloud.com/engineer/cloudeye/cce_03_0123.html)
- [CCE Password Salting and Encryption](https://support.huaweicloud.com/api-cce/add-salt.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-like operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return operation previews, confirmation prompts, cloud resource identifiers, and kubeconfig data that should be handled as sensitive.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
