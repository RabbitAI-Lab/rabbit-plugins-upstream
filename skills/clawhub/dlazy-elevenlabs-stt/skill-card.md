## Description:

Transcribes audio with ElevenLabs scribe_v1, with language detection and optional speaker diarization for subtitles and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill to transcribe audio for subtitles, transcripts, and meeting notes, optionally distinguishing speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external dLazy CLI package runs on the user's system.

Mitigation: Review the package before installation.

Risk: Audio supplied for transcription is uploaded to dLazy's cloud service.

Mitigation: Submit only audio you are comfortable uploading to dLazy.

Risk: Saving an API key with the CLI persists it in local configuration.

Mitigation: Use DLAZY_API_KEY per invocation if you prefer not to save the key locally.

Risk: The example uses --prompt while the listed audio option is --audio_url, which could cause incorrect invocations.

Mitigation: Check the CLI help and use the documented audio option before running a transcription.

## Reference(s):

- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON response containing transcription output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization; asynchronous requests can return a task ID instead of immediate output.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
