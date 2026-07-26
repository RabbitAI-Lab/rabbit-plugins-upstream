## Description: <br>
High-quality voice synthesis with 18 personas, 32 languages, sound effects, batch processing, and voice design using ElevenLabs API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and content creators use this skill to synthesize speech, generate sound effects, batch-process text, design voice previews, and configure ElevenLabs voice settings for agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credential storage is under-scoped or inconsistently documented. <br>
Mitigation: Prefer ELEVEN_API_KEY or ELEVENLABS_API_KEY environment variables over setup-created config.json or a skill-local .env file. <br>
Risk: Untrusted batch JSON and output paths can create unsafe local file handling. <br>
Mitigation: Review batch files before use and keep generated outputs inside a dedicated directory. <br>
Risk: Sensitive text, prompts, and limited local usage records may be exposed to ElevenLabs or retained locally. <br>
Mitigation: Avoid submitting sensitive content unless acceptable for the ElevenLabs API and clear local usage records when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/robbyczgw-cla/skills/elevenlabs-voices) <br>
- [ElevenLabs API documentation](https://docs.elevenlabs.io) <br>
- [ElevenLabs Voice Library](https://elevenlabs.io/voice-library) <br>
- [ElevenLabs Sound Generation API](https://elevenlabs.io/docs/api-reference/sound-generation) <br>
- [ElevenLabs Voice Generation API](https://elevenlabs.io/docs/api-reference/voice-generation) <br>
- [Voice guide](references/voice-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Audio files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; scripts write MP3 audio and JSON configuration or usage files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and an ElevenLabs API key via ELEVEN_API_KEY or ELEVENLABS_API_KEY.] <br>

## Skill Version(s): <br>
2.1.6 (source: frontmatter, package.json, CHANGELOG, released 2026-03-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
