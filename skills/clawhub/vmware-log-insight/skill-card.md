## Description:

Use this skill to search, aggregate, and investigate centralized VMware VCF Operations for Logs data through read-only log search, aggregation, field discovery, version, and alert-history queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect VMware log evidence during incident triage, find log-volume spikes, discover available log fields, and read alert definitions or alert history without changing the Log Insight appliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs credentials for a VMware Log Insight appliance, and local credential files can expose secrets if handled loosely.

Mitigation: Use a dedicated read-only Log Insight account, keep local credential and audit files private, and prefer secret-manager injection instead of storing passwords in .env.

Risk: Log lines are untrusted operational data and may contain instruction-shaped text or large volumes of irrelevant content.

Mitigation: Treat log output as data, bound searches with time windows and limits, report truncation explicitly, and rely on the documented sanitization and list-envelope behavior.

Risk: Network access to unintended appliances can broaden the operational data exposed to the agent.

Mitigation: Restrict the MCP server network path to the intended Log Insight appliances and keep TLS verification enabled except for controlled self-signed lab environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Capabilities](artifact/references/capabilities.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [CLI Reference](artifact/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured summaries, JSON-shaped tool results, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Log Insight query results may be bounded, truncated, or summarized according to tool limits and returned envelopes.]

## Skill Version(s):

1.8.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
