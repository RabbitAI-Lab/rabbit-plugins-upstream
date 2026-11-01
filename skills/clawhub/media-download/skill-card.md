## Description:

Download video, audio, and image files from supported links, or collect Pinterest images from searches, boards, and profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can save media from supported links and collect Pinterest images for moodboards or visual references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local-only assurance needs review for authenticated downloads because browser or cookie-file credentials can authenticate network requests.

Mitigation: Before authenticated downloads, approve the specific browser or cookie file and intended destination. Prefer preinstalled, reviewed downloader versions.

## Reference(s):

- [ClawHub release](https://clawhub.ai/vargai/skills/media-download)
- [Publisher profile](https://clawhub.ai/user/vargai)
- [Skill homepage listed in metadata](https://github.com/vargHQ/skills/tree/main/media-download)
- [Pinterest moodboard presets](artifact/references/pinterest-presets.md)

## Skill Output:

**Output Type(s):** [Media files, Text (saved-file paths)]

**Output Format:** [Local video, audio, and image files; saved-file paths printed as text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Videos are saved as MP4 when available; audio-only downloads are MP3. Output location can be selected.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
