## Description:

Search YouTube and view or manage your own playlists through the YouTube Data API v3.

This skill is ready for commercial/non-commercial use.

## Publisher:

[odrobnik](https://clawhub.ai/user/odrobnik)

### License/Terms of Use:

MIT-0

## Use Case:

People can ask an agent to search YouTube or view and change their own playlists, including adding and removing videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google OAuth grants account-wide YouTube access, and saved credentials can remain active until revoked.

Mitigation: Use a dedicated Google Cloud project, keep configuration and token files private, and sign out or revoke app access when no longer needed.

Risk: Deleting playlists or removing videos permanently changes the user's account.

Mitigation: Review the preview and obtain explicit approval before running destructive commands with --yes.

## Reference(s):

- [ClawHub release](https://clawhub.ai/odrobnik/skills/youtube-playlist-manager)
- [Project homepage](https://github.com/odrobnik/youtube-skill)
- [Setup instructions](SETUP.md)
- [YouTube IFrame Player reference](references/iframe-player.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Plain text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results, playlist details and change confirmations depend on the user's request and Google account access.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
