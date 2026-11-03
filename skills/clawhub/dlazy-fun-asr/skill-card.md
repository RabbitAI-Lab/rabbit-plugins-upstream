## Description:

Transcribes recordings with Alibaba Bailian Fun-ASR, with language detection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People who need searchable transcripts, subtitles, or meeting notes can submit recordings for transcription and optionally request speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recordings submitted for transcription are uploaded to dLazy's hosted service.

Mitigation: Submit only recordings you are comfortable sharing with dLazy, and review its data-handling terms before use.

Risk: Logging in saves the API key in the local CLI configuration.

Mitigation: Use the documented DLAZY_API_KEY environment variable when you prefer not to save the key in the CLI configuration, and rotate or revoke keys when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON transcription result with optional task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include speaker diarization and audio event tags; asynchronous mode may return a task identifier.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
