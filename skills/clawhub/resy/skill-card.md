## Description:

Manage Resy restaurant reservations through an MCP server by searching venues, booking and canceling tables, listing reservations, managing favorites, and subscribing to Priority Notify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage personal Resy reservation workflows from natural-language requests after configuring the Resy MCP server with their Resy account credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an npm MCP server with Resy credentials.

Mitigation: Use a pinned, reviewed version of the MCP server and avoid committing .mcp.json or .env files that contain credentials.

Risk: The connected MCP tools can book or cancel restaurant reservations.

Mitigation: Require explicit confirmation before booking or cancellation actions and run the server in a restricted environment.

Risk: The server uses Resy's private web-app API, which may change without notice.

Mitigation: Review failures carefully before retrying actions, especially favorite and Priority Notify calls that rely on reverse-engineered endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)
- [resy-mcp source repository](https://github.com/chrischall/resy-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON configuration snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may lead an agent to call Resy MCP tools that read account data or book and cancel reservations.]

## Skill Version(s):

0.14.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
