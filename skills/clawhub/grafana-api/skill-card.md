## Description:

Grafana API integration with managed authentication for reading and managing dashboards, data sources, folders, annotations, teams, alert rules, and organization information through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect and manage Grafana observability resources through authenticated API calls. It is suited for monitoring workflows that need dashboard, folder, data source, annotation, team, alert rule, organization, or current-user access with explicit approval before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable API operations can change or delete dashboards, folders, data sources, annotations, teams, and related monitoring assets.

Mitigation: Use read-only calls first, require explicit approval before POST, PUT, PATCH, or DELETE requests, and include specific resource identifiers and intended effects before executing changes.

Risk: Broad Grafana permissions can make the connected account's privileges the effective permission boundary for the skill.

Mitigation: Use least-privilege Grafana access, prefer read-only scopes where possible, and revoke unused connections promptly.

Risk: Ambiguous Maton accounts or multiple Grafana connections can route changes to the wrong instance.

Mitigation: Specify the intended Maton profile and Grafana connection when more than one account or connection exists.

Risk: Data source changes, deletions, alert-rule changes, and team changes can affect monitoring coverage or access structure.

Mitigation: Review these operations with extra care, summarize consequences, and require confirmation with concrete dashboard, folder, data source, alert rule, or team identifiers.

## Reference(s):

- [Grafana HTTP API Documentation](https://grafana.com/docs/grafana/latest/developers/http_api/)
- [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)
- [Grafana Folder API](https://grafana.com/docs/grafana/latest/developers/http_api/folder/)
- [Grafana Data Source API](https://grafana.com/docs/grafana/latest/developers/http_api/data_source/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/grafana-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API endpoint guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue read or write API calls through Maton after authentication; write operations require explicit user approval and specific resource identifiers.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
