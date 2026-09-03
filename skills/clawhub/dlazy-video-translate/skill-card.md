## Description:

Transcribes a video with word-level timings, translates subtitles, burns them into the video, and optionally creates a fitted dub track using dLazy tools and local ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and localization teams use this skill to generate translated subtitle files and finished MP4 outputs from source videos. When dubbing is requested, it also guides creation of a time-fitted replacement audio track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio files are uploaded to dLazy services for processing.

Mitigation: Avoid sensitive media unless the user accepts the service privacy tradeoff.

Risk: The workflow may incur billed dLazy API calls for transcription, translation, and optional TTS.

Mitigation: Use dry-run estimates before execution and confirm the user wants to proceed with billable steps.

Risk: Authentication can save an API key in the local dLazy configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local storage is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with shell commands, JSON examples, SRT instructions, and media file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces SRT subtitle files and finished MP4 variants when the described workflow is executed.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
