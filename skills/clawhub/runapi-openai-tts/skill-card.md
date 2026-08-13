## Description:

Generate MP3 speech with OpenAI TTS through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate speech audio through RunAPI, either for one-off MP3 deliverables through the CLI or for application integration through the SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompt text or media inputs to RunAPI/OpenAI and may incur paid requests.

Mitigation: Use it only when that service use and billing exposure are acceptable, and authenticate with an approved RunAPI API key or saved CLI configuration.

Risk: Generated audio deliverables are downloaded from service-controlled links.

Mitigation: Validate downloaded files are non-empty and match the expected audio MIME type before treating them as complete deliverables.

## Reference(s):

- [RunAPI OpenAI TTS model homepage](https://runapi.ai/models/openai-tts)
- [OpenAI TTS model overview, pricing, and rate limits](https://runapi.ai/models/openai-tts.md)
- [OpenAI provider overview](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [OpenAI TTS SDK integration](https://github.com/runapi-ai/openai-tts-sdk)
- [tts-1 variant](https://runapi.ai/models/openai-tts/tts-1.md)
- [tts-1-hd variant](https://runapi.ai/models/openai-tts/tts-1-hd.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MP3 audio files and preserves non-media service responses in their returned format.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
