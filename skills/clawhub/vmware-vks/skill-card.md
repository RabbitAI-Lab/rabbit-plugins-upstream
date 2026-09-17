## Description:

Manages vSphere Kubernetes Service (VKS) Supervisor clusters, vSphere Namespaces, TKC cluster lifecycle, kubeconfig retrieval, and Harbor registry checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to check VKS readiness, manage vSphere Namespaces, create, scale, upgrade, or delete TKC clusters, retrieve kubeconfigs, and inspect Harbor and storage status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles vCenter credentials and can export kubeconfigs containing bearer tokens.

Mitigation: Use a narrowly scoped vCenter service account, run kubeconfig retrieval only on explicit request, write kubeconfigs to short-lived owner-only files, and delete them after use.

Risk: Namespace and TKC operations can change infrastructure state or disrupt workloads.

Mitigation: Keep dry-run previews enabled for creation, require explicit approval for writes, respect delete guards, and review audit records for state-changing operations.

Risk: Using verify_ssl: false weakens TLS protection for vCenter connections.

Mitigation: Prefer verify_ssl: true with a CA-signed certificate or configure a trusted private CA before production use.

Risk: External package installation can introduce supply-chain exposure if the package source or distribution path is not trusted.

Mitigation: Install a pinned version only from a trusted source, review the project source, and validate package integrity according to local release controls.

Risk: Local password, audit, and kubeconfig files may persist longer than intended.

Mitigation: Avoid storing production passwords in readable .env files when a secret manager is available, keep file permissions owner-only, and apply retention or pruning for audit logs and exported kubeconfigs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vks)
- [Project homepage](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, MCP tool guidance, YAML or JSON configuration, and file path outputs for exported kubeconfigs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dry-run plans, operational status summaries, command snippets, and paths to owner-only kubeconfig files; live credential material should not be printed.]

## Skill Version(s):

1.10.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
