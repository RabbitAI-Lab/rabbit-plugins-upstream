## Description:

Query eventbrite.com from a shell for tickets, orders, organization events, attendees, and public event discovery using the documented token API and an fpx browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to compose read-only shell commands for Eventbrite account, organizer, attendee, order, and public discovery data without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose Eventbrite tokens, browser-session cookies, attendee emails, order details, and exported responses.

Mitigation: Use it for narrow read-only tasks, avoid broad attendee or order dumps unless necessary, and do not log, commit, or share tokens, cookies, attendee emails, order details, or exported responses.

Risk: The fpx browser bridge may use a signed-in Eventbrite browser session to access account data.

Mitigation: Install only if comfortable granting the agent access to the Eventbrite token or signed-in browser session, and keep usage scoped to read-only queries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/eventbrite-mcp)
- [Eventbrite documented API recipes](references/token-api.md)
- [Eventbrite discovery API fpx recipes](references/discovery-api.md)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Eventbrite command recipes using curl, jq, and fpx.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
