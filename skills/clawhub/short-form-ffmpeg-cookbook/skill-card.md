## Description:

Provides tested FFmpeg commands to crop video to vertical 1080×1920, burn captions, trim and join clips, and mix background music with voice ducking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Developers and creators use this skill to prepare short-form video for Reels, TikTok, and Shorts with FFmpeg commands for vertical framing, subtitles, clip edits, and music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the varg cloud FFmpeg option may share media URLs and incur credits; retention details are unspecified.

Mitigation: Use local FFmpeg for private footage. Before cloud processing, confirm the URLs may be shared and review charges and data handling.

Risk: The README also describes installing a separate 73-skill plugin, and the external installers and plugin were not inspected.

Mitigation: Install this individual skill unless you intentionally want the broader plugin, and review installer and plugin contents before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/short-form-ffmpeg-cookbook)
- [Project homepage](https://github.com/vargHQ/skills/tree/main/short-form-ffmpeg-cookbook)
- [Burn captions with FFmpeg](https://skills.varg.ai/burn-captions-with-ffmpeg/)
- [Crop a video to vertical](https://skills.varg.ai/crop-a-video-to-vertical-with-ffmpeg/)
- [Trim and join video clips](https://skills.varg.ai/trim-and-join-video-clips-with-ffmpeg/)
- [Add music to a video](https://skills.varg.ai/add-music-to-a-video-with-ffmpeg/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline FFmpeg command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands accept video, subtitle, and optional music file paths; recipes describe 1080×1920 vertical MP4 workflows.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
