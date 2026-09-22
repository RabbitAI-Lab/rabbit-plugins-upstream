## Description:

Manages Huawei Cloud CCE cluster lifecycle, node pools, nodes, addons, network prerequisites, and kubeconfig retrieval using the Huawei Cloud Python SDK v3.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pintudeyudi](https://clawhub.ai/user/pintudeyudi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud platform administrators use this skill to inspect and manage Huawei Cloud CCE Kubernetes clusters, including cluster lifecycle operations, node and node pool management, addon operations, EIP binding, and kubeconfig retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact CCE operations can delete clusters, delete nodes or node pools, hibernate clusters, uninstall addons, or evict workloads.

Mitigation: Install only for trusted CCE administrators and require explicit human confirmation before any operation that changes cluster state.

Risk: The security summary reports mismatched safety gating for state-changing controls.

Mitigation: Manually enforce confirmation for all state-changing operations until the manifest and implementation are fixed.

Risk: Credential and kubeconfig handling can expose sensitive cluster access material.

Mitigation: Use least-privilege IAM credentials from environment variables or a secret store, avoid passing secrets as tool arguments, and do not return or log kubeconfig unless required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pintudeyudi/skills/huawei-cloud-cce-cluster-management)
- [Cluster management task details](references/task-cluster-management.md)
- [Node pool management task details](references/task-nodepool-management.md)
- [Node management task details](references/task-node-management.md)
- [IAM permission policy](references/iam-policies.md)
- [Feature verification steps](references/verification-method.md)
- [Troubleshooting guide](references/troubleshooting.md)
- [CCE SDK API reference](references/cce-api-guide.md)
- [Cluster creation parameter reference](references/cce-cluster-parameters.md)
- [Huawei Cloud CCE API Reference](https://support.huaweicloud.com/api-cce/cce_02_0082.html)
- [Huawei Cloud CCE Python SDK](https://support.huaweicloud.com/sdk-python/cce_02_0101.html)
- [Huawei Cloud CCE password salting and encryption](https://support.huaweicloud.com/api-cce/add-salt.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-formatted tool results and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool calls may return status, data, message, and warning fields; preview responses are expected for dangerous operations.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
