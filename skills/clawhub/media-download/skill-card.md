## Description:

Download videos, audio and images to local files from a link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[securityqq](https://clawhub.ai/user/securityqq)

### License/Terms of Use:

MIT

## Use Case:

External users and developers can save videos, audio, and Pinterest images from links or searches as local files, including playlists and visual references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated downloads send matching browser session cookies to the download site; the skill's cookie assurance warrants review.

Mitigation: Prefer anonymous downloads. Before using authentication, review cookie handling and use a dedicated browser profile or narrowly scoped cookie export.

Risk: When yt-dlp is missing, the script can download a standalone build on first use.

Mitigation: Preinstall a verified yt-dlp version before running downloads.

## Reference(s):

- [Pinterest moodboard presets](references/pinterest-presets.md)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [Local video, audio, and image files; saved file paths printed as text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media is saved locally; format depends on the selected download mode.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
