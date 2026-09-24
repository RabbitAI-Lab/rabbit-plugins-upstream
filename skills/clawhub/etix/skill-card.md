## Description:

Search Etix events, venues, and performers and retrieve event or venue details through an MCP server that uses an active Etix browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Etix events, venues, performers, showtimes, and details from within an MCP-enabled workflow. It is intended for event discovery tasks that can rely on the user's own active Etix browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Etix requests through the user's own browser session, which may expose session context to the MCP workflow.

Mitigation: Install only for trusted workflows, use project-local MCP configuration where possible, and keep the browser extension enabled only when needed.

Risk: The setup depends on a browser extension and an active Etix tab, so tool calls may fail if the bridge, extension, pairing, or Etix session is unavailable.

Mitigation: Run the documented health check after setup and before relying on event or venue results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [Etix website](https://www.etix.com/ticket/)
- [fetchproxy setup dependency](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose MCP configuration and browser-extension setup steps before the Etix tools can be used.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
