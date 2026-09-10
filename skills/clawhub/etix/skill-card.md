## Description:

Search Etix events, venues, and performers and retrieve event or venue details through an MCP server that uses a browser-backed Etix session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find Etix events, venues, performers, showtimes, and ticket-related event details from public Etix pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run unpinned third-party code.

Mitigation: Pin and verify the etix-mcp package version and fetchproxy commit before use.

Risk: Requests are routed through a live browser session.

Mitigation: Use a dedicated browser profile for Etix and avoid using a profile with unrelated sensitive sessions.

Risk: The browser extension and MCP configuration may remain active after the task is complete.

Mitigation: Remove or disable the extension and MCP configuration when finished.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [fetchproxy extension repository](https://github.com/chrischall/fetchproxy)
- [Etix website](https://www.etix.com/ticket/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires etix-mcp, the fetchproxy extension, and an open etix.com tab.]

## Skill Version(s):

0.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
