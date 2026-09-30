## Description:

Transcribes audio with ElevenLabs scribe_v1, supporting language detection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can transcribe audio for subtitles, transcripts, and meeting notes, with optional speaker separation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files or URLs supplied for transcription may be sent to dLazy's hosted service.

Mitigation: Only submit audio you are authorized to share with the service.

Risk: Logging in can store a dLazy API key locally.

Mitigation: Use a per-command DLAZY_API_KEY where appropriate, and rotate or revoke the key if needed.

Risk: Installing the external dLazy CLI introduces a third-party software dependency.

Mitigation: Review the pinned @dlazy/cli package before installing it globally.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON transcription result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker separation; asynchronous calls return a task ID for later retrieval.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
