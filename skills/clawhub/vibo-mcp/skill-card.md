## Description:

Access Vibo event music planning through an MCP server so an agent can help with events, timeline sections, song requests, playlists, and music exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a Vibo account for event music planning tasks such as reviewing timelines, managing song requests, joining shared events, and exporting playlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vibo credentials or saved session tokens could expose account access if logged, committed, or shared.

Mitigation: Treat VIBO_PASSWORD, VIBO_ACCESS_TOKEN, VIBO_REFRESH_TOKEN, and ~/.vibo-mcp/session.json as secrets; keep them out of source control and restrict local file access.

Risk: Write actions can change event songs, comments, users, timeline sections, profile photos, notifications, or playlist exports.

Mitigation: Review dry-run previews before setting confirm:true on mutating tools.

## Reference(s):

- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [Vibo](https://vibodj.com)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON configuration snippets and inline MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mutating Vibo tools are confirm-gated and provide a dry-run preview before confirm:true.]

## Skill Version(s):

1.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
