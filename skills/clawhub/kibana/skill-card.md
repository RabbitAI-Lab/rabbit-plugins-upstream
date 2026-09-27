## Description:

Kibana API integration with managed authentication for reading, creating, updating, and deleting Kibana resources through Maton-mediated connections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and security or observability teams use this skill to inspect and manage Kibana saved objects, dashboards, data views, spaces, alerts, fleet resources, connectors, roles, and cases through an authenticated Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write-capable Kibana operations, including create, update, and delete actions on saved objects, dashboards, data views, spaces, alerts, fleet resources, security roles, and cases.

Mitigation: Use least-privilege Kibana credentials, default to read/list operations, and require explicit user approval with exact resource identifiers before any write.

Risk: Kibana connector execution can cause external side effects such as sending messages, opening tickets, paging people, invoking webhooks, or writing downstream data.

Mitigation: Read the connector first, then confirm the connector ID, target, payload, and intended effect with the user before execution.

Risk: Hosted functions, triggers, and destinations can keep running after setup and may create persistent data flows.

Mitigation: Review each function, trigger, destination host, payload, and persistence behavior separately; prefer Maton-controlled destinations and remove automation when it is no longer needed.

Risk: Long-lived API keys and raw HTTP fallback increase credential exposure risk.

Mitigation: Prefer OAuth with operating-system credential storage, avoid exporting or logging credentials, and rotate any key that was printed, committed, or pasted.

Risk: Kibana and trigger responses may contain business data, personal data, credentials, financial details, or private communications.

Mitigation: Extract only fields needed for the task and avoid dumping raw responses into logs, files, or destinations the user has not approved.

## Reference(s):

- [Kibana Skill on ClawHub](https://clawhub.ai/byungkyu/skills/kibana)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Kibana REST API Documentation](https://www.elastic.co/docs/api/doc/kibana/)
- [Saved Objects API](https://www.elastic.co/guide/en/kibana/current/saved-objects-api.html)
- [Alerting API](https://www.elastic.co/guide/en/kibana/current/alerting-apis.html)
- [Fleet API](https://www.elastic.co/guide/en/fleet/current/fleet-apis.html)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces task guidance and commands for authenticated Kibana API access through Maton; write operations, connector execution, connection creation, and automation require explicit user approval.]

## Skill Version(s):

1.2.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
