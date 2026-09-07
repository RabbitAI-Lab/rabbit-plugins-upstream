## Description:

vmware-vks helps agents manage vSphere Kubernetes Service (VKS), including Supervisor clusters, vSphere Namespaces, TKC cluster lifecycle operations, kubeconfig retrieval, and Harbor registry checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to check VKS compatibility, manage vSphere Namespaces, create, scale, upgrade, and delete TKC clusters, retrieve kubeconfigs, and inspect Harbor or namespace storage information. It is intended for configured vSphere 8.x+ environments with Workload Management enabled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can access live cluster credentials such as kubeconfigs and session tokens.

Mitigation: Use secured workstations, avoid printing kubeconfigs into chat, write credentials only to secure file paths, and prefer secret-manager injection for vCenter passwords.

Risk: Namespace, cluster lifecycle, scale, upgrade, and delete actions can change production VKS environments.

Mitigation: Restrict use to trusted operators with least-privilege vCenter and Supervisor accounts, keep dry-run or confirmation gates for writes, and review policy and audit settings before enabling state-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vks)
- [VMware-VKS project homepage](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](artifact/references/capabilities.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, YAML plans, JSON or tool responses, and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to write kubeconfigs to local files rather than printing live credentials into conversation context.]

## Skill Version(s):

1.9.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
