## Description:

Query eventbrite.com from a shell for tickets, orders, organization events, attendees, and public event discovery using documented Eventbrite token API calls and browser-bridged fpx requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Eventbrite account, ticket, order, organization, attendee, and public event data from shell workflows without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive Eventbrite account, order, organization, attendee, token, cookie, and browser-bridge data to the agent.

Mitigation: Install only when that read access is acceptable, avoid logging or committing sensitive values and outputs, and keep tokens and cookies out of shared files.

Risk: The documented Eventbrite API supports write operations that are outside this skill's stated scope.

Mitigation: Use the recipes as read-only queries and do not improvise create, update, or other write calls from this skill.

## Reference(s):

- [Eventbrite documented API curl recipes](references/token-api.md)
- [Eventbrite discovery API fpx recipes](references/discovery-api.md)
- [Eventbrite API token setup](https://www.eventbrite.com/platform/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Eventbrite query recipes using curl, jq, and fpx]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
