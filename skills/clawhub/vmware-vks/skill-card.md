## Description: <br>
Manages vSphere Kubernetes Service (VKS) Supervisor clusters, vSphere Namespaces, TKC cluster lifecycle, kubeconfig access, and Harbor registry checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to operate VMware vSphere Kubernetes Service environments, including namespace administration, TKC cluster creation, scaling, upgrades, deletion, compatibility checks, and kubeconfig retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give agents live control over VMware Kubernetes resources, including namespace and TKC cluster write operations. <br>
Mitigation: Install only for authorized administrators, use least-privilege vCenter accounts, keep write and destructive operations gated by explicit user approval, and rely on dry-run previews where available. <br>
Risk: Kubeconfig retrieval can expose credential-bearing session tokens if printed into chat or logs. <br>
Mitigation: Require an explicit user request for kubeconfig retrieval, write kubeconfigs to local files, and never paste kubeconfig, bearer tokens, or session tokens into the conversation. <br>
Risk: Local password files and relaxed TLS settings can increase credential or transport exposure in production environments. <br>
Mitigation: Prefer a secret manager over local .env passwords, restrict file permissions when local configuration is used, and enable TLS verification for production vCenter endpoints. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-vks) <br>
- [VMware VKS Source Homepage](https://github.com/vmware-skills/VMware-VKS) <br>
- [Capabilities](references/capabilities.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with CLI commands, configuration examples, and structured operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct agents to call the vmware-vks CLI or MCP server and to write kubeconfig output to files instead of chat.] <br>

## Skill Version(s): <br>
1.8.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
