## Description:

Guides an agent through bounded yt-dlp workflows for downloading videos, extracting audio or subtitles, cutting clips, and archiving scoped playlists or channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tmchow](https://clawhub.ai/user/tmchow)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill when they need an agent to save streaming-site media, extract audio or subtitles, cut clips, or archive a bounded playlist or channel while preserving safe confirmation points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may download files to disk and run yt-dlp or ffmpeg for URLs the user provides.

Mitigation: Use the skill for user-requested media only, verify resulting files, and stop when rights, scope, user-only input, or missing binaries block safe completion.

Risk: Browser cookies, cookie files, PO tokens, headers, or other auth material can expose secrets if used casually.

Mitigation: Require explicit user approval before auth access, prefer browser-cookie access over raw cookie files, avoid printing or logging secrets, and stop when a workaround would require exposing token values.

Risk: Playlist or channel URLs can expand into large or unintended downloads.

Mitigation: Confirm playlist or channel range before archive work, keep single-video jobs on --no-playlist, and use an archive file so reruns skip completed entries.

## Reference(s):

- [YouTube auth and extractor failure late route](references/youtube-auth.md)
- [yt-dlp upstream project](https://github.com/yt-dlp/yt-dlp)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local media files as task artifacts when the agent follows the skill.]

## Skill Version(s):

0.1.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
