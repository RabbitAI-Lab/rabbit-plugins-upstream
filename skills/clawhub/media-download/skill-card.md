## Description:

Download videos, audio, playlists, and Pinterest images from links or searches to local files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use it to save media from links for offline viewing, editing, or visual research. It can also extract audio, metadata, and playlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial security scan marks the skill suspicious and cites browser-session downloads, cookie handling, unpinned setup tools, and unresolved references.

Mitigation: Review the browser-session and cookie options before use, and check the setup tools and unresolved references before deployment; treat the scan as incomplete rather than as a finding of malicious intent.

## Reference(s):

- [ClawHub media-download release](https://clawhub.ai/vargai/skills/media-download)
- [Pinterest moodboard presets](references/pinterest-presets.md)
- [yt-dlp installation guide](https://github.com/yt-dlp/yt-dlp#installation)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Local MP4, MP3, and image files, with saved-file paths and brief status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Files are saved to the selected directory; available formats depend on the source and chosen options.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
