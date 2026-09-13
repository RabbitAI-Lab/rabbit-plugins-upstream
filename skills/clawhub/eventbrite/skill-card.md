## Description:

Eventbrite API integration with managed OAuth for managing events, venues, ticket classes, orders, and attendees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an Eventbrite account through Maton, inspect account data, and manage events, venues, ticket classes, orders, and attendees. It supports read/list workflows by default and requires explicit confirmation before writes, connection changes, or automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated Eventbrite access can expose event, order, attendee, venue, and ticket-class data from the connected account.

Mitigation: Install only if that access is acceptable, prefer OAuth over API keys, use least-privilege scopes where available, and start with read-only/list actions.

Risk: Write operations or automation can create, publish, change, delete, or forward Eventbrite-related data.

Mitigation: Require a separate explicit confirmation before publishing, changing, deleting, creating automation, or forwarding event data to any destination.

Risk: Long-lived API keys or raw response dumps can increase credential and personal-data exposure.

Mitigation: Use OAuth and the Maton CLI credential store where possible; avoid exposing API keys in environment variables, command lines, logs, or files.

## Reference(s):

- [ClawHub Eventbrite skill page](https://clawhub.ai/byungkyu/skills/eventbrite)
- [Maton homepage](https://maton.ai)
- [Eventbrite API Documentation](https://www.eventbrite.com/platform/api)
- [Eventbrite API basics](https://www.eventbrite.com/platform/docs/api-basics)
- [API Gateway skill](https://clawhub.ai/byungkyu/api-gateway)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash, HTTP, JSON, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Eventbrite connection.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
