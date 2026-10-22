## Description:

Transcribes video, translates subtitles into Simplified Chinese, burns them into the video, and optionally adds a timing-aligned dubbed audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can transcribe videos, translate subtitle text into Simplified Chinese, and produce a subtitled MP4; they can also request a timing-aligned dubbed audio track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can silently replace existing files in the video working folder.

Mitigation: Use a fresh working folder, check for output-name collisions, and get approval before replacing any existing file.

Risk: Local media is uploaded to dLazy for processing and service calls can incur charges.

Mitigation: Use only media approved for cloud processing, confirm the target language, review estimated usage, and decide whether to save the API key locally.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Files, Media, Text]

**Output Format:** [MP4 video and SRT subtitle files; optional WAV audio segments and dubbed MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dubbing stage is optional; video and audio are uploaded for cloud processing.]

## Skill Version(s):

1.0.25 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
