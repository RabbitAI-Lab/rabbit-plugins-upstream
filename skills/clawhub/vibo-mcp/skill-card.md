## Description:

Helps hosts and couples plan event music through Vibo by reading timelines, requests and playlists and managing songs, guests and music exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Event hosts and couples use this skill to check Vibo event timelines, song requests and playlists, and to manage songs, participants and music exports through an assistant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and saved session tokens can expose the user's Vibo account and connected music services.

Mitigation: Install only if you trust the vibo-mcp package and protect credentials and saved session tokens.

Risk: Changes to events, participants, playlists or music exports may affect the user's account.

Mitigation: Keep the default write-confirmation mode and review each preview before approving a change.

## Reference(s):

- [vibo-mcp ClawHub release](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [Vibo](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration]

**Output Format:** [Text and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event details and song lists; confirmation previews and receipts for account changes.]

## Skill Version(s):

2.4.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
