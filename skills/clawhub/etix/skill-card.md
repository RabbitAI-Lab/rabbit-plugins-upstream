## Description:

Search Etix events, venues, and performers and pull event/venue details via MCP. Triggers on phrases like "find events on etix", "etix tickets for", "what's playing at <venue> on etix", "etix event details for", "search etix for <artist>", or any request involving Etix events, venues, performers, or showtimes. Requires etix-mcp installed and the fetchproxy extension active with an open etix.com tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Etix events, venues, and performers and retrieve event or venue details through the etix-mcp integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the etix-mcp npm package and a browser extension that relays requests through an open etix.com tab.

Mitigation: Review the package and extension sources before use, keep the extension disabled when not needed, and install only in environments where this browser bridge is acceptable.

Risk: The integration relies on Etix website behavior rather than an official public API.

Mitigation: Use the healthcheck tool when requests fail and verify important event or venue details against Etix before relying on them.

Risk: Requests are dispatched through the user's browser session.

Mitigation: Use the skill consistent with Etix terms and with awareness that the active browser session mediates access.

## Reference(s):

- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [etix-mcp source repository](https://github.com/chrischall/etix-mcp)
- [fetchproxy browser extension source](https://github.com/chrischall/fetchproxy)
- [Etix website](https://www.etix.com/ticket/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires etix-mcp, the fetchproxy extension, and an open etix.com tab for use.]

## Skill Version(s):

0.4.5 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
