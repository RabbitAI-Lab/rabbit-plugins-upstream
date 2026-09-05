## Description:

Call the DeepSeek API (deepseek-v4-pro, deepseek-v4-flash, and deepseek-v4-flash-vision-exp) through RunAPI using OpenAI-compatible Chat Completions and Responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to call DeepSeek models through RunAPI for text, image input, streaming, and a verified custom-function path while keeping request shapes within supported protocol boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and provided image URLs are sent through RunAPI.

Mitigation: Confirm the intended data flow before use and avoid sending sensitive content unless the RunAPI account and project are approved for that data.

Risk: Using a broad or unrelated API credential can expand impact if the key is exposed.

Mitigation: Use a RunAPI-scoped API key with OPENAI_BASE_URL set to https://runapi.ai/v1.

## Reference(s):

- [DeepSeek on RunAPI ClawHub page](https://clawhub.ai/runapi-ai/skills/runapi-deepseek)
- [RunAPI DeepSeek model page](https://runapi.ai/models/deepseek)
- [RunAPI DeepSeek documentation](https://runapi.ai/models/deepseek.md)
- [RunAPI DeepSeek provider page](https://runapi.ai/providers/deepseek.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [DeepSeek compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses RunAPI API-key configuration and OpenAI-compatible endpoint guidance.]

## Skill Version(s):

0.1.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
