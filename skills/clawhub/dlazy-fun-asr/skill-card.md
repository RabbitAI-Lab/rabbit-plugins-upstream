## Description:

Alibaba Bailian Fun-ASR recording transcription supports Chinese, English, and other languages, with automatic language detection and speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and productivity agents use this skill to invoke dLazy's Fun-ASR cloud transcription workflow for audio files or URLs, including optional speaker diarization and asynchronous polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files or URLs and task parameters are sent to dLazy cloud services for transcription.

Mitigation: Use only approved audio, confirm data handling requirements before upload, and use a revocable dLazy API key.

Risk: A global CLI install persists a local binary, and authentication can store an API key in the user's dLazy config file.

Mitigation: Prefer the documented npx invocation when a persistent install is not needed, and rotate or revoke API keys from the dLazy dashboard when access changes.

Risk: The documented default language is zh, which can produce lower-quality output for non-Chinese audio.

Mitigation: Set --language_code explicitly for non-Chinese transcription tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI can return asynchronous task IDs and hosted result assets for later polling or download.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
