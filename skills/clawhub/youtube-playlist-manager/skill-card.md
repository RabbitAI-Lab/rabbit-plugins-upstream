## Description:

Searches YouTube, retrieves video details, and helps users manage their own YouTube playlists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[odrobnik](https://clawhub.ai/user/odrobnik)

### License/Terms of Use:

MIT-0

## Use Case:

Users and their agents can search YouTube, inspect video details, and view or change the user's own playlists with their permission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google OAuth access and locally stored credentials or tokens could expose the user's YouTube account.

Mitigation: Grant access only when comfortable with playlist management, keep config.json and tokens.json private, and use logout to revoke local access.

Risk: Playlist edits or deletions can make unwanted changes to the user's account.

Mitigation: Review destructive playlist changes before approving --yes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/odrobnik/skills/youtube-playlist-manager)
- [Project homepage](https://github.com/odrobnik/youtube-skill)
- [YouTube IFrame Player reference](references/iframe-player.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON (--json)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results, video details, playlist information, change results, and confirmation previews.]

## Skill Version(s):

1.3.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
