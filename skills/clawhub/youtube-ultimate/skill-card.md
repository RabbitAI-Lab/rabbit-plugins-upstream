## Description:

Helps agents extract YouTube transcripts, search and inspect videos, read comments and account data with opt-in read-only OAuth, and download video or audio through yt-dlp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to research YouTube content, collect transcripts, inspect channels, comments, playlists, subscriptions, and liked videos, and optionally save media for offline workflows. It is suited for transcript-first research where unauthenticated transcript access can be combined with opt-in YouTube Data API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic migration of a legacy pickle token can execute code from a local credential file.

Mitigation: Before running version 4.3.0 on a system with older credentials, remove or quarantine ~/.config/youtube-skill/token.pickle and re-authenticate to create a fresh JSON token.

Risk: Authenticated commands can read YouTube account data such as channel information, subscriptions, playlists, and liked videos.

Mitigation: Use YOUTUBE_SKILL_NO_ACCOUNT=1 when account access is not needed, and authenticate only with a user-created OAuth client using the youtube.readonly scope.

Risk: Download commands write media files to disk and rely on locally installed tools.

Mitigation: Set YOUTUBE_SKILL_NO_DOWNLOAD=1 to disable downloads, choose an explicit output directory, and install yt-dlp and uv from trusted sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/youtube-ultimate)
- [YouTube read-only OAuth scope](https://www.googleapis.com/auth/youtube.readonly)
- [Google account permissions](https://myaccount.google.com/permissions)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Plain text, JSON, Markdown with inline shell commands, and downloaded media files when download commands are used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript and metadata commands print to stdout; authenticated commands require a user-provided Google OAuth client; downloads write media files to the requested directory or current directory.]

## Skill Version(s):

4.3.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
