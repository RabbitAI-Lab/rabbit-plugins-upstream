## Description:

Use this skill to inspect or manage VMware NSX networking through NSX Manager, including segments, Tier-0 and Tier-1 gateways, NAT, static routes, BGP, IP pools, health checks, and VM-to-segment troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network, virtualization, and platform engineers use this skill to inspect VMware NSX inventory and health, troubleshoot connectivity, and make explicit user-approved NSX networking changes. It is intended for NSX Manager environments where agents may need read access by default and controlled write access for segments, gateways, NAT, routing, BGP, and IP pools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make high-impact NSX networking changes, including segment, gateway, NAT, static route, IP pool, and Tier-0 BGP updates.

Mitigation: Use least-privilege or read-only NSX credentials by default and require explicit human approval before any non-read operation.

Risk: Delete operations can disrupt workloads or remove dependent network configuration.

Mitigation: Review dry-run or MCP delete previews first; only confirm deletion after blockers, blast radius, and attached resources are understood.

Risk: Production credentials and TLS settings can expose sensitive infrastructure if handled loosely.

Mitigation: Keep TLS verification enabled, use a private CA through SSL_CERT_FILE when needed, and store production passwords in a secret manager when available.

## Reference(s):

- [VMware NSX skill homepage](https://github.com/vmware-skills/VMware-NSX)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured MCP guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include NSX inventory summaries, health findings, troubleshooting steps, dry-run previews, and explicit change instructions.]

## Skill Version(s):

1.11.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
