## Description:

Query eventbrite.com from a shell for tickets, orders, organization events, attendees, and public event discovery using Eventbrite token API calls and an fpx browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to compose read-only shell commands for Eventbrite account data, organization events, attendees, orders, and public event discovery without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Eventbrite tokens, browser-session cookies, orders, tickets, attendee names, and attendee emails may be exposed if command output or logs are shared.

Mitigation: Keep usage to authorized read-only queries, avoid logging or committing tokens and cookies, and treat returned Eventbrite account data as private.

Risk: The browser-bridge surface depends on a signed-in Eventbrite browser session and can fail when pairing, CSRF cookies, or bot-wall state are stale.

Mitigation: Use the documented token API for scripts when possible, and refresh or re-pair the browser bridge before retrying fpx discovery calls.

## Reference(s):

- [Eventbrite token API recipes](references/token-api.md)
- [Eventbrite discovery API recipes](references/discovery-api.md)
- [Eventbrite API key setup](https://www.eventbrite.com/platform/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, curl examples, fpx examples, and jq recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only command guidance; generated commands may return private Eventbrite account, order, ticket, attendee, token, or browser-session data.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
