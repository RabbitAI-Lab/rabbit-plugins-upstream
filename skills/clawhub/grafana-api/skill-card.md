## Description:

Grafana lets agents use managed Maton authentication to inspect and, with explicit approval, change Grafana dashboards, folders, data sources, annotations, teams, plugins, service-account inventory, and alerting configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and operations teams use this skill to work with Grafana observability resources through authenticated API calls. It supports read-first inspection workflows and write workflows only after explicit approval for the target resource and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform Grafana writes that change dashboards, folders, data sources, annotations, teams, and alerting configuration.

Mitigation: Default to read/list calls, use a least-privileged Grafana connection, and require explicit approval with exact resource identifiers before any POST, PUT, PATCH, or DELETE request.

Risk: Team operations and alerting or data-source changes can affect access, monitoring behavior, or credential-adjacent configuration.

Mitigation: Confirm the team, alert rule, folder, dashboard, or data source by id and name, summarize consequences, and avoid echoing full data-source configurations unless needed for the task.

Risk: Triggers and destinations can create persistent cross-service event forwarding.

Mitigation: Create or update destinations only after isolated approval that names the host, payload fields, persistence, and credential handling; prefer platform destinations and delete unused destinations.

Risk: Hosted functions run with the deploying Maton account authority and may process sensitive Grafana or event data.

Mitigation: Deploy only user-authored or user-reviewed handlers, use DENY_ALL network policy for Grafana tasks, disclose reachable connections before deploy or invocation, and delete functions when no longer needed.

Risk: Raw MATON_API_KEY workflows expose a long-lived credential to the environment.

Mitigation: Prefer OAuth through the Maton CLI and avoid exporting MATON_API_KEY except where the CLI cannot be installed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/grafana-api)
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
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with shell commands, JSON payload examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include proposed Grafana API requests and automation steps; write actions require explicit user approval before execution.]

## Skill Version(s):

1.2.4 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
