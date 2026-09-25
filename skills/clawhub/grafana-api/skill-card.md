## Description:

Grafana provides managed-authentication access to dashboards, folders, data sources, annotations, teams, alert rules, plugins, and organization or user information, with write operations requiring explicit confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and observability operators use this skill to inspect and manage Grafana resources through Maton-managed authentication. It is suited for read/list workflows by default and for confirmed writes or automation involving dashboards, folders, data sources, annotations, teams, and alerting configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable Grafana operations can modify or delete dashboards, folders, data sources, annotations, teams, and alerting configuration.

Mitigation: Use least-privilege Grafana credentials and require explicit user confirmation with exact resource IDs before any write or automation.

Risk: Long-lived Maton API keys can be exposed through logs, shell history, child processes, or pasted output when raw HTTP access is used.

Mitigation: Prefer OAuth through the Maton CLI and operating-system credential store; if an API key is required, do not print, persist, or pass it on a command line, and rotate it if exposed.

Risk: Automation triggers and hosted functions can forward operational data outside the intended Grafana workflow.

Mitigation: Avoid forwarding trigger data to third-party URLs unless necessary, deploy Grafana functions with deny-all outbound networking when possible, and remove unused connections, functions, triggers, and destinations.

## Reference(s):

- [ClawHub Grafana Skill](https://clawhub.ai/byungkyu/skills/grafana-api)
- [byungkyu ClawHub Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Grafana HTTP API Documentation](https://grafana.com/docs/grafana/latest/developers/http_api/)
- [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)
- [Grafana Folder API](https://grafana.com/docs/grafana/latest/developers/http_api/folder/)
- [Grafana Data Source API](https://grafana.com/docs/grafana/latest/developers/http_api/data_source/)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authenticated Grafana API calls, Maton CLI commands, SDK examples, and safety guidance for write-capable operations.]

## Skill Version(s):

1.2.8 (source: server release evidence; artifact frontmatter version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
