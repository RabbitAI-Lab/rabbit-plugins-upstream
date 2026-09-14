## Description:

Kibana API integration with managed authentication for reading and modifying Kibana resources such as saved objects, dashboards, data views, spaces, alerts, fleet resources, connectors/actions, security roles, and cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and security analysts use this skill to inspect Kibana resources, manage observability and security assets, and perform approved write actions through a Maton-authenticated Kibana connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or delete Kibana resources.

Mitigation: Default to read-only calls and require explicit approval with exact resource identifiers and payloads before any write.

Risk: Maton mediates access to the user's Kibana instance.

Mitigation: Use OAuth with least-privilege Kibana credentials and verify the intended connection before sending requests.

Risk: Connector execution can trigger external side effects such as emails or webhooks.

Mitigation: Confirm the connector ID, target, and payload with the user before execution.

Risk: Persistent functions, triggers, or destinations can continue moving data after setup.

Mitigation: Create automation only after user approval of the data flow and deletion path.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/kibana)
- [Maton Homepage](https://maton.ai)
- [Kibana REST API Documentation](https://www.elastic.co/docs/api/doc/kibana/)
- [Saved Objects API](https://www.elastic.co/guide/en/kibana/current/saved-objects-api.html)
- [Alerting API](https://www.elastic.co/guide/en/kibana/current/alerting-apis.html)
- [Fleet API](https://www.elastic.co/guide/en/fleet/current/fleet-apis.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should minimize raw Kibana data exposure and require explicit confirmation before write, connector, connection, function, or trigger actions.]

## Skill Version(s):

1.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
