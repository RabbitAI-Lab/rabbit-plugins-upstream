## Description:

Network AIops supports governed multi-vendor network device operations over NAPALM, including device state reads, diagnostics, configuration backup and diff, configuration merge/replace/rollback, and optional NetBox source-of-truth lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators, SREs, and infrastructure engineers use this skill to inspect Cisco, Arista, Juniper, and other NAPALM-supported devices, troubleshoot interface and BGP issues, back up and compare configurations, and perform governed configuration changes. It is also useful for agents that need optional NetBox lookups alongside live device state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact network configuration operations and handles device and NetBox credentials.

Mitigation: Review before production use, prefer read-only device and NetBox credentials unless writes are explicitly required, and require operators to inspect diffs before merge, replace, rollback, or undo operations.

Risk: Raw device configurations and diffs may contain secrets or sensitive operational data.

Mitigation: Avoid include_secrets=True in agent or MCP workflows, keep enable secrets out of config.yaml, and prefer local file exports when a raw configuration must be reviewed by a human.

Risk: Package supply-chain changes could affect a tool with access to device credentials.

Mitigation: Pin or internally mirror the network-aiops package before granting it production network access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/network-aiops)
- [Project homepage](https://github.com/AIops-tools/Network-AIops)
- [Issue tracker](https://github.com/AIops-tools/Network-AIops/issues)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce device facts, diagnostics, diffs, backups, NetBox summaries, and operator-facing remediation guidance; large configuration outputs may be size-bounded or redacted.]

## Skill Version(s):

0.12.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
