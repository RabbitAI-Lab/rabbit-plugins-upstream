## Description:

High-quality voice synthesis with 18 personas, 32 languages, sound effects, batch processing, and voice design using ElevenLabs API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and agents use this skill to generate speech, sound effects, and voice previews through ElevenLabs, including multilingual, streaming, and batch audio workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill loads API keys from environment variables and skill-local files, and the setup wizard can store a key in config.json.

Mitigation: Prefer environment variables or a credential manager, restrict local file permissions, and avoid committing config.json or .env.

Risk: Text prompts and speech content are sent to ElevenLabs for audio generation.

Mitigation: Avoid sensitive, confidential, or regulated text in prompts unless the deployment has approved ElevenLabs for that data.

Risk: Usage tracking can retain request metadata and prompt snippets in .usage.json.

Mitigation: Review, reset, or delete .usage.json when prompt history should not be retained.

Risk: OpenClaw built-in TTS and the skill scripts use different accepted API key environment names.

Mitigation: Set the variable required by the path being used and test with non-sensitive sample text before relying on the integration.

## Reference(s):

- [ElevenLabs](https://elevenlabs.io)
- [ElevenLabs API Documentation](https://docs.elevenlabs.io)
- [ElevenLabs Voice Library](https://elevenlabs.io/voice-library)
- [ElevenLabs Sound Effects API](https://elevenlabs.io/docs/api-reference/sound-generation)
- [ElevenLabs Voice Design API](https://elevenlabs.io/docs/api-reference/voice-generation)
- [Voice Guide](references/voice-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/robbyczgw-cla/skills/elevenlabs-voices)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; generated audio is saved as MP3 files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ElevenLabs API calls and may create local config.json, .env, .usage.json, MP3 outputs, samples, and batch output directories.]

## Skill Version(s):

2.2.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
