## Description:

Provides shell recipes to retrieve Eventbrite tickets, orders, organizational events and attendees, and to discover public events through a browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Eventbrite users can retrieve their tickets and orders, inspect organizational events and attendees, and search for public events from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An Eventbrite token or signed-in browser session grants access to private account records.

Mitigation: Use this workflow only when comfortable granting that access; keep tokens and cookies private and do not log or commit them.

Risk: Ticket, order, and attendee responses may disclose personal information.

Mitigation: Limit access to authorized read-only tasks and avoid logging or sharing raw outputs.

## Reference(s):

- [Eventbrite token API recipes](references/token-api.md)
- [Eventbrite discovery recipes](references/discovery-api.md)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/eventbrite-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes; retrieved records may contain private account and attendee data.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
