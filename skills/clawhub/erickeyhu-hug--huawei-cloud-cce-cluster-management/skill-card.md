## Description: <br>
Huawei Cloud CCE (Cloud Container Engine) cluster lifecycle management skill using Python SDK v3. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to manage Huawei Cloud CCE clusters, nodes, node pools, addons, public EIP binding, and kubeconfig retrieval from an agent workflow. <br>

### Deployment Geography for Use: <br>
Huawei Cloud CCE regions listed in the skill documentation, including mainland China and Asia-Pacific regions. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive cluster credentials, including kubeconfig output. <br>
Mitigation: Treat kubeconfig output as a secret, avoid logging or sharing it, and use a narrowly scoped IAM identity. <br>
Risk: Cluster deletion, hibernation, node drain, scaling, addon removal, and similar operations can disrupt workloads or delete resources. <br>
Mitigation: Use the documented preview flow first, require confirm=true only after human review, and schedule disruptive changes during approved maintenance windows. <br>
Risk: Binding a public EIP can change cluster exposure. <br>
Mitigation: Require explicit approval before public EIP binding and verify network access controls before execution. <br>
Risk: Long-lived or overprivileged Huawei Cloud AK/SK credentials increase production account impact. <br>
Mitigation: Use narrowly scoped IAM permissions, avoid long-lived admin keys, prefer environment variables or per-call credentials, and prefer SSH keys over node passwords. <br>


## Reference(s): <br>
- [Cluster Lifecycle Operations](references/task-cluster-management.md) <br>
- [Node Pool Operations](references/task-nodepool-management.md) <br>
- [Node Scheduling Operations](references/task-node-management.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Verification Steps](references/verification-method.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>
- [CCE Python SDK API Reference](references/cce-api-guide.md) <br>
- [Cluster and Node Pool Parameters](references/cce-cluster-parameters.md) <br>
- [Huawei Cloud CCE API Reference](https://support.huaweicloud.com/api-cce/cce_02_0082.html) <br>
- [Huawei Cloud CCE Python SDK](https://support.huaweicloud.com/sdk-python/cce_02_0101.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON-formatted tool results with status, data, message, and warning fields, plus Markdown and bash examples in guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Dangerous operations are designed to return a preview unless confirm=true is supplied.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
