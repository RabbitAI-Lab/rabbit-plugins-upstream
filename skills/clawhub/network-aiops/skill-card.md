## Description:

Network AIops helps agents inspect, diagnose, back up, diff, and change multi-vendor network device configurations through NAPALM with audit, risk-tier, undo, and secret-handling guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators, developers, and SREs use this skill to perform governed Cisco, Arista, Juniper, Nexus, IOS-XR, and NetBox-backed device operations, from read-only health checks and RCA to configuration diff, merge, replace, and rollback workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make real network device configuration changes and does not enforce a universal read-only mode or approval gate.

Mitigation: Install it only where the agent is allowed to reach the configured devices, use read-only device and NetBox accounts unless writes are intended, and require operators to review diffs before merge, replace, rollback, or undo actions.

Risk: Network device configs and diagnostics may contain sensitive operational data or secrets.

Mitigation: Keep the state directory locked down, prefer encrypted secrets, avoid plaintext credential fallbacks, and do not request raw configs with include_secrets=True unless the operator understands they may enter logs or transcripts.

## Reference(s):

- [Network-AIops homepage](https://github.com/AIops-tools/Network-AIops)
- [Capabilities](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Analysis, JSON]

**Output Format:** [Markdown with inline shell commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include network diagnostics, device facts, diffs, backups, and configuration guidance; credential values are normally masked unless raw output is explicitly requested.]

## Skill Version(s):

0.11.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
