## Description:

Transcribes video with word-level timings, translates the subtitles, burns them into the video, and can optionally add a time-fitted dubbed audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and localization teams use this skill to create translated subtitles and, when requested, a dubbed version of a video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The processing commands can overwrite files with the same output names in the working directory.

Mitigation: Use a dedicated working directory or back up existing files before processing.

Risk: Source media and local files are uploaded to dLazy services for processing.

Mitigation: Use media that is authorized for upload, and review dLazy's service terms before processing sensitive content.

Risk: The translated subtitle language may not match the intended target language.

Mitigation: Confirm the requested target language before running the translation stage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, Subtitle files]

**Output Format:** [MP4 video and SRT subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Subtitles are produced by default; a dubbed audio track is optional.]

## Skill Version(s):

1.0.30 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
