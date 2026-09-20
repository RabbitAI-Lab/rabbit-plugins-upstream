## Description:

The Subtitle Generator skill creates multilingual SRT or WebVTT subtitle files from video audio using Faster-Whisper first and OpenAI Whisper as a fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aqbjqtd](https://clawhub.ai/user/aqbjqtd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate timed subtitle files for video content, with optional language selection and automatic ASR engine selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First use may automatically create and reuse a persistent ~/.whisper-venv environment and install current package-index versions of Whisper-related dependencies.

Mitigation: Review dependency installation behavior before deployment, prefer pinned dependencies, and validate the virtual environment before reuse.

Risk: Long transcription jobs may run in the background and send completion events through OpenClaw with limited user control.

Mitigation: Ask for user approval before long-running setup or transcription jobs and narrow notification behavior to the intended session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aqbjqtd/skills/subtitle-generator)
- [Publisher profile](https://clawhub.ai/user/aqbjqtd)
- [FFmpeg downloads](https://ffmpeg.org/download.html)
- [PyTorch Metal wheel index](https://download.pytorch.org/whl/metal)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands, Guidance]

**Output Format:** [SRT or WebVTT subtitle files with progress and completion messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes the subtitle file next to the input video and can emit completion events when notification mode is enabled.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
