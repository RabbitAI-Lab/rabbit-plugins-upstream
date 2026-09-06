## Description:

Access Vibo event music planning via MCP for events, timelines, song requests, playlists, exports, and song-management actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and event hosts use this skill to manage Vibo wedding or event music workflows from an agent, including reading event timelines, adding or updating songs, joining events, inviting users, and exporting playlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses locally stored Vibo passwords or session tokens for an account that can read and change event data.

Mitigation: Install only when that access is acceptable, keep .mcp.json and ~/.vibo-mcp/session.json private, restrict file permissions where possible, and rotate or revoke Vibo credentials or tokens if exposure is suspected.

Risk: Full responses from some read tools can include profile images, notification images, song thumbnails, or cover art.

Mitigation: Prefer compact search responses where available, page larger read results with limit parameters, and avoid sharing full tool outputs outside the trusted workspace.

Risk: Mutating tools can change Vibo event data after confirmation.

Mitigation: Review dry-run previews carefully and pass confirm:true only after the intended event, section, song, user, or export action is verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [Vibo](https://vibodj.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some MCP tools return Vibo account, event, song, playlist, user, notification, and media-link data; mutating tools require confirm:true before making network changes.]

## Skill Version(s):

1.7.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
