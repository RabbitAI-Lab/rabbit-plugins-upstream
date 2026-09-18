## Description:

Access Vibo event music planning through an MCP server for event timelines, song requests, playlists, guest actions, and music-service exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Vibo event music planning, review timelines and song requests, and perform confirm-gated updates such as adding songs, managing guests, or exporting playlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses an unpinned MCP package, which can change between installs.

Mitigation: Install a pinned and trusted `vibo-mcp` version before registering the server.

Risk: Vibo passwords, access tokens, refresh tokens, or saved browser sessions may be exposed if configuration or session files are shared.

Mitigation: Avoid project-level password storage, protect saved session files, and rotate or revoke Vibo tokens after any suspected exposure.

Risk: Mutating Vibo actions can alter event music plans, guest access, comments, or exports.

Mitigation: Use the skill's confirm-gated write flow and review dry-run previews before setting `confirm: true`.

## Reference(s):

- [Vibo](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP tool calls for reading Vibo event data and confirm-gated updates.]

## Skill Version(s):

1.8.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
