## Description:

Provides shell recipes to query Eventbrite tickets, orders, organizer events and attendees, and discover public events through a browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and event organizers use these recipes to read their Eventbrite tickets, orders, events and attendee details, or search public events from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge has Eventbrite site access and can use a signed-in session.

Mitigation: Install and pair the bridge only if comfortable granting it Eventbrite site access; use the skill's read-only recipes.

Risk: Orders and attendee results can expose names and email addresses; tokens and cookies grant account access.

Mitigation: Keep results private and avoid logging or committing tokens, cookies, and attendee data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/eventbrite-mcp)
- [Eventbrite token API recipes](references/token-api.md)
- [Eventbrite discovery recipes](references/discovery-api.md)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)
- [ContextMint Bridge source and releases](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell examples and JSON query recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes; returned results may contain private attendee and account data.]

## Skill Version(s):

1.1.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
