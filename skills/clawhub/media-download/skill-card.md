## Description:

Download videos, audio, and Pinterest images to local files from links or searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can save online videos, audio, playlists, and Pinterest images locally for workflows such as moodboards and visual references, when they have the right to save and use the content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-session and cookie options can involve sending cookies to target sites.

Mitigation: Review these options before use, and only access browser cookies with the user's authorization.

Risk: The scanner flags unpinned installer dependencies, and its review was partial with two references unresolved.

Mitigation: Review installer sources and versions, and resolve the remaining references before relying on the security assessment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/media-download)
- [Project homepage (listed in metadata)](https://github.com/vargHQ/skills/tree/main/media-download)
- [Pinterest moodboard presets](references/pinterest-presets.md)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [Local MP4, MP3, and image files with saved file paths and brief status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports links, playlists, Pinterest searches, and Pinterest URLs; output location and quality can be selected.]

## Skill Version(s):

1.0.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
