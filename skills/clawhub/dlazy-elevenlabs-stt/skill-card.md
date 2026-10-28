## Description:

ElevenLabs scribe_v1 speech-to-text with automatic language detection and optional speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can transcribe audio with ElevenLabs scribe_v1, detect Chinese or English automatically, optionally separate speakers, and use the resulting text for subtitles, transcripts, or meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected recordings are uploaded to dLazy for transcription, which may expose confidential audio to an external service.

Mitigation: Upload only recordings approved for external processing, and review dLazy's privacy and retention terms before sending confidential audio.

Risk: The dLazy organization API key is saved in the local CLI configuration and could be exposed if that account or file is compromised.

Mitigation: Restrict access to the saved key, use an environment variable when appropriate, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [JSON transcription result with text and optional speaker diarization; optionally saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Language selection (Chinese or English); optional diarization; asynchronous task mode is available.]

## Skill Version(s):

1.3.35 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
