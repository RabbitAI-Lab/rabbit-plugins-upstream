## Description: <br>
Huawei Cloud CCE cluster lifecycle management skill using Python SDK v3. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to manage Huawei Cloud CCE clusters, node pools, nodes, addons, EIP access, and kubeconfig retrieval from an agent workflow. <br>

### Deployment Geography for Use: <br>
Huawei Cloud supported regions documented by the skill, including China and Asia-Pacific regions. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create cloud resources and cause billing or capacity changes. <br>
Mitigation: Use a dedicated least-privilege Huawei IAM user, start in a non-production project, and manually confirm target cluster, node count, and billing impact before create or scale actions. <br>
Risk: Kubeconfig retrieval can expose cluster access credentials. <br>
Mitigation: Treat kubeconfig output as a secret and avoid saving or sharing it in logs, tickets, or persistent agent memory. <br>
Risk: EIP binding and unbinding can change public cluster access. <br>
Mitigation: Manually verify the target cluster, EIP, and exposure impact before bind or unbind actions. <br>
Risk: Destructive or disruptive CCE operations can delete clusters, drain nodes, hibernate clusters, or remove node pools. <br>
Mitigation: Use the preview flow first and execute only after explicit confirmation with the intended resource identifiers. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cce-cluster-management) <br>
- [CCE SDK API Reference](references/cce-api-guide.md) <br>
- [Cluster Creation Parameter Reference](references/cce-cluster-parameters.md) <br>
- [CCE IAM Permission Configuration](references/iam-policies.md) <br>
- [Cluster Management Task Details](references/task-cluster-management.md) <br>
- [Node Pool Management Task Details](references/task-nodepool-management.md) <br>
- [Node Management Task Details](references/task-node-management.md) <br>
- [Feature Verification Steps](references/verification-method.md) <br>
- [Common Troubleshooting Issues](references/troubleshooting.md) <br>
- [Huawei Cloud CCE API Reference](https://support.huaweicloud.com/api-cce/cce_02_0082.html) <br>
- [Huawei Cloud CCE Python SDK](https://support.huaweicloud.com/sdk-python/cce_02_0101.html) <br>
- [Huawei Cloud CCE Password Salting and Encryption](https://support.huaweicloud.com/api-cce/add-salt.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-formatted tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return cloud resource identifiers, operation status, risk warnings, and kubeconfig content.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
