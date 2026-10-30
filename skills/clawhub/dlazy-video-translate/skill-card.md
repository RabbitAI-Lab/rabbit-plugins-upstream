## Description:

Transcribes a video with word-level timings, translates the subtitles, burns them in, and optionally creates a fitted dubbed audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and localization teams use this skill to produce translated, burned-in subtitles and, when requested, a fitted dubbed audio track from a video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can overwrite existing files in its working directory.

Mitigation: Use a fresh output directory and get explicit approval before replacing existing files.

Risk: Media is uploaded to dLazy for cloud processing, and tool use may incur charges.

Mitigation: Use the service only for media you are comfortable uploading, confirm the target language, and consider expected usage charges and saved API credentials before running.

## Reference(s):

- [dLazy CLI source project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [MP4 video files, SRT subtitle files]

**Output Format:** [MP4 video with burned-in translated subtitles; SRT subtitles; optional dubbed MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dubbing is optional and runs only when requested.]

## Skill Version(s):

1.0.28 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
