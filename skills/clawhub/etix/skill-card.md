## Description:

Search Etix events, venues, and performers and pull event/venue details via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Etix event listings, inspect event or venue details, and troubleshoot the local Etix MCP bridge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Etix requests through the user's browser session by way of a local MCP server and browser extension.

Mitigation: Use a dedicated browser profile with only the Etix access intended for the agent, approve pairing deliberately, and review the npm package and extension source before installation.

Risk: Etix does not provide a public consumer API, so the site behavior and endpoints this integration depends on may change.

Mitigation: Run the Etix healthcheck when tool calls fail and confirm important event or venue details on Etix before relying on them.

Risk: Use of the integration may be governed by Etix terms and organizational policy.

Mitigation: Use it only in contexts where routing requests through the user's own browser session is acceptable under applicable terms and internal policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [etix-mcp source repository](https://github.com/chrischall/etix-mcp)
- [fetchproxy source repository](https://github.com/chrischall/fetchproxy)
- [Etix ticket site](https://www.etix.com/ticket/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool names, event or venue identifiers, event URLs, venue details, price ranges, and healthcheck guidance.]

## Skill Version(s):

0.4.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
