## Description:

Query Eventbrite data from a shell using curl for the documented token API and fpx for browser-backed public event discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Eventbrite account, organization, attendee, ticket, event, and public discovery data from command-line workflows without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to query Eventbrite account data using a personal token or browser session.

Mitigation: Install only when account-data access is intended, prefer token-based curl for scripts, and avoid logging tokens or captured cookies.

Risk: Browser-backed discovery depends on fpx and Transporter pairing, which can expose signed-in Eventbrite session access to agent-driven requests.

Mitigation: Review and remove fpx or Transporter pairing when browser-session access is no longer needed.

Risk: The documented API supports organizer write operations, but the artifact only scopes read-only recipes.

Mitigation: Keep agent usage limited to the provided read-only commands and review any proposed write calls before execution.

## Reference(s):

- [Eventbrite documented API recipes](artifact/references/token-api.md)
- [Eventbrite discovery API recipes](artifact/references/discovery-api.md)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/eventbrite-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only command recipes for Eventbrite APIs and browser-bridged discovery flows.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
