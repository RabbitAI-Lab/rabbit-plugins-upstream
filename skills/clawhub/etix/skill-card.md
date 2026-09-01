## Description:

Search Etix events, venues, and performers and pull event/venue details via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Etix events, venues, performers, showtimes, and public event details through an MCP server connected to their own browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an unofficial Etix integration and a user-approved browser bridge to access public event data behind Etix's bot-wall.

Mitigation: Install only when comfortable with that access pattern, review fetchproxy extension permissions, and pair only the expected Etix MCP/domain.

Risk: Requests are dispatched through the user's own browser session.

Mitigation: Use a browser session appropriate for Etix access and run the health check before relying on search or detail results.

Risk: Etix does not publish a public consumer API, so website endpoints and pages may change.

Mitigation: Treat failures or unexpected results as integration drift and verify important event, venue, price, and availability details directly on Etix.

## Reference(s):

- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [etix-mcp source repository](https://github.com/chrischall/etix-mcp)
- [fetchproxy source repository](https://github.com/chrischall/fetchproxy)
- [Etix website](https://www.etix.com/ticket/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include setup guidance, MCP tool names, event search results, venue details, event details, health-check guidance, and user-facing risk notes.]

## Skill Version(s):

0.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
