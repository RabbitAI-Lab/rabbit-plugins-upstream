## Description:

Transcribes audio with ElevenLabs scribe_v1, supporting automatic language detection and optional speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can transcribe audio for subtitles, searchable transcripts, and meeting notes, with optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio is sent to dLazy for cloud transcription and may contain sensitive information.

Mitigation: Review dLazy privacy terms before submitting sensitive recordings.

Risk: API usage may incur charges, and login stores an API key in local configuration.

Mitigation: Review usage costs; use the documented environment-variable option if you prefer not to store the key locally.

Risk: The skill relies on an external CLI package.

Mitigation: Review the pinned CLI release before installing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source (listed by the skill)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON response containing transcription results; asynchronous requests may return a task identifier and status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include speaker diarization; output may be returned asynchronously.]

## Skill Version(s):

1.3.33 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
