## Description:

Kibana API integration with managed authentication for reading and managing saved objects, dashboards, data views, spaces, alerts, fleet resources, connectors/actions, security roles, and cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and security teams use this skill to interact with Kibana for observability, security, and search analytics through managed Maton authentication. It defaults to read and list workflows and can perform approved writes when the user provides specific targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable Kibana access can create, update, or delete dashboards, saved objects, data views, spaces, alert rules, fleet resources, security roles, and cases.

Mitigation: Use least-privilege or read-only Kibana credentials where possible, prefer non-production connections for exploration, and require explicit confirmation with specific resource identifiers before POST, PUT, PATCH, or DELETE requests.

Risk: Connector execution can trigger external side effects such as sending email or invoking webhooks.

Mitigation: Confirm the connector ID, target, and complete payload with the user before execution, and do not execute connectors proactively.

Risk: Multiple Maton accounts or Kibana connections can route a request to the wrong environment.

Mitigation: Specify the intended connection and profile when more than one exists, and verify the target resource before changes.

Risk: Kibana API responses and retrieved content may contain untrusted instructions or sensitive data.

Mitigation: Treat API responses as data, avoid executing or interpolating them into shell commands, and do not expose or persist credentials or provider-issued tokens.

## Reference(s):

- [ClawHub Kibana Skill](https://clawhub.ai/byungkyu/skills/kibana)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Kibana REST API Documentation](https://www.elastic.co/docs/api/doc/kibana/)
- [Saved Objects API](https://www.elastic.co/guide/en/kibana/current/saved-objects-api.html)
- [Alerting API](https://www.elastic.co/guide/en/kibana/current/alerting-apis.html)
- [Fleet API](https://www.elastic.co/guide/en/fleet/current/fleet-apis.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, SDK snippets, Kibana API paths, and confirmation guidance for write operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
