## Description:

Query Eventbrite data from a shell, including user tickets and orders, organizer events and attendees through the documented token API, and public event discovery through a browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compose read-only Eventbrite shell workflows for account, organizer, event, attendee, ticket, and public discovery data without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose Eventbrite account data, tickets, organizer data, and attendee names or emails to the agent and command output.

Mitigation: Use it only where that read access is acceptable, and avoid writing sensitive command output to shared files, logs, or transcripts.

Risk: EVENTBRITE_TOKEN and browser-session access function like account credentials.

Mitigation: Store tokens and browser sessions carefully, do not commit them, and rotate or revoke access if they are exposed.

Risk: Eventbrite's documented API supports organizer write operations outside this skill's stated scope.

Mitigation: Keep usage to the documented read-only recipes and review any proposed command before execution.

## Reference(s):

- [Eventbrite token API recipes](references/token-api.md)
- [Eventbrite discovery API recipes](references/discovery-api.md)
- [Eventbrite API token setup](https://www.eventbrite.com/platform/api-keys)
- [Eventbrite documented API root](https://www.eventbriteapi.com/v3)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and jq-oriented JSON API outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes for curl and fpx surfaces; command results can include sensitive account, ticket, organizer, and attendee data.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
