## Description:

Generate MP3 speech with OpenAI TTS through RunAPI. Use for one-off speech generation or application integration. Prefer the RunAPI CLI for one-off requests and the target-language SDK for production integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate MP3 speech through RunAPI OpenAI TTS, either for one-off CLI requests or application integration through target-language SDKs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompt text is sent to RunAPI and the underlying OpenAI TTS provider for speech generation.

Mitigation: Confirm the user is comfortable using RunAPI for OpenAI TTS before sending prompt text or generating audio.

Risk: Authentication may rely on RUNAPI_API_KEY or saved RunAPI CLI configuration.

Mitigation: Keep API keys in environment variables or approved RunAPI configuration and avoid embedding credentials in code or request files.

Risk: Using the CLI as a production runtime layer can make integrations brittle.

Mitigation: Use the target-language RunAPI SDK for application and production integrations; reserve the CLI path for one-off generation, manual checks, and debugging.

## Reference(s):

- [RunAPI OpenAI TTS model page](https://runapi.ai/models/openai-tts)
- [Model overview](https://runapi.ai/models/openai-tts.md)
- [tts-1](https://runapi.ai/models/openai-tts/tts-1.md)
- [tts-1-hd](https://runapi.ai/models/openai-tts/tts-1-hd.md)
- [OpenAI provider page](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, SDK package names, and request-field details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to produce RunAPI SDK integration steps or one-off CLI requests that generate MP3 audio with RunAPI-managed audio URLs.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
