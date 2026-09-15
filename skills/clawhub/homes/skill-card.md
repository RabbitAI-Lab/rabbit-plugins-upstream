## Description:

Look up real-estate listings, property details, price and tax history, market reports, saved homes, and photo galleries on homes.com via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate researchers use this skill to ask an agent for homes.com property search results, listing details, histories, market reports, saved homes, saved searches, photos, and local mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an external MCP package and browser extension through a signed-in homes.com browser session.

Mitigation: Pin homes-mcp to a reviewed version, review the fetchproxy extension source and permissions, and install only when that session access is acceptable.

Risk: Saved homes and saved searches can expose account-specific homes.com data.

Mitigation: Invoke saved-home or saved-search tools only after an explicit user request and avoid retaining or sharing the returned account-specific data beyond the task.

Risk: homes.com does not publish a public consumer API, so page extraction can fail or produce incomplete results when page structure, authentication, or WAF behavior changes.

Mitigation: Treat extracted property data as informational, check important facts against homes.com directly, and surface authentication or challenge errors instead of silently retrying.

## Reference(s):

- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include homes.com listing data, property URLs, market statistics, photo URLs when requested, and local calculator results.]

## Skill Version(s):

1.4.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
