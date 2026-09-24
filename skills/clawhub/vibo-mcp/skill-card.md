## Description:

Accesses Vibo event music planning through an MCP server so agents can help with events, timelines, song requests, playlists, do-not-play lists, event joining, and Spotify or Apple Music exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and event hosts use this skill to let an agent inspect and update Vibo event music plans, including timelines, song requests, guest contributions, playlists, and music-service exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vibo credentials, captured browser session tokens, or local session files may be exposed if MCP configuration files, backups, source control, or shared machines are not handled carefully.

Mitigation: Use project-scoped MCP configuration when possible, keep credential and session files out of source control and backups, restrict local file permissions, and revoke or rotate Vibo credentials or tokens if the machine or configuration is shared.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [Vibo](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [Source repository listed by the skill](https://github.com/chrischall/vibo-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include setup guidance, MCP configuration snippets, dry-run previews for confirm-gated writes, and summaries of Vibo account or event data.]

## Skill Version(s):

2.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
