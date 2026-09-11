## Description:

VMware Monitor provides read-only VMware vCenter/ESXi monitoring for cluster health, object investigations, inventory, alarms, events, and VM details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and infrastructure operators use this skill to query VMware environments, triage cluster and object health, inspect alarms and events, and prepare read-only monitoring summaries before any remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and relies on an external vmware-monitor executable and dependencies that handle VMware credentials and infrastructure data.

Mitigation: Pin a reviewed package version or commit where possible, review the upstream source before production use, and deploy with a dedicated read-only VMware service account.

Risk: Configuration may place VMware target passwords in a local .env file.

Mitigation: Prefer secret-manager injection for production credentials; when .env is used, restrict file permissions and treat password obfuscation as protection against casual disclosure only.

Risk: Disabling TLS verification or enabling webhook alerts can expose monitoring data or weaken connection assurance.

Mitigation: Keep TLS verification enabled in production and review daemon/webhook destinations and payload scope before enabling scheduled notifications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-monitor)
- [Project homepage](https://github.com/vmware-skills/VMware-Monitor)
- [Setup Guide](references/setup-guide.md)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Health Summary Template](references/health-summary-template.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional structured CLI or MCP results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide generation of local offline HTML snapshots through vmware-monitor commands; no public artifact is uploaded by the skill.]

## Skill Version(s):

1.11.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
