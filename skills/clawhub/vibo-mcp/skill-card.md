## Description:

Helps an agent manage Vibo event music plans, including timelines, song requests, playlists, and music-service exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Event hosts and couples use this skill to ask an agent about Vibo event timelines, song requests, and playlists, and to make approved music-planning changes or exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account passwords and captured access or refresh tokens in local configuration or session files could be exposed.

Mitigation: Treat credentials and ~/.vibo-mcp/session.json as secrets; avoid committing configuration files, restrict file permissions, and revoke or rotate exposed credentials.

Risk: An agent could change event music, guest access, or exports without the user's intended approval.

Mitigation: Keep confirmation mode enabled for write actions and review each proposed change before approving it.

## Reference(s):

- [vibo-mcp ClawHub release](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [Vibo](https://vibodj.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration]

**Output Format:** [Markdown guidance and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results and confirmation previews or receipts for event-music changes; compact responses omit media by default.]

## Skill Version(s):

2.4.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
