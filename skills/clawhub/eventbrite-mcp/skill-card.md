## Description:

Helps agents retrieve Eventbrite tickets, orders, organizer events and attendees, and discover public events using read-only requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Eventbrite users can look up their tickets and orders, review their organizations' events and attendees, and search for public events without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account tokens, browser cookies, and order or attendee details may be exposed in logs, commits, or shared transcripts.

Mitigation: Keep credentials and personal data out of logs, commits, and shared transcripts; give tools account access only when needed.

Risk: Improvised API calls could change organizer data despite the skill's read-only scope.

Mitigation: Use only the documented read-only recipes; do not add write calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/eventbrite-mcp)
- [Eventbrite token API recipes](references/token-api.md)
- [Eventbrite discovery recipes](references/discovery-api.md)
- [ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes; returned account data may include personal information.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
