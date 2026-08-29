## Description:

Transcribes a video with word-level timings, translates the subtitles, burns them into the video, and optionally adds a fitted dub track using dLazy tools and local ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate video subtitles, burn translated SRT captions into media, and optionally create a dubbed audio track aligned to the original timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media and extracted audio are uploaded to dLazy API and media storage for processing.

Mitigation: Use the skill only with media the user is comfortable sending to dLazy, and review dLazy service terms before processing sensitive content.

Risk: dLazy API credentials may be stored locally in the CLI configuration file.

Mitigation: Protect the local configuration file, rotate or revoke keys from the dLazy dashboard when needed, or use the DLAZY_API_KEY environment variable for per-invocation credentials.

Risk: Translation, transcription, and dubbing calls can consume paid dLazy credits, especially for longer videos or per-segment TTS dubbing.

Mitigation: Confirm cost expectations before processing long media and use dry-run or credit-estimation options when available.

Risk: The workflow runs ffmpeg and ffprobe locally and writes media outputs in the chosen working directory.

Mitigation: Run commands from the intended media directory and review input and output paths before execution.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands and generated media/subtitle files when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces SRT subtitle files and MP4 video outputs through local ffmpeg plus dLazy API calls.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
