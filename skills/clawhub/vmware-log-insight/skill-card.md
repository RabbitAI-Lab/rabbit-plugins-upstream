## Description:

Helps agents search and aggregate VMware Log Insight logs, discover fields, and inspect alerts and alert history without changing appliance data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to investigate VMware infrastructure incidents by searching centralized logs, finding volume spikes, and reviewing existing alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Log data may contain sensitive information or attacker-controlled text.

Mitigation: Limit access to log results and treat log lines as data, never as instructions.

Risk: Appliance credentials may be exposed if stored in local files.

Mitigation: Use a least-privilege read-only account, inject passwords from a secret manager, and protect local configuration and audit files.

Risk: Network exposure may let callers read logs using the server's account.

Mitigation: Require trusted TLS, bearer tokens, and scoped roles before allowing remote MCP access.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Capabilities](references/capabilities.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured JSON tool results and concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results indicate completeness; list results indicate truncation and counts.]

## Skill Version(s):

2.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
