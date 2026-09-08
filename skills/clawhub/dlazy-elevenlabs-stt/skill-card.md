## Description:

ElevenLabs scribe_v1 speech-to-text skill for transcribing audio with automatic language detection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to invoke dLazy's ElevenLabs STT workflow for subtitles, transcripts, and meeting notes from audio inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected audio or media inputs to dLazy-hosted endpoints.

Mitigation: Use it only for data that may be processed by dLazy-hosted services and review organization data-sharing requirements before invocation.

Risk: The skill requires installing or running @dlazy/cli from npm.

Mitigation: Review the package source and pinned install command before installing or running the CLI.

Risk: The skill stores or uses a dLazy API key and includes payment or recharge guidance.

Mitigation: Treat API-key setup, key storage, rotation, revocation, and recharge actions as explicit user choices.

Risk: Security review flagged confusing broader data-upload language relative to the advertised speech-to-text purpose.

Mitigation: Confirm the actual files and parameters being sent before execution and avoid passing unrelated local media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI may return a synchronous JSON output object or an asynchronous task identifier for polling.]

## Skill Version(s):

1.3.14 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
