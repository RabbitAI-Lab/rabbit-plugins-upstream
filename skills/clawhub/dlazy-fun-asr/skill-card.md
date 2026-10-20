## Description:

Transcribes recordings with Fun-ASR for subtitles, transcripts, and meeting notes, with language selection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and teams use this skill to transcribe audio recordings for subtitles, written transcripts, and meeting notes, with optional speaker identification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files provided for transcription may be uploaded to dLazy, and result files may be hosted there.

Mitigation: Only submit recordings you are authorized to share and check whether hosted processing is appropriate for sensitive audio.

Risk: Signing in can save an API key in the local dLazy CLI configuration.

Mitigation: Protect the local configuration or supply DLAZY_API_KEY per invocation to avoid saving the key locally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Transcription text in a JSON response; optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization and audio event tags; asynchronous requests may return a task ID.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
