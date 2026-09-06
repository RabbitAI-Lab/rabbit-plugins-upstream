## Description:

Kibana API integration with managed authentication for reading and managing saved objects, dashboards, data views, spaces, alerts, fleet resources, connectors/actions, security roles, and cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, security analysts, and operations teams use this skill to inspect and administer Kibana resources through Maton-managed authentication. It is suited for observability, security, and search analytics workflows where agents need to list resources, retrieve details, and perform confirmed changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or delete Kibana resources such as dashboards, data views, spaces, alerting rules, fleet resources, roles, and cases.

Mitigation: Default to read and list operations; require explicit user approval with specific resource identifiers, payload, and intended effect before any POST, PUT, PATCH, or DELETE.

Risk: Connector execution can trigger external side effects such as email, webhook, or chat actions.

Mitigation: Confirm the connector ID, action type, target, and full payload with the user before execution.

Risk: Authentication can involve OAuth credentials or a long-lived Maton API key.

Mitigation: Prefer OAuth, avoid printing or persisting credentials, send API keys only to api.maton.ai, and isolate or pin CLI and SDK installations where practical.

Risk: Exploratory use against production Kibana may affect monitoring, alerting, or access control.

Mitigation: Use least-privilege and preferably non-production Kibana permissions for exploratory work, and specify the intended Maton profile and connection when multiple accounts or connections exist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/kibana)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Kibana REST API Documentation](https://www.elastic.co/docs/api/doc/kibana/)
- [Saved Objects API](https://www.elastic.co/guide/en/kibana/current/saved-objects-api.html)
- [Alerting API](https://www.elastic.co/guide/en/kibana/current/alerting-apis.html)
- [Fleet API](https://www.elastic.co/guide/en/fleet/current/fleet-apis.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Kibana API requests through the Maton CLI or SDK; state-changing operations require explicit confirmation.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
