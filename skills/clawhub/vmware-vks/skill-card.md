## Description:

vmware-vks helps agents manage vSphere Kubernetes Service environments, including Supervisor compatibility checks, vSphere Namespaces, TKC cluster lifecycle operations, kubeconfig retrieval, Harbor registry checks, and storage usage review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and platform engineers use this skill to operate vSphere Kubernetes Service environments through agent-assisted CLI or MCP workflows. It supports namespace administration, TKC cluster creation, scaling, upgrades, deletion, kubeconfig access, and pre-flight compatibility checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives agents access to live kubeconfig credentials and vCenter session bearer tokens.

Mitigation: Require operator approval for kubeconfig retrieval, write exported kubeconfigs only to protected paths with restrictive permissions, and never print kubeconfig content or bearer tokens into chat or logs.

Risk: Namespace and TKC write operations can change capacity, delete resources, or disrupt running workloads.

Mitigation: Use least-privilege vCenter accounts, keep dry-run previews enabled for create operations, require explicit confirmation for destructive actions, and rely on the built-in workload and namespace guards before applying changes.

Risk: Per-target vCenter passwords may be supplied through local environment files.

Mitigation: Prefer a secret manager over storing passwords in .env files and restrict access to any local configuration or credential files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vks)
- [Project homepage](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, YAML plans, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to write kubeconfig output to protected local files instead of displaying tokens in chat.]

## Skill Version(s):

1.8.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
