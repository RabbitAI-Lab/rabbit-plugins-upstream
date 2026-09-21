## Description:

Search Etix events, venues, and performers and pull event/venue details via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Etix events, venues, performers, and showtimes, then retrieve event or venue details through the etix-mcp integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration sends Etix requests through the user's own browser tab and cookies using a browser bridge.

Mitigation: Install and pair the bridge only when needed, keep the extension paired only during intended use, and confirm the user is comfortable with this request path.

Risk: The integration uses Etix website endpoints rather than an official public API.

Mitigation: Review Etix's terms before use and expect endpoint behavior or access requirements to change.

## Reference(s):

- [Etix](https://www.etix.com/ticket/)
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an installed MCP server and browser bridge to retrieve public Etix event and venue data.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
