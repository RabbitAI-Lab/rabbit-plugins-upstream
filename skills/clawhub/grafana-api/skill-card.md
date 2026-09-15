## Description:

Grafana provides managed-authentication API access for reading and, with explicit approval, creating, updating, or deleting dashboards, data sources, folders, annotations, teams, and selected alerting resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and observability teams use this skill to inspect Grafana resources, manage dashboards and related objects, and set up approved Grafana-backed automation through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact Grafana writes can change or delete dashboards, data sources, folders, annotations, teams, or alerting resources.

Mitigation: Use read/list calls first, identify the exact target resource, describe the intended effect, and wait for explicit user confirmation before any POST, PUT, PATCH, or DELETE.

Risk: The connected Grafana credential may carry broad permissions in the selected instance.

Mitigation: Use least-privilege Grafana credentials, prefer read-only scopes when possible, specify the intended connection, and revoke unused connections promptly.

Risk: Long-lived API keys and raw responses can expose credentials or sensitive observability data.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or storing tokens, and return only the response fields needed for the task.

Risk: Hosted functions or trigger destinations can create persistent automation or data forwarding.

Mitigation: Create or update automation only after separate approval that names the function, destination host, data fields, frequency, and persistence.

## Reference(s):

- [Grafana HTTP API Documentation](https://grafana.com/docs/grafana/latest/developers/http_api/)
- [Dashboard API](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)
- [Folder API](https://grafana.com/docs/grafana/latest/developers/http_api/folder/)
- [Data Source API](https://grafana.com/docs/grafana/latest/developers/http_api/data_source/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
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

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with shell commands, code blocks, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should default to read/list guidance and require explicit user confirmation before writes, new connections, or hosted automation.]

## Skill Version(s):

1.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
