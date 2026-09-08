## Description:

Generates MP3 speech with OpenAI TTS through RunAPI for one-off speech generation or application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate text-to-speech audio through RunAPI, either as one-off MP3 artifacts via the CLI or as application integrations through an SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests may submit text content to RunAPI/OpenAI TTS and may consume paid API credits.

Mitigation: Use a dedicated RunAPI key where possible, review request.json for sensitive text before submission, and avoid additional paid submissions without user authorization.

Risk: Interactive browser login can authenticate an agent session if used unexpectedly.

Mitigation: Prefer RUNAPI_API_KEY or saved CLI configuration, and use browser login only when explicitly requested.

Risk: A successful service status may not guarantee the requested audio deliverable is valid.

Mitigation: Download every requested media deliverable and verify each file is non-empty and has the expected audio MIME type.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-openai-tts)
- [RunAPI OpenAI TTS homepage](https://runapi.ai/models/openai-tts)
- [OpenAI TTS model overview, pricing, and rate limits](https://runapi.ai/models/openai-tts.md)
- [OpenAI provider overview](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [OpenAI TTS SDK integration](https://github.com/runapi-ai/openai-tts-sdk)
- [tts-1 variant](https://runapi.ai/models/openai-tts/tts-1.md)
- [tts-1-hd variant](https://runapi.ai/models/openai-tts/tts-1-hd.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with shell commands, JSON request files, SDK code, and downloaded MP3 audio artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses and downloaded audio are verified against the discovered result contract.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
