## Description:

Guides read-only Eventbrite account queries and public event discovery using a personal API token or a paired browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Eventbrite users can retrieve tickets, orders, organizer events and attendees, or discover public events through read-only shell recipes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell commands can expose an Eventbrite API token or browser-session cookies.

Mitigation: Keep credentials out of logs and commits, and pair the browser bridge only when comfortable granting session access.

Risk: Order and attendee queries can return personal or business data.

Mitigation: Limit access and sharing to authorized recipients, and handle exports as sensitive data.

## Reference(s):

- [Eventbrite token API recipes](references/token-api.md)
- [Eventbrite discovery recipes](references/discovery-api.md)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/eventbrite-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries; returned account and attendee data may be sensitive.]

## Skill Version(s):

1.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
