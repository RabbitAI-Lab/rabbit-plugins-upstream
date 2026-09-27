## Description:

Guides read-only Eventbrite queries for tickets, orders, organizer events and attendees, and public event discovery from a shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Eventbrite users can retrieve their tickets and orders, inspect their organizations' events and attendees, and find public events using read-only shell recipes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries can expose private account data, including attendee records, orders, and email addresses.

Mitigation: Limit queries to needed data and avoid saving, logging, or sharing private results unless necessary.

Risk: An OAuth token or signed-in browser session gives the workflow access to Eventbrite account data.

Mitigation: Use only with an account and session you intend to grant access to; keep tokens and cookies private and out of logs.

## Reference(s):

- [Eventbrite MCP release](https://clawhub.ai/chrischall/skills/eventbrite-mcp)
- [Documented API recipes](artifact/references/token-api.md)
- [Event discovery recipes](artifact/references/discovery-api.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only requests; account queries require an OAuth token or an authorized browser session.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
