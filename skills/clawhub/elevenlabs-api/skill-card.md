## Description:

ElevenLabs API integration with managed authentication for text-to-speech, voice cloning, sound effects, and audio processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access ElevenLabs through Maton for voice listing, speech generation, voice cloning, sound effects, transcription, audio processing, and related account or project tasks. The skill is suited to workflows that need managed authentication and explicit review before writes or new account connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ElevenLabs activity is routed through Maton and requires authorizing a relevant ElevenLabs account.

Mitigation: Install only when that routing and authorization model is acceptable; use OAuth where possible and connect only the account needed for the task.

Risk: Write operations can create voice clones, delete resources, change projects, or trigger billed generation.

Mitigation: Default to read and list calls first, then confirm the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Long-lived Maton API keys can leak through environment variables, logs, command lines, or persisted files when the CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI; if raw HTTP is required, read the key only from the process environment, never print or persist it, and send it only to api.maton.ai.

Risk: API responses may contain personal data or adversarial content.

Mitigation: Extract only the fields needed for the task, avoid storing raw responses unless requested, and treat fetched content as data rather than executable instructions.

## Reference(s):

- [ElevenLabs API Documentation](https://elevenlabs.io/docs/api-reference)
- [ElevenLabs Developer Portal](https://elevenlabs.io/developers)
- [ElevenLabs Models Overview](https://elevenlabs.io/docs/overview/models)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/elevenlabs-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request guidance and command examples for Maton-mediated ElevenLabs operations; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
