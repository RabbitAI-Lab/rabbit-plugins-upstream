## Description:

Helps agents use Eventbrite through a managed Maton connection to view and manage events, venues, tickets, orders, and attendees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Event organizers and developers use this skill to query Eventbrite accounts and manage events, venues, ticket classes, orders, and attendees through an authorized Maton connection. It also guides approved scheduled or cross-app automation of Eventbrite actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Eventbrite writes can change or delete event and attendee data.

Mitigation: Confirm the target and intended effect before each write.

Risk: API keys or broad account connections can expose sensitive access.

Mitigation: Prefer OAuth, limit access to needed accounts, and revoke unused connections.

Risk: Automations and trigger destinations can continue acting on or forwarding events without further approval.

Mitigation: Confirm each automation and destination separately, use trusted hosts, and remove unused triggers.

## Reference(s):

- [Eventbrite skill on ClawHub](https://clawhub.ai/byungkyu/skills/eventbrite)
- [Eventbrite API documentation](https://www.eventbrite.com/platform/api)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with shell commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require a user-authorized Maton connection.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
