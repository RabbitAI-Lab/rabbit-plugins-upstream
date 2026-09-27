## Description:

ElevenLabs scribe_v1 speech-to-text with automatic language detection and optional speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users can invoke this skill to transcribe audio with ElevenLabs scribe_v1, including optional speaker diarization for subtitles, transcripts, and meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI and sends selected audio or media inputs to dLazy-hosted endpoints.

Mitigation: Review the CLI package before installation and use the pinned npx invocation when you do not want a persistent global install.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when you do not want a saved key, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: The artifact examples include an incorrect --prompt invocation for a command whose inspected options use --audio_url.

Mitigation: Verify commands with dlazy elevenlabs-stt -h and pass audio input through --audio_url.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when invoked with --no-wait; saved result assets may be downloaded with --save.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
