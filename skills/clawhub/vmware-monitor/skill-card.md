## Description:

VMware Monitor gives agents safe, read-only access to VMware vCenter and ESXi inventory, health, alarms, events, performance, capacity, and investigation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators, developers, and agents use this skill to inspect VMware environments, triage alarms, investigate VMs, hosts, and datastores, and prepare read-only operational summaries before any remediation is routed to companion skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive VMware inventory, alarm, event, log, and session data.

Mitigation: Use a dedicated least-privilege account and grant only the additional session or diagnostic-log privileges needed for the specific reads you intend to use.

Risk: Passwords may be supplied through local environment files if operators choose that setup path.

Mitigation: Prefer a secret manager or runtime environment injection instead of storing passwords in .env.

Risk: Optional Slack or Discord webhooks can receive infrastructure details from daemon scans.

Mitigation: Enable webhooks only for destinations approved to receive operational infrastructure data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-monitor)
- [Project homepage](https://github.com/vmware-skills/VMware-Monitor)
- [Setup Guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Health Summary Template](references/health-summary-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with optional CLI commands, configuration snippets, and structured tool-result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local HTML health snapshots only when the user requests HTML output.]

## Skill Version(s):

1.11.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
