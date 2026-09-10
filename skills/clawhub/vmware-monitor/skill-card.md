## Description:

VMware Monitor helps agents perform safe, read-only VMware vCenter and ESXi monitoring, including inventory, alarms, events, performance, capacity, and object-centered investigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and infrastructure operators use this skill to inspect VMware and vSphere environments, triage alarms and capacity or performance issues, and gather read-only context before any operational changes are made elsewhere.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can read VMware and vSphere operational data exposed through configured targets.

Mitigation: Install only in environments where the agent should have that visibility and use a read-only VMware account.

Risk: Local configuration may include VMware credentials and optional webhook URLs.

Mitigation: Restrict permissions on ~/.vmware-monitor/.env or inject secrets from a secret manager, and enable webhooks only for approved destinations.

Risk: Production use depends on the installed PyPI or GitHub package matching the reviewed release.

Mitigation: Pin the package version and review the package source or release fingerprint before deployment.

Risk: Monitoring output can be incomplete when a configured vCenter is unreachable or a result set is truncated.

Mitigation: Surface unreachable targets and truncation indicators, then narrow the query or raise limits before drawing operational conclusions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-monitor)
- [Project Homepage](https://github.com/vmware-skills/VMware-Monitor)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Health Summary Template](references/health-summary-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown summaries with inline shell commands, tabular operational results, JSON-compatible MCP data, and optional self-contained HTML snapshot files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only operational outputs; list-style tool results identify returned rows, limits, totals, truncation, and follow-up hints.]

## Skill Version(s):

1.11.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
