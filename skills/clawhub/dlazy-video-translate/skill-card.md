## Description:

Transcribes a video with word-level timings, translates the subtitles, burns them into the video, and optionally lays down a fitted dub track using dLazy tools and local ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and localization teams use this skill to convert an input video into translated subtitles and, when requested, a dubbed MP4 aligned to the source timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected audio or video files are uploaded to dLazy services for transcription, translation, and optional dubbing.

Mitigation: Confirm the source file, target language, and optional dubbing request before running the pipeline, and use only media that is approved for third-party processing.

Risk: The workflow requires a dLazy API key and can consume dLazy credits.

Mitigation: Prefer the DLAZY_API_KEY environment variable for one-off jobs on shared machines and review dry-run or credit estimates before paid calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces SRT subtitle files and MP4 video files during agent execution.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
