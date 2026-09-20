## Description:

Use this skill to manage VMware NSX security for distributed firewall policies and rules, security groups, VM tags, Traceflow diagnostics, and IDPS profile/status tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and security operators use this skill to inspect and administer VMware NSX/vDefend security controls, including DFW policies, security groups, tags, Traceflow diagnostics, and IDPS status. It is suited to controlled infrastructure operations where proposed writes and destructive actions are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer NSX security policy, including firewall-related write operations.

Mitigation: Install it only for agents intended to manage NSX security policy and use a dedicated least-privilege NSX account.

Risk: Persistent .env credentials can expose NSX access if the host or file permissions are mishandled.

Mitigation: Prefer injected secrets or a secret manager for production, and keep any local credential files tightly permissioned.

Risk: Deletes and tag changes can alter firewall enforcement or group membership.

Mitigation: Keep audit logging enabled and review previews before confirming deletes or tag changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-nsx-security)
- [Publisher profile](https://clawhub.ai/user/zw008)
- [Project homepage](https://github.com/vmware-skills/VMware-NSX-Security)
- [Setup Guide](artifact/references/setup-guide.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Capabilities Reference](artifact/references/capabilities.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce NSX security operation plans, CLI commands, configuration snippets, MCP tool-use guidance, and reviewable previews for destructive changes.]

## Skill Version(s):

1.12.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
