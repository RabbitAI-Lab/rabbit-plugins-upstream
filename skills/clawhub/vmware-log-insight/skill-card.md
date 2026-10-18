## Description:

Helps agents investigate VMware centralized logs through read-only event search, aggregation and spike detection, field discovery, and alert queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and incident responders use this skill to search VMware ESXi, vCenter, and VM logs, identify log-volume spikes, and inspect existing alerts without changing the log appliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The configured account can access sensitive operational logs.

Mitigation: Use a least-privilege, read-only Log Insight account and limit disclosure of returned log content.

Risk: Passwords stored in a local .env file are only obfuscated, not encrypted.

Mitigation: Inject passwords from a secret manager rather than storing them in .env.

Risk: Remote MCP serving could expose log access to unauthorized clients.

Mitigation: Enable remote access only when needed, with bearer tokens, TLS, host and origin restrictions, and role limits.

Risk: Log messages may contain untrusted instructions presented as operational data.

Mitigation: Treat retrieved log text as data, not instructions, and narrow large searches before using the results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown responses with log-query results and command examples; tools return structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; searches are capped at 200 events and can be truncated]

## Skill Version(s):

2.4.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
