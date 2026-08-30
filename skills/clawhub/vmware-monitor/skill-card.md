## Description:

vmware-monitor provides read-only VMware vCenter and ESXi monitoring for inventory, health, alarms, events, performance, capacity, and object-centered investigations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators, SREs, and developers use this skill to query VMware vCenter and ESXi inventory and health, triage alarms and events, and produce read-only investigation summaries before choosing any remediation path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to VMware infrastructure and requires target credentials.

Mitigation: Use a read-only vCenter or ESXi account, keep ~/.vmware-monitor/.env locked down, or inject credentials from a secret manager.

Risk: Optional Slack or Discord webhooks can send aggregated infrastructure alert metadata to configured destinations.

Mitigation: Configure webhooks only for approved destinations and start the daemon only when scheduled alert delivery is intended.

Risk: Disabling TLS verification can hide connection integrity problems.

Mitigation: Keep TLS verification enabled in production and reserve verify_ssl: false for isolated lab or home systems with self-signed certificates.

Risk: Read-only source-level enforcement does not replace infrastructure permissions.

Mitigation: Deploy with VMware accounts that are permissioned read-only so platform controls enforce the same operating boundary.

Risk: Large inventory or event results may be truncated or bounded by the backing VMware API.

Mitigation: Check returned, total, truncated, and hint fields before treating a list result as complete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-monitor)
- [Project Homepage](https://github.com/vmware-skills/VMware-Monitor)
- [Setup Guide](artifact/references/setup-guide.md)
- [Capabilities Reference](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)
- [Investigation Protocol](artifact/references/investigation-protocol.md)
- [Health Summary Template](artifact/references/health-summary-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, CLI tables, MCP JSON envelopes, and optional self-contained HTML snapshots.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only VMware monitoring output; list-style MCP tools include returned, limit, total, truncated, and hint fields.]

## Skill Version(s):

1.8.14 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
