## Description:

Connects an agent to Systeme.io to manage contacts, tags, course enrolments, community memberships, subscriptions, and approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Users and teams managing a Systeme.io account can ask an agent to look up and update contacts, tags, course or community access, and subscriptions, or set up approved webhooks and automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes can change contact data, course or community access, and subscription state.

Mitigation: Default to read-only requests; confirm the account, connection, target record, payload, and effect before each write.

Risk: Webhooks and automations can persistently forward customer or event data to a destination.

Mitigation: Approve each webhook, function, or trigger only after checking the destination host, owner, event scope, and data it will receive.

## Reference(s):

- [ClawHub Systeme.io skill](https://clawhub.ai/byungkyu/skills/systeme)
- [Maton homepage](https://maton.ai)
- [Systeme.io API Reference](https://developer.systeme.io/reference)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Scheduled trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API actions require an authorized Systeme.io connection.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
