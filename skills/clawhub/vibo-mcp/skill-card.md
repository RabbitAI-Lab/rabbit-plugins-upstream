## Description:

vibo-mcp lets agents access Vibo event music planning through MCP for events, timelines, song requests, playlists, and music-service exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users planning events with Vibo use this skill to inspect and update event music details, including timeline sections, requested songs, playlists, guest participation, and exports to Spotify or Apple Music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vibo passwords, access tokens, refresh tokens, and saved browser sessions are sensitive secrets.

Mitigation: Keep VIBO_PASSWORD, VIBO_ACCESS_TOKEN, VIBO_REFRESH_TOKEN, and ~/.vibo-mcp/session.json out of source control, logs, shared folders, and backups; rotate credentials if exposure is suspected.

Risk: Confirmed MCP tool calls can change Vibo event music planning data.

Mitigation: Review dry-run previews and use confirm-gated write operations only when the proposed change matches the intended event, section, song, user, or export action.

## Reference(s):

- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [Vibo](https://vibodj.com)
- [Vibo web app](https://web.vibodj.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown text with JSON configuration and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP tool use may read Vibo account data and, when confirmed, modify event music planning data.]

## Skill Version(s):

1.5.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
