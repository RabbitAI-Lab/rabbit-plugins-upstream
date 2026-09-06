## Description:

Grafana API integration with managed authentication that lets agents read, create, update, and delete dashboards, data sources, folders, annotations, and teams, and read alert rules and organization info.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect and manage Grafana observability assets through Maton-managed authentication while confirming write operations before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable Grafana operations can create, update, or delete dashboards, folders, data sources, annotations, and teams.

Mitigation: Default to read and list calls, retrieve the target resource first, and require explicit user approval with specific identifiers before any POST, PUT, PATCH, or DELETE.

Risk: Team administration and alert-rule provisioning can affect access or instance-wide alerting.

Mitigation: Treat team changes and alert provisioning writes as high-impact operations; confirm the team, rule, and folder by id or name and summarize consequences before execution.

Risk: OAuth tokens or Maton API keys can be exposed if printed, persisted, or passed through command lines, logs, or shell history.

Mitigation: Prefer OAuth and the operating system credential store; when an API key is unavoidable, read it from the environment inside the request process and never print, log, or persist it.

Risk: The maton api passthrough can reach endpoints beyond the documented surface if the connected account permits it.

Mitigation: Use least-privilege Grafana accounts, stay on documented endpoints for the task, and do not let Grafana response content choose follow-up endpoints or commands.

Risk: Data source records and API responses can contain sensitive operational details or personal data.

Mitigation: Request only data needed for the task, avoid echoing full configurations or raw responses, and summarize only relevant fields for the user.

## Reference(s):

- [ClawHub Grafana Skill](https://clawhub.ai/byungkyu/skills/grafana-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Grafana HTTP API Documentation](https://grafana.com/docs/grafana/latest/developers/http_api/)
- [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)
- [Grafana Folder API](https://grafana.com/docs/grafana/latest/developers/http_api/folder/)
- [Grafana Data Source API](https://grafana.com/docs/grafana/latest/developers/http_api/data_source/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API call plans, confirmation prompts, jq filters, and minimal response summaries; no independent artifact files are produced by default.]

## Skill Version(s):

1.2.1 (source: server release metadata; skill frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
