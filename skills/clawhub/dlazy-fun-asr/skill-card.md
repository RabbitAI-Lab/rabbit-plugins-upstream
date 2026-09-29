## Description:

Transcribes recordings with Fun-ASR for subtitles, transcripts, and meeting notes, with language and speaker options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and teams use this skill to transcribe recordings for subtitles, written transcripts, and meeting notes, with optional speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio or other local media selected by the user may be uploaded to dLazy's cloud service.

Mitigation: Review recordings and obtain appropriate authorization before sending them to the service.

Risk: Authentication may persist a dLazy API key in local configuration.

Mitigation: Use the DLAZY_API_KEY environment variable if a persistent local key is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON response containing transcription output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization and audio-event tagging; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
