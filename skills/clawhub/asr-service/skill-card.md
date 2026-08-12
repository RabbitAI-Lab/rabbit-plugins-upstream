## Description:

SenseVoice-Small ASR for Chinese speech recognition, speaker diarization, and SRT/VTT subtitle output through an IFF-managed FunASR service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vincentlau2046-sudo](https://clawhub.ai/user/vincentlau2046-sudo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to transcribe local audio files with SenseVoice-Small, including optional language selection, speaker labels, and SRT or VTT subtitle text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected audio files are sent to the configured ASR endpoint for transcription.

Mitigation: Keep the default localhost endpoint unless a remote ASR service is explicitly trusted.

Risk: The skill may start the local IFF/FunASR service when transcription is requested.

Mitigation: Install it only when the local service is intended, review the service configuration, and stop IFF when it is no longer needed.

## Reference(s):

- [ClawHub asr-service skill page](https://clawhub.ai/vincentlau2046-sudo/skills/asr-service)
- [FunASR](https://github.com/modelscope/FunASR)
- [InferFabric](https://github.com/vincentlau2046-sudo/inferfabric)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions]

**Output Format:** [Plain text, JSON, SRT, or VTT strings, with CLI output on stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcription results may include language, duration, timestamped segments, and speaker labels when verbose output or diarization is requested.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
