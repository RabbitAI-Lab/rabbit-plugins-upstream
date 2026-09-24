## Description:

Query Eventbrite from a shell for tickets, orders, organization events, attendees, and public event discovery using curl or a signed-in browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and event organizers use this skill to compose read-only Eventbrite shell commands for account data, event details, attendee lists, orders, and public event search without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Eventbrite tokens, browser-session cookies, order details, attendee records, and email addresses can expose private account or event information.

Mitigation: Use the recipes only with authorized accounts, organizations, and events; avoid logging, sharing, or committing tokens, cookies, and API output.

Risk: The browser bridge depends on a signed-in Eventbrite browser session and Chrome site access through the Transporter extension.

Mitigation: Pair only a trusted browser profile, keep browser access scoped to Eventbrite, and review generated shell commands before running them.

## Reference(s):

- [Eventbrite documented API recipes](references/token-api.md)
- [Eventbrite discovery API recipes](references/discovery-api.md)
- [Eventbrite API token setup](https://www.eventbrite.com/platform/api-keys)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/eventbrite-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes; command output may include JSON containing private Eventbrite account, order, attendee, email, token, or cookie data.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
