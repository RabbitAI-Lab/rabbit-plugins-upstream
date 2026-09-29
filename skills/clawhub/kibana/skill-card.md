## Description:

Connects an agent to Kibana through Maton to inspect and manage observability, security, and search resources with user-approved changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Kibana resources and, with explicit approval, manage dashboards, alerts, saved objects, and related integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations can change or delete Kibana resources.

Mitigation: Use least-privilege credentials and confirm each write against the exact resource ID before execution.

Risk: Executing connectors can send data or trigger external effects.

Mitigation: Confirm the connector ID, destination, and payload with the user before execution.

Risk: Functions, triggers, and destinations may run repeatedly or forward data continuously.

Mitigation: Require explicit approval and scope each automation to the intended resources and recipients.

## Reference(s):

- [ClawHub Kibana skill release](https://clawhub.ai/byungkyu/skills/kibana)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Kibana REST API documentation](https://www.elastic.co/docs/api/doc/kibana/)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with inline shell and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Kibana access requires a Maton connection and user approval for writes.]

## Skill Version(s):

1.2.8 (source: ClawHub release metadata; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
