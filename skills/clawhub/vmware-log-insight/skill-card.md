## Description:

Helps agents search and aggregate VMware Log Insight events, inspect log fields and alert history, and investigate log spikes without changing appliance data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to investigate VMware ESXi, vCenter, and VM logs, identify spikes, and review existing alert information through a configured Log Insight appliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Log access can expose sensitive operational data.

Mitigation: Use a least-privilege, read-only service account and limit queries to the investigation.

Risk: Credentials and local audit records require protection.

Mitigation: Inject passwords from a secret manager instead of storing them in .env, and protect local configuration and audit files.

Risk: Disabling TLS verification can expose appliance connections.

Mitigation: Keep TLS verification enabled except for controlled lab appliances.

Risk: Retrieved logs may contain untrusted instructions or excessive text.

Mitigation: Treat log lines as data, narrow search windows, and check truncation indicators before summarizing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Capabilities](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and structured JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries; check completion and truncation indicators before drawing conclusions.]

## Skill Version(s):

2.2.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
