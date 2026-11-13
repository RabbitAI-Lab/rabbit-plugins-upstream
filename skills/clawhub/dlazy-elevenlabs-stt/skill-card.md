## Description:

Transcribes audio with ElevenLabs scribe_v1, with automatic language detection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People who need transcripts can use this skill to turn audio into text for subtitles, meeting notes, and other transcription tasks, with optional speaker labels. It requires a dLazy account and API authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the stated transcription purpose and the dLazy login setup, and says the review was partial.

Mitigation: Confirm the dLazy authentication setup fits your use, and review referenced components that were unavailable to the scanners before relying on the skill.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON response containing transcription results, with optional speaker diarization fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task ID when run with --no-wait.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
