## Description:

Downloads video, audio, and Pinterest images from supported links to local files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to save linked videos, audio, playlists, and Pinterest images for editing, reference gathering, or offline access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-login downloads have misleading privacy assurances about cookie use.

Mitigation: Correct the cookie privacy statement before enabling this path. Prefer anonymous downloads; if authentication is needed, approve the target service and use a dedicated browser profile or narrowly scoped cookie export.

Risk: Future downloaded dependencies were not verified, and yt-dlp may be downloaded on first use when it is not installed.

Mitigation: Preinstall reviewed downloader versions before use to avoid automatic dependency resolution.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/vargai/skills/media-download)
- [Skill source repository homepage](https://github.com/vargHQ/skills/tree/main/media-download)
- [Pinterest moodboard presets](references/pinterest-presets.md)
- [Media download guide](https://varg.ai/how-to/skills/media-download)

## Skill Output:

**Output Type(s):** [Files]

**Output Format:** [Local MP4, MP3, and image files, with saved file paths reported as text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Files are saved to a selected output directory; video quality, audio-only, playlist, and Pinterest item-count options are available.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
