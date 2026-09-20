## Description:

ElevenLabs scribe_v1 speech-to-text with automatic language detection and optional speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to call the dLazy ElevenLabs speech-to-text wrapper from an agent workflow, transcribing audio with optional language selection, speaker diarization, asynchronous polling, and result saving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files, URLs, parameters, and generated result data are sent to dLazy-hosted services rather than processed only locally.

Mitigation: Avoid uploading sensitive audio unless dLazy's terms fit the use case, and use dry-run or review command parameters before submitting data.

Risk: The skill requires a dLazy API key that may be stored in the local CLI configuration or supplied through an environment variable.

Mitigation: Use OS user permissions for the CLI config, avoid exposing DLAZY_API_KEY in shared logs or shells, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global npm install leaves the dLazy CLI available on the system beyond a single invocation.

Mitigation: Use the pinned npx invocation, npx @dlazy/cli@1.2.3, when a persistent global CLI install is not desired.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source link from artifact metadata](https://github.com/dlazy-ai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration guidance]

**Output Format:** [Markdown guidance with bash commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return asynchronous task identifiers, poll for completion, and save returned assets to a local path when requested.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
