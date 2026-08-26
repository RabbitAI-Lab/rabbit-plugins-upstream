## Description:

Grafana API integration with managed authentication for reading and modifying dashboards, data sources, folders, annotations, alerts, and teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Grafana monitoring, visualization, and observability resources through Maton-managed authentication. It supports read-first workflows and write operations when the user explicitly confirms the target and intended change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can reach a broad set of Grafana API endpoints, including service-account inventory beyond its stated scope.

Mitigation: Use a least-privilege Grafana connection, prefer read-only scopes for exploration, and avoid accounts that can enumerate or administer service accounts unless the task requires that access.

Risk: Write-capable Grafana operations can change or delete dashboards, data sources, folders, annotations, alerts, and teams.

Mitigation: Require explicit user confirmation for each write with the specific resource identifier, payload, and intended effect before running POST, PUT, PATCH, or DELETE requests.

## Reference(s):

- [Grafana HTTP API Documentation](https://grafana.com/docs/grafana/latest/developers/http_api/)
- [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)
- [Grafana Folder API](https://grafana.com/docs/grafana/latest/developers/http_api/folder/)
- [Grafana Data Source API](https://grafana.com/docs/grafana/latest/developers/http_api/data_source/)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/grafana-api)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton CLI or SDK calls against a user-authorized Grafana connection; write operations require explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
