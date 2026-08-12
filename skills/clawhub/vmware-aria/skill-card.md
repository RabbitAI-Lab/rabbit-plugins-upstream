## Description:

vmware-aria helps agents query VMware Aria Operations and VCF Operations data for metrics, alerts, capacity forecasts, anomalies, reports, platform health, and fleet diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators, VMware administrators, and SRE teams use this skill to inspect Aria Operations data, triage alerts, plan capacity, generate reports, and prepare operational recommendations. It is suited for local CLI and MCP-based agent workflows that need monitored infrastructure evidence before taking action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Aria Operations credentials and local configuration files.

Mitigation: Confirm the package source before installation, use least-privileged Aria service accounts, keep `.env` permissions at 600, and prefer a secret manager for production credentials.

Risk: Some tools can change alert state, alert definitions, or generated reports.

Mitigation: Reserve PowerUser-style credentials for authorized users only, require explicit approval for write actions, and review audit logs for write operations.

Risk: Operational summaries can be misleading if list results are truncated or if alert/resource identifiers are confused.

Mitigation: Check result envelopes for truncation, preserve returned enum values, and use the documented investigation flow before reporting root cause or recommended action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aria)
- [VMware Aria source homepage](https://github.com/vmware-skills/VMware-Aria)
- [Setup Guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented operational summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI commands, MCP tool guidance, report links, capacity forecasts, alert summaries, and configuration steps.]

## Skill Version(s):

1.8.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
