## Description:

Access Vibo event timelines, song requests, playlists, and music exports through an MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Vibo users and their assistants can review event plans and song requests, organize music and guests, and export event playlists through their Vibo account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installed package can access the user's Vibo account and its event data.

Mitigation: Install only if you trust the vibo-mcp package and review event changes before approving them.

Risk: Passwords, access tokens, refresh tokens, and saved sessions can expose the Vibo account if shared.

Mitigation: Keep credentials and session files private; omit secrets from shared configuration, logs, screenshots, and support bundles.

## Reference(s):

- [Vibo](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Shell commands]

**Output Format:** [Markdown with JSON configuration examples and tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event changes require user confirmation; some read tools offer compact or full responses.]

## Skill Version(s):

2.4.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
