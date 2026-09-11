## Description:

Transcribes video with word-level timings, translates subtitles, burns them into an MP4, and optionally creates a timing-fitted dubbed audio track using dLazy tools and local ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and localization teams use this skill to translate video speech into subtitles and, when requested, generate a dubbed MP4 aligned to the original timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads selected media to third-party dLazy services for transcription, translation, and speech synthesis.

Mitigation: Use only media that is appropriate to send to dLazy services, and review dLazy service terms before processing sensitive content.

Risk: The skill installs or executes a third-party CLI and may save API credentials in the user's local dLazy configuration.

Mitigation: Prefer npx or an isolated project for one-off runs, review the CLI source before installation, and use DLAZY_API_KEY when a saved API key is not desired.

Risk: ffmpeg commands create output files in the working directory and can overwrite files when run with replacement flags.

Mitigation: Run the workflow in a dedicated directory and review generated filenames before executing media-processing commands.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash commands and generated media/subtitle file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces SRT subtitle files and MP4 outputs through local ffmpeg and dLazy CLI calls.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
