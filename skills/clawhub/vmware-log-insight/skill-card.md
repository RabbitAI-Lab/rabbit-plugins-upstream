## Description:

Helps agents search and aggregate VMware Log Insight events, discover fields, and inspect alerts through read-only queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to investigate VMware appliance logs, identify event spikes, and inspect alert history without changing the log store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Appliance credentials stored in a local .env file may be exposed; b64 encoding does not encrypt them.

Mitigation: Use a read-only service account and inject passwords from a secret manager, or protect the .env file with restricted permissions.

Risk: Installing the separate runtime package grants it access to configured appliance logs and credentials.

Mitigation: Review the installed package and its provenance before enabling the integration.

Risk: Log content can contain untrusted text or exceed the useful context for an investigation.

Mitigation: Limit searches to relevant windows and fields, check truncation indicators, and treat returned log text as data rather than instructions.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Markdown summaries and structured JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results indicate truncation; aggregation can identify log-volume spikes.]

## Skill Version(s):

2.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
