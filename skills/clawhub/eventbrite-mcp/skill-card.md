## Description:

Query eventbrite.com from a shell using curl for the documented Eventbrite token API and fpx for browser-bridged public event discovery/search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-focused Eventbrite users use this skill to compose read-only shell commands for tickets, orders, organization events, attendees, and public event discovery without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Eventbrite OAuth tokens, browser cookies, and returned order, attendee, or email data could expose private account information if logged or committed.

Mitigation: Keep tokens and cookies out of logs and repositories, treat outputs as private, and redact sensitive fields before sharing results.

Risk: Queries can access account, organization, order, and attendee data through the user's authorized Eventbrite session or token.

Mitigation: Run only narrowly scoped read-only commands for Eventbrite data the user is authorized to access.

Risk: Public event discovery depends on a signed-in browser bridge and may fail when the bridge is unpaired, blocked, or returning a non-JSON interstitial.

Mitigation: Confirm the fpx profile is paired, refresh a signed-in eventbrite.com tab when needed, and inspect the first response before building automation on a field.

## Reference(s):

- [Eventbrite documented API curl recipes](references/token-api.md)
- [Eventbrite discovery API fpx recipes](references/discovery-api.md)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/eventbrite-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON or jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Eventbrite query guidance; returned API data may include private account, order, attendee, and email information.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
