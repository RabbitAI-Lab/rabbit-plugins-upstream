## Description:

Access your Vibo event music planning through MCP for events, timelines, song requests, playlists, do-not-play lists, joins, song updates, and exports to Spotify or Apple Music.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their Vibo account, inspect event music planning data, manage timeline sections and song requests, and export event playlists through the vibo-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses Vibo credentials, access tokens, refresh tokens, and a local session file that can grant account access if exposed.

Mitigation: Treat VIBO_PASSWORD, VIBO_ACCESS_TOKEN, VIBO_REFRESH_TOKEN, and ~/.vibo-mcp/session.json as secrets, and avoid sharing MCP configuration files.

Risk: Mutating Vibo tools can change event music planning data, contacts, comments, notifications, exports, and related account state.

Mitigation: Keep confirmation mode on ask-user so account-changing actions require an explicit preview and approval before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [Vibo](https://vibodj.com)
- [vibo-mcp npm Package](https://www.npmjs.com/package/vibo-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with JSON configuration snippets and MCP tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools can return compact or full views where supported; mutating tools use confirmation previews before account-changing actions.]

## Skill Version(s):

2.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
