## Description:

vibo-mcp lets agents access Vibo event music planning through an MCP server, including events, timeline sections, song requests, playlists, and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External Vibo users and their agents use this skill to inspect and update event music plans, including timelines, song requests, playlists, guest participation, and music-service exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup runs vibo-mcp through an unpinned npm invocation.

Mitigation: Install and register a pinned, reviewed vibo-mcp version before connecting it to a production agent.

Risk: The skill can use Vibo passwords, access tokens, refresh tokens, or captured browser sessions.

Mitigation: Store credentials outside plaintext project config where possible, restrict local file permissions, and revoke or delete captured sessions when they are no longer needed.

Risk: Mutating Vibo actions can change event music plans, guest access, comments, profile images, and exports.

Mitigation: Use the built-in dry-run behavior and require confirm: true only after reviewing the proposed change.

## Reference(s):

- [vibo-mcp on ClawHub](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [Vibo](https://vibodj.com)
- [vibo-mcp GitHub repository](https://github.com/chrischall/vibo-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses compact responses by default for media-bearing read tools; mutating tools are confirm-gated and return dry-run previews unless explicitly confirmed.]

## Skill Version(s):

1.8.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
