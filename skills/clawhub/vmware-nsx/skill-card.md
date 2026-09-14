## Description:

Use this skill to inspect and manage VMware NSX networking through NSX Manager, including segments, Tier-0 and Tier-1 gateways, NAT, static routes, BGP, IP pools, inventory health, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, network engineers, and infrastructure operators use this skill to query NSX state, troubleshoot connectivity, and perform explicitly requested network changes through NSX Manager. It is intended for NSX, NSX-T, and NSX 4.x networking tasks, not firewall policy, VM lifecycle, distributed port groups, or load balancing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact NSX network writes through MCP tools without a built-in confirmation gate.

Mitigation: Call write tools only after the user explicitly requests the specific change; prefer CLI dry-run and double-confirm workflows for manual changes.

Risk: Production credentials may be stored locally in the vmware-nsx environment file.

Mitigation: Use read-only or narrowly scoped NSX service accounts where possible, keep file permissions restricted, and prefer secret-manager injection for production passwords.

Risk: Incorrect network changes can disrupt segments, gateways, NAT, routes, BGP, or IP pools.

Mitigation: Use production deny rules in ~/.vmware/rules.yaml, keep TLS verification enabled, and review audit logs for state-changing operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-nsx)
- [Project homepage](https://github.com/vmware-skills/VMware-NSX)
- [Setup Guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and text responses with command examples, configuration snippets, and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce NSX CLI commands, MCP tool guidance, setup instructions, troubleshooting analysis, and change plans that require user approval before write operations.]

## Skill Version(s):

1.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
