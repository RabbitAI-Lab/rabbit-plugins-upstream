## Description:

VMware Monitor gives agents read-only VMware vCenter and ESXi visibility for inventory, alarms, events, performance, capacity, and object-centered health investigations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and infrastructure operators use this skill to inspect VMware environments, triage health issues, and gather evidence before handing any remediation to companion write-capable tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool requires read access to VMware inventory, alarms, events, performance, and capacity data.

Mitigation: Use a least-privilege vSphere account scoped to the environments the agent is allowed to inspect.

Risk: The configuration uses a local .env file for VMware target secrets.

Mitigation: Protect the .env file with restrictive permissions or inject credentials from a secret manager at runtime.

Risk: Disabling TLS verification can expose monitoring sessions to interception.

Mitigation: Keep TLS verification enabled in production and reserve certificate-validation bypasses for intentional isolated lab use.

Risk: Scheduled monitoring and webhooks can send operational alert metadata outside the local machine.

Mitigation: Start the daemon and configure Slack, Discord, or other webhook URLs only when scheduled alerts are intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-monitor)
- [VMware Monitor Homepage](https://github.com/vmware-skills/VMware-Monitor)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Health Summary Template](references/health-summary-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, structured text, CLI commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce offline HTML snapshot commands and read-only monitoring summaries; results depend on configured VMware targets and credentials.]

## Skill Version(s):

1.8.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
