## Description:

ElevenLabs API integration with managed authentication for text-to-speech, voice cloning, sound effects, and audio processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to access ElevenLabs API capabilities through Maton-managed authentication for speech generation, voice management, audio processing, transcription, and related account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ElevenLabs API access is routed through Maton-managed authentication.

Mitigation: Install only when this routing is acceptable, use OAuth when possible, and review connection prompts before authorizing access.

Risk: Write, delete, voice-cloning, and billable generation actions can change account data or incur usage costs.

Mitigation: Confirm the target resource, payload, and intended effect before running any modifying or billable operation.

Risk: Broad or ambiguous account access can affect the wrong ElevenLabs connection or Maton profile.

Mitigation: Choose the narrowest available scopes and specify the intended connection or profile when multiple accounts are available.

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

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce ElevenLabs API responses, including JSON metadata and audio data, through the Maton gateway.]

## Skill Version(s):

1.2.0 (source: release metadata; artifact frontmatter metadata lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
