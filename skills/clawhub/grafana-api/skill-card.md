## Description:

Helps agents use an authorized Grafana connection to inspect and manage dashboards, folders, data sources, annotations, and teams, with user approval before changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Grafana monitoring resources and, with explicit approval, manage dashboards, folders, data sources, annotations, and teams. It also describes optional scheduled or event-driven workflows through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad raw API path can reach high-impact Grafana endpoints beyond the documented workflows.

Mitigation: Use a least-privilege Grafana account, avoid admin tokens, and review each requested endpoint and operation before execution.

Risk: Writes to teams, data sources, dashboards, folders, or alert provisioning can affect access and monitoring.

Mitigation: Identify the target resource and consequences, then require explicit user confirmation before each POST, PUT, PATCH, or DELETE.

Risk: Service-account token inventory and data source details may expose sensitive information; automation destinations can disclose data.

Mitigation: Limit reads and returned fields to the task; do not disclose tokens or embed credentials in functions, triggers, or destinations.

## Reference(s):

- [ClawHub Grafana skill release](https://clawhub.ai/byungkyu/skills/grafana-api)
- [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/developers/http_api/)
- [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)
- [Grafana Data Source API](https://grafana.com/docs/grafana/latest/developers/http_api/data_source/)
- [Maton API documentation](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown guidance and commands; Grafana API responses in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authorized Grafana connection and explicit approval for writes.]

## Skill Version(s):

1.2.10 (source: ClawHub release metadata; artifact frontmatter: 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
