## Description:

Alibaba Bailian Fun-ASR transcribes recordings in Chinese, English, and other languages, with automatic language detection and speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to transcribe recordings for subtitles, transcripts, and meeting notes, with optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and did not establish how dLazy authentication relates to the stated transcription service.

Mitigation: Review the login setup and referenced package and configuration details before installing if that distinction matters to you.

Risk: Audio supplied as a local file path is uploaded to dLazy media storage, and request parameters are sent to its hosted API.

Mitigation: Avoid submitting sensitive recordings unless dLazy's data handling meets your requirements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source listed in skill metadata (release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON containing transcription results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Speaker information may be included when diarization is enabled; asynchronous mode can return a task identifier and status.]

## Skill Version(s):

1.3.39 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
