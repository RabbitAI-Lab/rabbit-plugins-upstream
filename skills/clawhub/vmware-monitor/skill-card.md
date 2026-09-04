## Description:

vmware-monitor gives agents read-only VMware vCenter and ESXi monitoring for inventory, health triage, alarms and events, performance and capacity checks, and VM, host, and datastore investigations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and VMware operators use this skill to ask agents for read-only VMware estate status, triage, and investigation output before deciding whether separate approved remediation is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires local access to VMware monitoring data and infrastructure credentials.

Mitigation: Use a least-privilege read-only vCenter or ESXi account, prefer a secret manager over storing passwords in .env when possible, and restrict local credential file permissions.

Risk: Optional recurring scans and webhooks can distribute operational alert summaries outside the local agent session.

Mitigation: Enable daemon scanning or webhook delivery only when recurring monitoring is intended, and send webhooks only to user-controlled destinations.

Risk: Disabling TLS verification can weaken protection for VMware API connections.

Mitigation: Keep TLS verification enabled in production and use CA-signed certificates for production vCenter or ESXi endpoints.

Risk: The artifact describes source-level read-only enforcement, but independent runtime safety still depends on the connected VMware account.

Mitigation: Review the source before production deployment and connect with a read-only VMware account so the platform enforces non-destructive access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-monitor)
- [Project homepage](https://github.com/vmware-skills/VMware-Monitor)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Health Summary Template](references/health-summary-template.md)
- [Investigation Protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose, CLI tables, JSON-style MCP results, and optional offline HTML snapshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only VMware inventory, alarm, event, performance, capacity, and investigation results; list responses may include pagination metadata.]

## Skill Version(s):

1.11.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
