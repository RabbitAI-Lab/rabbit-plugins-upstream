## Description:

Helps agents retrieve Eventbrite orders, tickets, organization events, attendees, and public event listings through read-only shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and event organizers use this skill to look up their Eventbrite orders, tickets, events, and attendees, or discover public events without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Eventbrite API tokens or browser-session cookies could be exposed.

Mitigation: Keep credentials out of logs and commits; prefer token-based access for scripts and grant browser-bridge access only when needed.

Risk: Order and attendee responses may contain private contact and ticket details.

Mitigation: Limit displayed fields and avoid logging raw attendee, order, email, or barcode values.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/eventbrite-mcp)
- [Token API recipes](artifact/references/token-api.md)
- [Event discovery recipes](artifact/references/discovery-api.md)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries; returned account and attendee data may be sensitive.]

## Skill Version(s):

1.1.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
