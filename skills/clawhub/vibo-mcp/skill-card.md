## Description:

Helps people plan Vibo event music through an MCP server, including timelines, song requests, playlists, and music-service exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Vibo hosts and event planners use the skill to review event timelines and song requests, organize playlists, manage event participation, and export music to connected services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vibo account credentials and captured session tokens may be stored in local configuration files and exposed if those files are shared.

Mitigation: Keep credential files out of repositories and sync folders, restrict file permissions, and rotate or revoke credentials if exposed.

Risk: Event membership, song lists, and planning details can be changed through write tools.

Mitigation: Review each proposed change and its confirmation preview before approving it.

## Reference(s):

- [vibo-mcp on ClawHub](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [Vibo](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read responses may use compact or full views; event changes require user confirmation.]

## Skill Version(s):

2.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
