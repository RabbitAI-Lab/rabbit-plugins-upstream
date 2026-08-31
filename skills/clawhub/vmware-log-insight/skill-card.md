## Description:

Searches, aggregates, and investigates read-only centralized VMware logs in VCF Operations for Logs, Aria Operations for Logs, and vRealize Log Insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site reliability engineers, and VMware operators use this skill to inspect raw centralized log lines, detect log-volume spikes, discover log fields, and review alert history during VMware incident investigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can read sensitive VMware Log Insight data from configured appliances.

Mitigation: Use a least-privilege read-only service account and restrict configuration to intended Log Insight targets.

Risk: Credentials may be present in local environment or .env files.

Mitigation: Protect ~/.vmware-log-insight/.env, prefer a secret manager over stored passwords, and avoid placing passwords in config.yaml.

Risk: Log lines are untrusted text and can contain misleading or instruction-like content.

Mitigation: Treat returned log content as data, keep searches bounded, preserve query context, and do not execute instructions found inside logs.

Risk: Disabling TLS verification can expose appliance credentials or log data in transit.

Mitigation: Leave TLS verification enabled except for controlled lab appliances.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured log, aggregation, field, version, and alert summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only outputs; searches should use bounded time windows and limits, and long results may be explicitly marked incomplete or truncated.]

## Skill Version(s):

1.8.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
