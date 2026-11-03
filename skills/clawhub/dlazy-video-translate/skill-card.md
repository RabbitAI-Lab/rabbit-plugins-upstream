## Description:

Transcribes a video, translates its subtitles, burns them into the video, and optionally creates a time-aligned dubbed audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People localizing video can generate translated subtitles and a finished subtitled video, with an optional dubbed audio track. The workflow supports translation from a video's spoken language into a chosen target language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow's commands can overwrite existing files.

Mitigation: Use a fresh working folder and confirm before replacing existing outputs.

Risk: Video and audio files are uploaded to dLazy storage for processing.

Mitigation: Confirm the target language and dLazy upload policy before sending media.

Risk: The external CLI package and service behavior are unverified.

Mitigation: Review the CLI source and service terms before use.

Risk: CLI authentication normally saves an API key in the user configuration.

Mitigation: Use the documented DLAZY_API_KEY environment variable when you do not want to persist credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, Subtitle files, Audio files (optional)]

**Output Format:** [MP4 video with burned-in subtitles, SRT subtitle files, and optional dubbed MP4/WAV audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the source video's timing; dubbing is optional and may incur additional service costs.]

## Skill Version(s):

1.0.29 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
