## Description:

Manages VMware NSX and vDefend distributed firewall policies and rules, security groups, VM tags, Traceflow diagnostics, and IDS/IPS status for agent-assisted security operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and security operators use this skill to inspect and manage NSX DFW policies, security groups, VM tags, Traceflow checks, and IDPS settings with audit-aware controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-assisted NSX firewall and tag changes can immediately affect network traffic.

Mitigation: Use a least-privilege NSX service account, require explicit approval for write operations, prefer dry-run previews where available, and review proposed rule or tag changes before execution.

Risk: Persistent local credential files can expose NSX access if host permissions are too broad.

Mitigation: Prefer secret-manager or ephemeral environment injection for production, and keep config and .env files owner-only.

Risk: Incorrect DFW rule order or group membership criteria can silently permit or block traffic.

Mitigation: Verify group membership, preserve rule sequence semantics, enable logging on new rules during validation, and use Traceflow to validate traffic paths before enforcing deny rules.

## Reference(s):

- [VMware NSX Security homepage](https://github.com/vmware-skills/VMware-NSX-Security)
- [Capabilities Reference](artifact/references/capabilities.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Setup Guide](artifact/references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with CLI commands and structured MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed NSX changes, dry-run commands, audit-aware write guidance, and Traceflow or IDPS status summaries.]

## Skill Version(s):

1.8.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
