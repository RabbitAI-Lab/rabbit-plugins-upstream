## Description:

Search Etix events, venues, and performers and retrieve event and venue details through an MCP server that requires etix-mcp, the fetchproxy extension, and an open etix.com tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Etix events, venues, performers, showtimes, and ticket-related event details from an agent workflow. It is useful when an agent needs structured event discovery or venue detail retrieval through the Etix MCP integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration can route Etix-domain requests through the user's active browser session.

Mitigation: Install only when browser-session routing is acceptable, approve pairing only when the displayed code matches, and remove or revoke the extension or pairing when it is no longer needed.

Risk: Use may be affected by Etix terms and by changes to Etix website behavior.

Mitigation: Review Etix's terms before use and keep workflows limited to permitted event-discovery and detail-retrieval activity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [Etix website](https://www.etix.com/ticket/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on an active etix.com browser tab and fetchproxy pairing.]

## Skill Version(s):

0.6.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
