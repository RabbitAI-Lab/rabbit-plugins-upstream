## Description:

ElevenLabs scribe_v1 transcribes speech with language detection and optional speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can transcribe audio for subtitles, meeting notes, and other records, with optional speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI package and its credential handling were not inspected in the supplied security evidence.

Mitigation: Review the dLazy CLI project and consider whether you trust its authentication flow before installing or configuring it.

Risk: Local audio files supplied for transcription are uploaded to dLazy-hosted media storage.

Mitigation: Only submit recordings you are permitted to share with the service, and review dLazy's service terms before use.

## Reference(s):

- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON containing transcription text and optional speaker diarization]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcription output may be returned asynchronously when requested.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
