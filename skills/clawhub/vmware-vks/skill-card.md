## Description: <br>
Vmware Vks helps agents manage vSphere Kubernetes Service environments, including Supervisor clusters, vSphere Namespaces, TKC lifecycle operations, kubeconfig retrieval, Harbor checks, and storage usage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to inspect VKS readiness and operate vSphere Namespaces and Tanzu Kubernetes clusters through guided CLI or MCP workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retrieve kubeconfigs that contain live short-lived vCenter session tokens. <br>
Mitigation: Require explicit approval before kubeconfig retrieval, write kubeconfigs to files instead of conversation output, and keep exported files permission-restricted with cleanup expectations. <br>
Risk: Credential setup may place vCenter passwords in local environment files. <br>
Mitigation: Use least-privilege vCenter accounts and prefer secret-manager or runtime environment injection over storing passwords in .env files. <br>
Risk: TLS verification can be disabled for self-signed vCenter certificates. <br>
Mitigation: Set verify_ssl to true with trusted certificates wherever possible and review exceptions before production use. <br>
Risk: Write operations can change or delete VKS namespaces and TKC clusters. <br>
Mitigation: Review dry-run plans, keep destructive actions behind confirmation, and rely on audit logging and workload guards before applying changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vks) <br>
- [VMware VKS homepage](https://github.com/zw008/VMware-VKS) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured CLI or MCP results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run plans, operational checks, and file paths for kubeconfig exports; agents should avoid printing live tokens.] <br>

## Skill Version(s): <br>
1.8.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
