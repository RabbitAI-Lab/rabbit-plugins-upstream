## Description:

VMware Log Insight lets an agent search, aggregate, and inspect read-only log and alert data from VMware VCF Operations for Logs, formerly Aria Operations for Logs or vRealize Log Insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and incident responders use this skill to query centralized VMware log data, inspect alerts, discover fields, and identify log spikes during troubleshooting. It is intended for read-only investigation of configured Log Insight appliances, not for changing alerts or ingesting logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured Log Insight credentials may expose appliance access if stored insecurely.

Mitigation: Use a read-only service account, inject secrets from a secret manager in production, and restrict local secret files to the minimum required permissions.

Risk: Returned log contents may contain sensitive operational data or instruction-shaped text.

Mitigation: Bound searches by time and limit, treat log lines as data, and avoid acting on instructions found in returned logs.

Risk: Disabling TLS verification can expose credentials and log data in transit.

Mitigation: Keep TLS verification enabled except for controlled lab appliances.

## Reference(s):

- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-log-insight)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and JSON-shaped tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only MCP and CLI workflows; results can include bounded log events, aggregate bins, field lists, appliance version data, and alert metadata.]

## Skill Version(s):

1.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
