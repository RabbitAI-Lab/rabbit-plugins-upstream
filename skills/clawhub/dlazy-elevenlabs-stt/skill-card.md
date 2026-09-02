## Description:

ElevenLabs scribe_v1 speech-to-text with auto language detection and optional speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to transcribe audio with ElevenLabs scribe_v1 through the dLazy CLI, including optional language selection and speaker diarization for subtitles, transcripts, and meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files, audio URLs, and invocation parameters are sent to a hosted dLazy/ElevenLabs service for transcription.

Mitigation: Use the skill only with audio that is appropriate for the hosted service and review organizational data-handling requirements before sending sensitive recordings.

Risk: `dlazy login` stores an organization API key on the local machine.

Mitigation: Use OS account protections for the local config, rotate or revoke the key from dLazy when access changes, and prefer `npx @dlazy/cli@1.2.3` when a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON responses and text transcripts, with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when invoked with --no-wait.]

## Skill Version(s):

1.3.11 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
