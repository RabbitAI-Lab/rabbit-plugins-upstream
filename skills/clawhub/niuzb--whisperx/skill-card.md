## Description:

WhisperX provides local speech-to-text transcription using OpenAI Whisper, with high-quality offline recognition, no API key required, word-level timestamps, and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[niuzb](https://clawhub.ai/user/niuzb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to transcribe local audio files or voice messages into text with optional word-level timing and speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing WhisperX brings Python package and ML dependency supply-chain exposure.

Mitigation: Install in an isolated environment, pin the WhisperX version, and review dependencies before deployment.

Risk: First use may download speech models into the local Whisper cache before offline transcription works.

Mitigation: Pre-cache approved models in controlled environments and account for local model storage.

Risk: Optional speaker diarization may require a HuggingFace token.

Mitigation: Enable diarization only when needed and handle any required token as a secret.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/niuzb/skills/whisperx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash commands and transcription text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include word-level timestamps when requested and supported by WhisperX.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
