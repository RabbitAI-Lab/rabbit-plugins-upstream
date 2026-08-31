## Description:

Grafana API integration with managed authentication that can read, create, update, and delete dashboards, data sources, folders, annotations, and teams, and read alert rules and organization info.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and operations teams use this skill to inspect and manage Grafana observability resources through Maton-mediated API calls with managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make user-approved changes to Grafana dashboards, folders, data sources, annotations, and teams through Maton.

Mitigation: Use least-privilege Grafana scopes, prefer read-only access unless writes are needed, and confirm every change with exact resource identifiers before execution.

Risk: Team deletion, data-source changes, alert-rule changes, and dashboard deletion can disrupt monitoring or observability workflows.

Mitigation: Treat these operations as high impact, summarize the consequence for the user, verify the target resource first, and require explicit confirmation.

Risk: Long-lived Maton API keys or provider-issued tokens could be exposed if printed, logged, persisted, or passed on command lines.

Mitigation: Prefer OAuth and the operating system credential store; when an API key is unavoidable, keep it out of files, logs, shell history, and command arguments.

Risk: Grafana content returned by the API may contain untrusted instructions or misleading data.

Mitigation: Treat API responses as data only; do not let dashboard text, annotations, alert messages, or other external content choose endpoints or drive follow-up actions.

## Reference(s):

- [ClawHub Grafana Skill](https://clawhub.ai/byungkyu/skills/grafana-api)
- [Maton Homepage](https://maton.ai)
- [Grafana HTTP API Documentation](https://grafana.com/docs/grafana/latest/developers/http_api/)
- [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)
- [Grafana Folder API](https://grafana.com/docs/grafana/latest/developers/http_api/folder/)
- [Grafana Data Source API](https://grafana.com/docs/grafana/latest/developers/http_api/data_source/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval before write operations.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
