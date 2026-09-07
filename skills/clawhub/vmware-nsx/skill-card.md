## Description:

Manages VMware NSX networking for segments, Tier-0 and Tier-1 gateways, NAT, routing, IP pools, health checks, and connectivity troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to operate VMware NSX networking through guided CLI and MCP workflows. It supports network segment, gateway, NAT, route, IP pool, health, and troubleshooting tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can directly change NSX networking, including segments, gateways, NAT, routes, IP pools, and BGP settings.

Mitigation: Use a read-only or least-privilege service account unless writes are required, and require dry-run or explicit human approval before create, update, delete, NAT, route, IP pool, or BGP changes.

Risk: Production changes may bypass intended controls if policy rules are not configured for sensitive targets.

Mitigation: Configure policy deny rules for production changes and review audit records for state-changing operations.

Risk: Disabling SSL verification outside lab environments can weaken transport security for NSX Manager connections.

Mitigation: Use verify_ssl: true with a trusted CA for production and reserve SSL bypass for lab environments only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-nsx)
- [Project homepage](https://github.com/vmware-skills/VMware-NSX)
- [Setup Guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline shell commands and structured tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include NSX CLI commands, MCP tool selections, configuration checks, and operational review steps.]

## Skill Version(s):

1.8.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
