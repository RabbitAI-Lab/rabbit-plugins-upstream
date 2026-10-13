## Description:

Helps agents search and investigate VMware Log Insight logs, identify volume spikes, and inspect fields and alerts without changing appliance data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure engineers and incident responders use this skill to investigate centralized VMware logs, spot log spikes, and review alert history during troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Log queries may expose sensitive operational data if credentials have excessive access.

Mitigation: Use a read-only Log Insight account with the minimum access needed.

Risk: Passwords stored in a local .env file are only obfuscated, not encrypted.

Mitigation: Inject passwords from a secret manager rather than storing them in .env; protect any local .env file with restrictive permissions.

Risk: Disabling TLS verification can expose appliance credentials and log data in transit.

Mitigation: Keep TLS verification enabled outside self-signed lab environments.

Risk: Installing an external package introduces software supply-chain exposure.

Mitigation: Review the uv/PyPI package source before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Publisher profile](https://clawhub.ai/user/zw008)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands]

**Output Format:** [Structured JSON query results and concise Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only log events, time-series aggregates and spikes, fields, and alert details; search results indicate when incomplete.]

## Skill Version(s):

1.9.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
