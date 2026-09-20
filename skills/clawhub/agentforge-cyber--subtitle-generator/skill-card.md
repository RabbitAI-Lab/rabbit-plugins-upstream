## Description:

Generates multilingual SRT or WebVTT subtitles from video or audio using Faster-Whisper first and OpenAI Whisper as a fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentforge-cyber](https://clawhub.ai/user/agentforge-cyber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to transcribe video or audio and create aligned subtitle files in SRT or WebVTT format. It is intended for workflows that need automatic subtitle generation, language detection, ASR-based transcription, and subtitle timing cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically install persistent ASR dependencies into a user-level virtual environment.

Mitigation: Require explicit approval before first-run package installation and pin dependency versions before deployment.

Risk: The skill describes cleanup and process-management behavior around background execution.

Mitigation: Limit cleanup to skill-owned temporary files and track only process IDs created by this skill.

Risk: Completion notifications may include generated file names or paths.

Mitigation: Make notifications opt-in and disclose what file names or paths will be sent.

Risk: The authoritative security verdict is suspicious.

Mitigation: Review and scan the skill before installation or operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentforge-cyber/skills/subtitle-generator)
- [Publisher profile](https://clawhub.ai/user/agentforge-cyber)
- [FFmpeg downloads](https://ffmpeg.org/download.html)
- [PyTorch Metal package index](https://download.pytorch.org/whl/metal)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown/text guidance with bash commands; generated subtitle files in SRT or WebVTT format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes subtitle output next to the source media file and can emit completion or failure notifications when requested.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
