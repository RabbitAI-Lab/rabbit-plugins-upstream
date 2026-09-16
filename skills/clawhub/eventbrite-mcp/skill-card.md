## Description:

Query eventbrite.com from a shell for tickets, orders, organization events, attendees, and public event discovery using Eventbrite API calls and an fpx browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compose read-only shell commands for Eventbrite account, organizer, attendee, event detail, and public discovery workflows. It is suited to one-shot queries and scripts that need Eventbrite data without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Eventbrite account, ticket, order, organization, and attendee data through a personal token or signed-in browser session.

Mitigation: Use the documented token API when possible, keep tokens and cookies out of logs and commits, and limit browser bridge access to eventbrite.com.

Risk: Shell output may contain personal data such as attendee names, emails, tickets, orders, or organization records.

Mitigation: Filter command output to the minimum needed fields and avoid storing raw responses in shared files or persistent logs.

Risk: The fpx browser bridge adds a third-party dependency and may expose signed-in Eventbrite session data to local tooling.

Mitigation: Review and pin @fetchproxy/cli before global installation, pair it only with the intended Eventbrite profile, and prefer token-based curl workflows for scripts.

## Reference(s):

- [Eventbrite Skill on ClawHub](https://clawhub.ai/chrischall/skills/eventbrite-mcp)
- [Eventbrite Documented API Recipes](references/token-api.md)
- [Eventbrite Discovery API Recipes](references/discovery-api.md)
- [Eventbrite API Keys](https://www.eventbrite.com/platform/api-keys)
- [Eventbrite API v3](https://www.eventbriteapi.com/v3)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Eventbrite recipes intended for curl, jq, and fpx workflows.]

## Skill Version(s):

0.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
