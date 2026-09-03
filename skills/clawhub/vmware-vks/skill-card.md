## Description:

vmware-vks helps agents manage vSphere Kubernetes Service environments, including Supervisor clusters, vSphere Namespaces, TKC cluster lifecycle, kubeconfig retrieval, and Harbor registry checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to operate VMware vSphere Kubernetes Service resources through agent-guided CLI or MCP workflows. It supports compatibility checks, namespace and TKC cluster lifecycle tasks, kubeconfig retrieval, Harbor checks, and storage usage review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve live kubeconfig tokens for Supervisor and TKC clusters.

Mitigation: Require kubeconfig output to be written to an explicit local file and avoid displaying token-bearing kubeconfig content in chat, logs, or shared transcripts.

Risk: Configured vCenter accounts may allow the agent to manage production VKS resources.

Mitigation: Use least-privilege service accounts, scope accounts to intended vCenter targets, and install only where agent-managed VKS operations are expected.

Risk: Local .env files may contain credential material for vCenter targets.

Mitigation: Prefer secret-manager injection for production passwords; when local files are used, restrict permissions on ~/.vmware-vks/.env.

Risk: Namespace and TKC lifecycle operations can change or delete cluster resources.

Mitigation: Keep dry-run previews and explicit confirmations in the workflow, review plans before apply, and rely on audit logging for write operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vks)
- [Project homepage from ClawHub metadata](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration paths, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to write kubeconfig output to explicit local files instead of displaying token-bearing content.]

## Skill Version(s):

1.9.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
