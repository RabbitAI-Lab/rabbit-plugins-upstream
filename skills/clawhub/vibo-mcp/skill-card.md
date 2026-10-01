## Description:

Helps Vibo hosts plan event music and manage timelines, song requests, playlists, and exports through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Vibo event hosts and their assistants use this skill to review event timelines, coordinate music requests and playlists, and make approved changes to event plans or connected music services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vibo credentials and saved session tokens could expose account and connected music-service data.

Mitigation: Protect passwords and tokens, and configure the server only in projects that need Vibo access.

Risk: Running an unpinned npm package may execute a changed release.

Mitigation: Review the npm package before installation and pin a reviewed version when possible.

Risk: Event changes, user-role edits, section deletion, and playlist exports can affect shared plans or connected services.

Mitigation: Keep the default confirmation flow enabled and review each change preview before approving it.

## Reference(s):

- [Vibo](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [ContextMint Bridge browser extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls]

**Output Format:** [Markdown guidance and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads return event and music data; changes return confirmation previews or receipts.]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
