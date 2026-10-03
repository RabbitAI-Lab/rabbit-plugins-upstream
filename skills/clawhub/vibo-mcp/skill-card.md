## Description:

Connects an agent to Vibo to review and manage event timelines, song requests, playlists, and music exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Event hosts and couples use this skill to review Vibo event plans and song requests, update timelines and playlists, and export music to connected services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vibo account passwords or captured session tokens may be stored locally and exposed through shared or committed configuration files.

Mitigation: Use private, non-synced MCP configuration; never commit credentials, and treat the saved browser session file like a password.

Risk: Event edits, invitations, or exports can affect real events if approved without review.

Mitigation: Keep the default ask-user confirmation mode and review each action preview before approving it.

## Reference(s):

- [Vibo](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [vibo-mcp source repository (linked in skill)](https://github.com/chrischall/vibo-mcp)
- [ContextMint Bridge browser extension](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Markdown responses and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results may omit media by default; changes require a confirmation preview unless the confirmation mode is changed.]

## Skill Version(s):

2.4.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
