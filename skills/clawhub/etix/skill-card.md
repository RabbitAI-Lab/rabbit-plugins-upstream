## Description:

Search Etix events, venues, and performers and retrieve event and venue details through an MCP server that uses an active Etix browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to search Etix event listings, inspect performers and venues, and retrieve event details such as time, venue, organizer, location, prices, and offer levels. It is intended for event-discovery workflows that can use a local MCP server and browser extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation depends on mutable third-party package and extension code.

Mitigation: Review etix-mcp and fetchproxy before installing, pin exact package versions and repository commits, and prefer project-scoped MCP configuration.

Risk: The extension routes requests through the user's active Etix browser session.

Mitigation: Use a dedicated browser profile with no unrelated signed-in sessions, and disable the extension when it is not actively needed.

Risk: Etix does not provide a public consumer API, so website endpoints and access controls may change.

Mitigation: Run etix_healthcheck when tools fail and review behavior against Etix terms before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [etix-mcp source](https://github.com/chrischall/etix-mcp)
- [fetchproxy extension source](https://github.com/chrischall/fetchproxy)
- [Etix website](https://www.etix.com/ticket/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool names, setup steps, search results, event details, venue details, and healthcheck guidance.]

## Skill Version(s):

0.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
