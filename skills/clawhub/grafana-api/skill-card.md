## Description:

Grafana API integration with managed authentication for reading and managing dashboards, data sources, folders, annotations, teams, and alert-rule information through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect and manage Grafana monitoring assets through authenticated API calls. It is intended for read-first workflows and confirmed changes to dashboards, folders, data sources, annotations, teams, and related alert-rule information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic API passthrough can use the full permission set of the connected Grafana token, including high-impact changes beyond the documented surface.

Mitigation: Use a dedicated least-privilege or read-only Grafana token where possible, default to read and list calls, and confirm every write by exact resource id or name before execution.

Risk: Grafana writes can delete or alter dashboards, folders, data sources, annotations, teams, and access-affecting team configuration.

Mitigation: Retrieve the target first, describe the specific effect, and require explicit user approval before POST, PUT, PATCH, or DELETE operations.

Risk: API keys and provider-issued tokens can expose long-lived credentials if printed, logged, stored, or passed through the shell environment.

Mitigation: Prefer OAuth through the Maton CLI and the operating system credential store; do not print, persist, export, or inspect credentials, and avoid Admin tokens for routine use.

Risk: Data source records may include credential-adjacent configuration such as URLs, usernames, authentication modes, or secret-related fields.

Mitigation: Read data source details only when needed and return only the fields required for the user's task.

Risk: Multiple Maton accounts or Grafana connections can make the default target ambiguous.

Mitigation: Specify the intended profile or connection when more than one exists, especially before any write.

## Reference(s):

- [ClawHub Grafana Skill](https://clawhub.ai/byungkyu/skills/grafana-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Grafana HTTP API Documentation](https://grafana.com/docs/grafana/latest/developers/http_api/)
- [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)
- [Grafana Folder API](https://grafana.com/docs/grafana/latest/developers/http_api/folder/)
- [Grafana Data Source API](https://grafana.com/docs/grafana/latest/developers/http_api/data_source/)
- [Maton API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user approval before write operations.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
