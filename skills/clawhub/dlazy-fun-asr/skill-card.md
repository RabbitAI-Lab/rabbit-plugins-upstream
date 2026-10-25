## Description:

Transcribes recordings with Alibaba Bailian Fun-ASR, supporting Chinese, English, and other languages with automatic language detection and speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users use this skill to transcribe recordings for subtitles, transcripts, and meeting notes, with optional speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio recordings are uploaded to dLazy for cloud transcription.

Mitigation: Submit only recordings you are authorized to share, and review dLazy privacy terms and costs.

Risk: The dLazy API key is stored in local CLI configuration.

Mitigation: Protect access to the local configuration and rotate or revoke a key if it is exposed.

Risk: Transcription depends on an external CLI.

Mitigation: Review and use only a CLI distribution you trust.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI project homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Structured JSON transcription results, with an optional saved result asset]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Language selection, optional speaker diarization and audio-event tagging, and asynchronous task support.]

## Skill Version(s):

1.3.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
