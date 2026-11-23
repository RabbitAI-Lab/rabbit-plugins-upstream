## Description:

Transcribes a video with word-level timings, translates the subtitles into Simplified Chinese, burns them into the video, and optionally adds a timing-matched dubbed audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and media teams use this skill to turn spoken video into translated subtitles, a captioned MP4, and, when requested, a dubbed audio track aligned to the original timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented ffmpeg commands use overwrite flags and may replace files at their output paths.

Mitigation: Use a dedicated working directory, check output filenames before running commands, and keep backups of files that matter.

Risk: ClawScan reports a high-confidence risk of overwriting existing files and an inaccurate claim about where commands write data; its scan was partial and does not establish malicious intent.

Mitigation: Review the commands and their input and output paths before execution, inspect the working directory, and follow the security guidance for authentication and installation data.

Risk: The skill documents uploading local audio and media files to dLazy services for processing.

Mitigation: Use only media you are permitted to share with the service, and review dLazy's service terms before uploading sensitive content.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)

## Skill Output:

**Output Type(s):** [Files]

**Output Format:** [MP4 video with SRT subtitle files; optional WAV audio segments and dubbed MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an input video and chosen source language; subtitles are translated into Simplified Chinese. Dubbing is optional and runs only when requested.]

## Skill Version(s):

1.0.35 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
