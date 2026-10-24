## Description:

Connects an agent to Vibo event music planning to review timelines, requests and playlists, and manage songs, guests and music exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Event hosts and couples use an agent to review Vibo timelines and song requests, manage event music and guests, and export playlists to connected music services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vibo passwords and captured session tokens grant access to the user's account.

Mitigation: Keep credentials in private, uncommitted configuration with restrictive permissions; revoke or rotate them if exposed.

Risk: Changes to event songs, sections, guests or connected playlists can affect a live event.

Mitigation: Review the proposed changes and approve the confirmation preview before submitting a write action.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [Vibo](https://vibodj.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Text or Markdown, including configuration examples and action previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event information comes from the connected Vibo account; changes require user confirmation.]

## Skill Version(s):

2.4.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
