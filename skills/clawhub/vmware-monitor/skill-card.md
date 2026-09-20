## Description:

vmware-monitor helps agents perform safe, read-only VMware vCenter/ESXi monitoring, health triage, inventory lookup, alarm and event review, and object-centered investigations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT operations teams, and site reliability engineers use this skill to query VMware vCenter and ESXi environments, summarize infrastructure health, inspect inventory, investigate alarms and events, and route remediation to separate write-capable VMware skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive VMware inventory, alarms, events, logs, and session data from production infrastructure.

Mitigation: Use a dedicated VMware account with the built-in Read-Only role and review the upstream package source before production use.

Risk: Local configuration can include VMware passwords and optional webhook URLs.

Mitigation: Prefer a secret manager over storing passwords in .env, keep file permissions restricted, and keep webhook URLs private.

Risk: Optional session and host-log reads may require privileges beyond the standard Read-Only role.

Mitigation: Grant Sessions.TerminateSession or Global.Diagnostics only when those specific reads are required.

Risk: Optional webhook monitoring can send operational hostnames, IP addresses, usernames, and issue details to the configured endpoint.

Mitigation: Use trusted HTTPS webhook destinations and treat those destinations as receiving operational data.

## Reference(s):

- [VMware Monitor source repository](https://github.com/vmware-skills/VMware-Monitor)
- [Read-only enforcement test](https://github.com/vmware-skills/VMware-Monitor/blob/main/tests/eval/regression/test_read_only_enforcement.py)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Cluster Health Summary Display Template](references/health-summary-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured tool output summaries with inline CLI commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May also create local audit logs, configuration files, and optional offline HTML health snapshots when the user runs the documented commands.]

## Skill Version(s):

1.15.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
