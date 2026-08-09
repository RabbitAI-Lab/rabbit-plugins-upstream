## Description:

Access Vibo event music planning through an MCP server for event timelines, song requests, playlists, guest participation, and Spotify or Apple Music exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their Vibo account, inspect event music planning data, and manage event songs, sections, guests, comments, notifications, and playlist exports through MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored Vibo credentials or captured session tokens could expose account and event-planning data if `.mcp.json` or `~/.vibo-mcp/session.json` is shared or leaked.

Mitigation: Keep credential and session files private, prefer the normal email/password path when appropriate, and revoke or rotate Vibo sessions if credentials or tokens may have been exposed.

Risk: The MCP server can modify Vibo event data, including songs, sections, guest roles, comments, notifications, and playlist exports.

Mitigation: Review dry-run previews before enabling `confirm: true` on mutating tools, and only install the skill when event-management access is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [Vibo](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with JSON configuration snippets, inline shell commands, and MCP tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mutating Vibo tools are described as confirm-gated and return a dry-run preview unless confirm is true.]

## Skill Version(s):

1.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
