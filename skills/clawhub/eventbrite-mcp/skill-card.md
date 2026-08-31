## Description:

Query eventbrite.com from a shell for tickets, orders, organization events, attendees, and public event discovery using Eventbrite token API curl recipes and fpx browser-bridge recipes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Eventbrite account, organization, event, attendee, ticket, and public discovery data from shell workflows. It is suited to authorized read-only reporting, lookup, and one-shot data retrieval without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Eventbrite tokens, browser-session cookies, order details, and attendee names or emails may expose sensitive account data.

Mitigation: Use the skill only for authorized accounts, keep token and cookie material out of logs and commits, and restrict outputs to audiences allowed to view the Eventbrite data.

Risk: The fpx bridge depends on a signed-in browser session with Eventbrite site access.

Mitigation: Grant browser access only for the intended Eventbrite account, approve pairing deliberately, and remove or revoke access when the workflow is no longer needed.

Risk: Public discovery calls rely on Eventbrite consumer-site behavior that may return WAF interstitials or change response shapes.

Mitigation: Validate the first response before automating, handle non-JSON and non-2xx responses explicitly, and prefer the documented token API for supported account and event lookups.

## Reference(s):

- [Eventbrite access skill source](SKILL.md)
- [Eventbrite documented API curl recipes](references/token-api.md)
- [Eventbrite discovery API fpx recipes](references/discovery-api.md)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/eventbrite-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-processing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes; command output is typically JSON intended for jq processing.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
