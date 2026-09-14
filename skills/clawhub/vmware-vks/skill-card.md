## Description:

Manages vSphere Kubernetes Service Supervisor clusters, vSphere Namespaces, TKC cluster lifecycle, kubeconfig retrieval, and Harbor registry checks through the vmware-vks CLI or MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to check VKS compatibility and administer Supervisor Namespaces and Tanzu Kubernetes clusters in vSphere 8.x+ environments. It supports both read-only environment checks and approval-gated infrastructure changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles powerful infrastructure credentials and kubeconfigs that can grant vCenter-backed access for hours.

Mitigation: Use a least-privileged vCenter account, approve kubeconfig export only when specifically needed, write exports to owner-only files, and delete exported kubeconfigs after use.

Risk: Example configuration recommends an insecure TLS setting for production use.

Mitigation: Use verify_ssl: true with a trusted CA or pinned certificate for production environments.

Risk: Long-lived passwords may be stored in a local .env file.

Mitigation: Prefer a secret manager when available and keep any local credential files owner-only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vks)
- [Project homepage from ClawHub metadata](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, code]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to call vmware-vks CLI or MCP tools; kubeconfig outputs should be written to owner-only files and not printed.]

## Skill Version(s):

1.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
