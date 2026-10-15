## Description:

Transcribes audio with ElevenLabs scribe_v1, with language selection and optional speaker diarization for subtitles and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to transcribe audio for subtitles, transcripts, and meeting notes, with optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio supplied as a file or URL is sent to dLazy's cloud service.

Mitigation: Review provider terms and avoid submitting sensitive recordings without appropriate approval.

Risk: A global CLI install or saved API key can persist on the device.

Mitigation: Consider on-demand npx use and a per-invocation DLAZY_API_KEY for sensitive workflows.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON response containing transcription results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization; asynchronous requests return a task identifier.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
