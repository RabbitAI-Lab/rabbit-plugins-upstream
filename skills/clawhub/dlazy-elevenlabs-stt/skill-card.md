## Description:

Transcribes audio with ElevenLabs scribe_v1, with automatic language detection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators can transcribe audio for subtitles, meeting notes, and other text records, with optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio submitted for transcription is uploaded to dLazy storage and processed by its hosted service; its privacy and retention terms were not fully verified.

Mitigation: Review dLazy's privacy and retention terms before submitting confidential recordings, and submit only audio approved for cloud processing.

Risk: Use of the hosted service may incur account charges, and requests require a stored dLazy API key.

Mitigation: Check account costs before running the transcription and protect the API key; rotate or revoke it if exposed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI project (linked in skill metadata; server provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON transcription response, with optional speaker diarization data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task identifier when asynchronous mode is used.]

## Skill Version(s):

1.3.38 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
