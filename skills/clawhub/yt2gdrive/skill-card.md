## Description:

Sync latest audio or video (mp3/mp4) from YouTube channels to Google Drive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangoal2019](https://clawhub.ai/user/yangoal2019)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and run a local YouTube channel media sync workflow that stages recent audio or video files and uploads them to Google Drive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A misconfigured rclone remote, channel list, or staging directory could upload or clean up unintended local files.

Mitigation: Review the channel list, configure rclone intentionally, run with --dry-run first, and keep LOCAL_DIR pointed at a dedicated staging folder.

Risk: Optional launchd installation can make the sync run automatically every day.

Mitigation: Run scripts/install_launchd.sh only when scheduled execution is desired, and use the documented launchctl unload command to disable it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangoal2019/skills/yt2gdrive)
- [yt-dlp documentation](https://github.com/yt-dlp/yt-dlp)
- [rclone documentation](https://rclone.org/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and environment variable settings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide local media download, Google Drive upload, local cleanup, dry-run checks, and optional macOS launchd scheduling.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
