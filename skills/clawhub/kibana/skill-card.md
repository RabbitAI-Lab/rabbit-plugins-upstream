## Description:

Connects an agent to Kibana to inspect and manage observability and security resources through a Maton-authenticated connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations or security teams use this skill to inspect Kibana dashboards, saved objects, alerts, and related resources, and to make approved changes or set up automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes or deletions can change Kibana resources and permissions.

Mitigation: Use least-privilege credentials, check the connection and resource identifiers, and confirm each change and payload with the user before execution.

Risk: Executing a connector can send data or trigger actions outside Kibana.

Mitigation: Confirm the connector ID, destination, and payload with the user before executing it.

Risk: Trigger destinations can continuously forward matching events to a third party.

Mitigation: Obtain separate approval for each destination and disclose the receiving URL and data sent before enabling forwarding.

Risk: Raw HTTP authentication can expose a long-lived API key.

Mitigation: Prefer the CLI's managed login; use an API key only when needed and never print, persist, or send it to other hosts.

## Reference(s):

- [Kibana skill release](https://clawhub.ai/byungkyu/skills/kibana)
- [Maton](https://maton.ai)
- [Kibana REST API documentation](https://www.elastic.co/docs/api/doc/kibana/)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown guidance with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read and list operations are preferred; changes and external actions require explicit approval.]

## Skill Version(s):

1.2.8 (source: server-resolved release metadata; skill frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
