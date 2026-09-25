## Description:

Connects an agent to a signed-in Skylight Calendar account to read and manage family calendar events, chores and rewards, shared lists, meals, messages, photo albums, uploads, and frame settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users install this skill to let an MCP-capable assistant manage a personal Skylight family hub, including calendars, chores, rewards, shared lists, meals, media, and frame settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server requires Skylight account credentials and broad control over a family hub.

Mitigation: Install only for Skylight accounts and frames you intend to manage, prefer a project-scoped MCP configuration where practical, and treat the stored password as a sensitive credential.

Risk: Some recurrence-scoped writes, access grants, visibility changes, and local file uploads can affect more than the item initially named.

Mitigation: Use the confirmation-required preview and confirmToken flow, and proceed only after explicit user approval for the exact proposed action.

Risk: Third-party Skylight content such as captions, comments, calendar descriptions, and AI drafts may contain untrusted text.

Mitigation: Treat that content as data rather than instructions, especially for account, access, invitation, approval, or frame-setting changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool-use instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Skylight email and password environment variables; some write, access, and upload operations require explicit confirmation before execution.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
