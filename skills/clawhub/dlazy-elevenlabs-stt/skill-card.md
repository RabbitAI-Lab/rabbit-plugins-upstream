## Description:

ElevenLabs scribe_v1 speech-to-text with auto language detection and optional speaker diarization, for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can transcribe audio for subtitles, meeting notes, and general speech-to-text tasks, with optional speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and raised questions about how the dLazy CLI login flow relates to the transcription task.

Mitigation: Review the CLI authentication flow before authorizing it; use a dedicated API key and revoke it when no longer needed.

Risk: The skill sends requests to dLazy's hosted API and may upload local audio files to its media storage.

Mitigation: Avoid submitting sensitive audio unless its transfer is permitted, and review the service terms and data handling first.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key settings](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON response containing transcription output or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports language selection and optional speaker diarization; asynchronous mode can return a task identifier.]

## Skill Version(s):

1.3.44 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
