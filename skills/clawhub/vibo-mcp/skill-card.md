## Description:

Access Vibo event music planning through an MCP server for timelines, song requests, playlists, account details, and confirm-gated edits or exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External Vibo users and the developers configuring their MCP client use this skill to read event timelines, song requests, playlists, guest details, and account state, and to prepare confirm-gated updates such as song edits, event joins, playlist imports, and music-service exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can access Vibo account data, event details, guest information, song lists, connected playlists, and confirm-gated edit or export actions.

Mitigation: Install only when that account access is acceptable, review proposed actions before confirmation, and keep mutating tool calls gated with explicit confirmation.

Risk: Stored Vibo credentials or captured session tokens could expose the user's account if shared through configuration files, logs, or screenshots.

Mitigation: Keep .mcp.json and ~/.vibo-mcp/session.json private, avoid sharing them in support material, and treat Vibo tokens and passwords as secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [Vibo website](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference MCP tool calls and confirm-gated action previews.]

## Skill Version(s):

1.5.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
