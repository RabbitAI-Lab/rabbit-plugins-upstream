## Description:

Transcribes audio with ElevenLabs scribe_v1, with automatic language detection and optional speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating subtitles, transcripts, or meeting notes use this skill to transcribe audio with ElevenLabs scribe_v1 and optionally separate speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and flagged a mismatch between the transcription purpose and the documented dLazy CLI login flow; audio and credentials are handled through the dLazy service.

Mitigation: Review the CLI and confirm dLazy's login and data-handling practices before providing credentials or sensitive audio.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON containing transcription results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may be asynchronous when requested; the skill documentation shows an outputs array and an optional task status.]

## Skill Version(s):

1.3.43 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
