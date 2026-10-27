## Description:

Transcribes audio and creates timed Chinese–English subtitles for audio and video files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bjbook](https://clawhub.ai/user/bjbook)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to transcribe recordings or prepare timed Chinese–English SRT subtitles for audio and video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The subtitle translation workflow executes a generated Python file.

Mitigation: Review or replace that step so translated segments are written directly as JSON rather than executed as generated code.

Risk: Transcription may install a package and download a Whisper model on first use.

Mitigation: Require approval before dependency installation or model downloads and review the configured download source.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bjbook/skills/zhz-subtitle)
- [Skill homepage](http://openclaw.bjbook.net/)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Plain-text transcript or bilingual SRT subtitles, with timestamped JSON and intermediate SRT files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Subtitle order, transcription model size, and source language can be selected.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
