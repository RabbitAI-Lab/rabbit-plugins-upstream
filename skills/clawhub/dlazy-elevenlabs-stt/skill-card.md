## Description:

ElevenLabs scribe_v1 speech-to-text with automatic language detection and optional speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to transcribe audio with ElevenLabs scribe_v1, including automatic language detection and optional speaker diarization, for subtitles, transcripts, and meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a billable dLazy API key that may be stored in the local CLI config, and the security evidence reports that the installed CLI did not appear to enforce the file-permission protection claimed by the skill text.

Mitigation: Prefer per-invocation DLAZY_API_KEY on shared or sensitive machines, verify local config permissions before use, and rotate or revoke any exposed key.

Risk: Audio URLs or local audio files supplied to the skill may be uploaded to dLazy's hosted service for processing.

Mitigation: Only provide audio intended for upload to the service, and avoid sensitive audio unless the user's data-handling requirements permit it.

Risk: The skill depends on installing or invoking the third-party @dlazy/cli package through npm or npx.

Mitigation: Review the pinned package and source before installation, and prefer the pinned version declared by the release evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON result envelope from the dLazy CLI, with optional async task status when no-wait mode is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; provided audio URLs or local audio files may be sent to dLazy-hosted endpoints.]

## Skill Version(s):

1.3.7 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
