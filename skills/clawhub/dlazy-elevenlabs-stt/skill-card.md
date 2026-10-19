## Description:

Transcribes audio using ElevenLabs scribe_v1, with language selection and optional speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents can transcribe selected audio for subtitles, meeting notes, or other written records, with optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected audio and request parameters are sent to dLazy-hosted services.

Mitigation: Avoid sensitive audio unless dLazy's terms and data handling are acceptable to you.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Protect the local key and use per-invocation authentication when persistent storage is unsuitable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON containing transcription results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization; asynchronous requests can return a task ID before results are ready.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
