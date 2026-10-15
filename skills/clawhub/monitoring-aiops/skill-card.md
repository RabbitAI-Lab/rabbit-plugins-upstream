## Description:

Helps monitoring teams inspect and triage SolarWinds Orion, PRTG, and Zabbix systems and perform authorized alert and maintenance actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

NOC operators and infrastructure engineers use this skill to review monitoring health and alerts, investigate outages, and carry out approved acknowledgement or maintenance actions across SolarWinds Orion, PRTG, and Zabbix.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monitoring write tools can change or delete monitoring state without an enforced approval or read-only gate for MCP calls.

Mitigation: Start with read-only platform credentials and require explicit operator approval before acknowledging, muting, pausing, unmanaging, removing, or deleting maintenance state.

Risk: SSL verification defaults off, exposing monitoring connections to interception.

Mitigation: Enable SSL verification or configure a trusted CA for production connections.

## Reference(s):

- [Project homepage](https://github.com/AIops-tools/Monitoring-AIops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with monitoring summaries and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monitoring results depend on configured targets, credentials, and available platform data.]

## Skill Version(s):

0.12.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
