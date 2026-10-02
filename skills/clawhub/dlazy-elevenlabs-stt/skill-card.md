## Description:

Transcribes audio with ElevenLabs scribe_v1, with language detection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams transcribe audio for subtitles, meeting notes, and other written records, optionally distinguishing speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio and transcription parameters are sent to dLazy and ElevenLabs cloud services.

Mitigation: Avoid sensitive audio unless the service terms and your organization's data rules permit it.

Risk: Configuring the CLI stores a dLazy API key locally; global installation leaves the CLI installed.

Mitigation: Protect the local key and consider the pinned npx command or reviewing the pinned CLI source instead of global installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Transcription text returned in a JSON result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker separation; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.24 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
