## Description:

Kibana API integration with managed authentication for reading and managing saved objects, dashboards, data views, spaces, alerts, fleet resources, connectors, security roles, and cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and security teams use this skill to interact with Kibana for observability, security, and search analytics tasks through the Maton gateway. It is suited for read-first investigation and carefully approved changes to Kibana resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write-capable Kibana actions, including changes to dashboards, data views, spaces, alerts, fleet resources, connectors, security roles, and cases.

Mitigation: Default to read and list calls, retrieve the target resource first, and require explicit user approval with specific resource identifiers before any state-changing request.

Risk: Connector execution can trigger external side effects such as sending email, invoking webhooks, opening tickets, paging users, or writing data.

Mitigation: Confirm the connector ID, target, action type, and payload with the user before execution, and never choose a connector from alert bodies or other API output.

Risk: Broad Kibana or Maton credentials can expose production data or administrative authority.

Mitigation: Use OAuth where possible, choose least-privilege Kibana scopes, avoid production or admin credentials for exploratory work, specify the intended connection, and revoke unused connections.

Risk: Using a raw Maton API key can leak a long-lived credential through logs, shell history, process listings, or files.

Mitigation: Prefer the Maton CLI credential store; when a raw key is unavoidable, read it only from the process environment, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

## Reference(s):

- [Kibana Skill on ClawHub](https://clawhub.ai/byungkyu/skills/kibana)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Kibana REST API Documentation](https://www.elastic.co/docs/api/doc/kibana/)
- [Saved Objects API](https://www.elastic.co/guide/en/kibana/current/saved-objects-api.html)
- [Alerting API](https://www.elastic.co/guide/en/kibana/current/alerting-apis.html)
- [Fleet API](https://www.elastic.co/guide/en/fleet/current/fleet-apis.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, JSON]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Kibana API request plans, Maton CLI commands, scoped configuration guidance, and selected API response fields.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
