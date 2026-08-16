## Description:

OpsBuddy guides users through connecting a third-party MCP operations assistant that unifies monitoring platforms for asset discovery, health checks, log search, alert analysis, root-cause diagnosis, and remediation suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hatjs880328s](https://clawhub.ai/user/hatjs880328s)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations teams use OpsBuddy to connect a third-party operations monitoring service to OpenClaw, then ask natural-language questions about infrastructure health, assets, logs, alerts, and likely root causes. The skill is connection guidance only; users configure the service and credentials themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OpsBuddy requires an MCP token and configured monitoring-platform credentials.

Mitigation: Keep tokens out of chat, enter them only in the portal or MCP settings, and revoke and reapply immediately if a token is exposed.

Risk: Monitoring data and configured platform credentials transit through the third-party gateway at https://ywdz.lxiai.com/.

Mitigation: Confirm the data flow is acceptable for the organization before connecting platforms, and use read-only cloud or monitoring credentials where possible.

Risk: Operational diagnosis and remediation suggestions may be incomplete or incorrect for a production incident.

Mitigation: Review recommendations before acting on production systems and keep connected credentials read-only where possible.

## Reference(s):

- [OpsBuddy ClawHub Listing](https://clawhub.ai/hatjs880328s/skills/ospbuddy)
- [OpsBuddy Portal](https://ywdz.lxiai.com/)
- [Publisher Profile](https://clawhub.ai/user/hatjs880328s)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown text with JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-supplied OpsBuddy MCP token; the skill instructs users not to paste credentials into chat.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
