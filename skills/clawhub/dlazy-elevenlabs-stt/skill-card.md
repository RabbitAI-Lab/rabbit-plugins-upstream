## Description:

Transcribes audio with ElevenLabs scribe_v1 through the dLazy CLI, with optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can transcribe audio for subtitles, transcripts, and meeting notes, with optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external dLazy CLI may store an API key locally.

Mitigation: Protect local credentials or provide the key per invocation; rotate or revoke exposed keys.

Risk: Audio files supplied for transcription are uploaded to dLazy-hosted endpoints.

Mitigation: Upload only audio you are authorized to share and check its sensitivity before processing.

Risk: Installing a global CLI retains an external executable on the system.

Mitigation: Review the pinned package before installing; use the documented npx form to avoid a persistent global binary.

Risk: The default language code is Chinese, which may not match the audio.

Mitigation: Set --language_code explicitly when Chinese is not intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON transcription result or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization; results may be saved to a local file.]

## Skill Version(s):

1.3.28 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
