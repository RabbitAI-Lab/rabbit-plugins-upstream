## Description:

Manage Resy restaurant reservations via MCP, including venue search, table booking, reservation listing and cancellation, favorites, and Priority Notify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent search Resy availability, book or cancel reservations, manage favorites, and subscribe to Priority Notify through a configured resy-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unpinned third-party MCP server with Resy account credentials.

Mitigation: Pin the MCP package or use a reviewed local build, and protect Resy credentials with a secret manager or tightly controlled environment variables.

Risk: The skill can make or cancel real restaurant reservations, including actions that may involve payment or cancellation consequences.

Mitigation: Require the agent to confirm the restaurant, date, time, party size, and any payment or cancellation consequences before booking or canceling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)
- [resy-mcp source link from skill documentation](https://github.com/chrischall/resy-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include Resy search results, booking receipts, cancellation status, favorites, notifications, and setup guidance.]

## Skill Version(s):

0.13.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
