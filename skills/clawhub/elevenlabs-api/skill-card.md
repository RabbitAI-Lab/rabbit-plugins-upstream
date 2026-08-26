## Description:

ElevenLabs API integration with managed authentication for text-to-speech, voice cloning, sound effects, and audio processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call ElevenLabs through Maton for speech generation, voice cloning, sound effects, transcription, audio isolation, and related account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger write, delete, voice-cloning, or billed generation requests in a connected ElevenLabs account.

Mitigation: Use OAuth where possible, default to read/list calls, check the target connection, and require explicit user approval before any write, delete, voice-cloning, or billed generation request.

Risk: Using raw HTTP without the Maton CLI can expose a long-lived Maton API key through environment variables, logs, shell history, or process listings.

Mitigation: Prefer OAuth and the Maton CLI credential store; when raw HTTP is unavoidable, never print, persist, log, or pass the key on the command line.

Risk: Multiple Maton profiles or ElevenLabs connections can route a request to the wrong account.

Mitigation: Verify authentication with Maton, list active ElevenLabs connections, and pin the intended profile or connection before taking account-specific actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/elevenlabs-api)
- [ClawHub Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ElevenLabs API Documentation](https://elevenlabs.io/docs/api-reference)
- [ElevenLabs Developer Portal](https://elevenlabs.io/developers)
- [ElevenLabs Models Overview](https://elevenlabs.io/docs/overview/models)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or retrieve audio, transcription, metadata, and account data through ElevenLabs API calls.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
