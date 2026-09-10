## Description:

TinkerClaw YouTube lets agents retrieve YouTube transcripts, download media, and explore video, channel, comment, and account data with optional read-only Google OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to research YouTube content, extract transcripts, inspect videos and channels, read comments, and optionally download media for offline workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that automatic legacy token migration can execute code from a local pickle file before user consent.

Mitigation: Review before installing and avoid authenticated commands until legacy pickle migration is removed or changed to refuse pickle files; remove old token.pickle files and re-authenticate to JSON tokens.

Risk: Authenticated commands can read personal YouTube account data and store a long-lived OAuth token locally.

Mitigation: Use a dedicated ~/.config/youtube-skill/credentials.json OAuth client, confirm the youtube.readonly scope at consent time, and use YOUTUBE_SKILL_NO_ACCOUNT=1 or logout when account access is not needed.

Risk: Download commands write media and subtitle files to the selected output directory, or to the current directory when no output directory is provided.

Mitigation: Set an explicit output directory for downloads, review the target path before running, or set YOUTUBE_SKILL_NO_DOWNLOAD=1 in environments where file writes are not intended.

Risk: Unpinned runtime dependencies can reduce reproducibility for installations that require controlled builds.

Mitigation: Pin dependency versions and verify the installed yt-dlp binary when reproducible execution is required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/globalcaos/skills/youtube-ultimate)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [TinkerClaw project link from skill metadata](https://github.com/globalcaos/tinkerclaw)
- [YouTube read-only OAuth scope](https://www.googleapis.com/auth/youtube.readonly)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance]

**Output Format:** [Plain text and JSON CLI output, with optional downloaded media and subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated commands require a user-provided Google OAuth client; downloads require yt-dlp and write files only when requested.]

## Skill Version(s):

4.3.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
