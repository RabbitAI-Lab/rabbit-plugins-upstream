## Description:

Manages vSphere Kubernetes Service environments, including Supervisor clusters, vSphere Namespaces, TKC cluster lifecycle, kubeconfig access, and Harbor registry checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform operators use this skill to check VKS readiness and administer Supervisor Namespaces and TKC clusters in configured vCenter environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact VKS administration actions can create, update, scale, upgrade, or delete namespaces and TKC clusters.

Mitigation: Install only for authorized vCenter/VKS operators, use least-privilege service accounts, and require explicit approval before cluster writes.

Risk: Kubeconfig retrieval exposes bearer-token access to Supervisor or TKC Kubernetes APIs.

Mitigation: Run credential access only on explicit user request, write kubeconfigs to owner-only files, avoid printing token contents, and delete exported files after use.

Risk: Local configuration, password files, exported kubeconfigs, and audit logs contain sensitive operational data.

Mitigation: Keep local files owner-only, prefer a secret manager for passwords, and rotate or delete retained files according to the operator's policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vks)
- [VMware VKS source homepage](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, MCP tool guidance, and structured command or tool results when executed by the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to create owner-only kubeconfig files when explicitly requested; credential contents should not be printed.]

## Skill Version(s):

1.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
