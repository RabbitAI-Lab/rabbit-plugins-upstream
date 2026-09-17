## Description:

Call the DeepSeek API (deepseek-flash, deepseek-v4-pro, deepseek-v4-flash, and deepseek-v4-flash-vision-exp) through RunAPI using OpenAI-compatible Chat Completions and Responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure and call DeepSeek models through RunAPI with OpenAI-compatible Chat Completions and Responses. It also provides compatibility guidance for existing Anthropic Messages or Gemini contents clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI API keys are required and could be exposed through insecure configuration or logging.

Mitigation: Store keys in environment variables or a secret manager, avoid hardcoding them in prompts or files, and prevent key values from appearing in logs.

Risk: Prompts, data, and image URLs are routed to a third-party service for processing.

Mitigation: Use the skill only when RunAPI processing is acceptable for the data classification, and avoid private prompts, sensitive data, or sensitive image URLs unless approved.

Risk: Unsupported model or protocol assumptions can produce rejected requests or misleading integration guidance.

Mitigation: Use exact supported model IDs, verify final content and usage fields, apply at most one evidence-backed shape correction, and avoid automatic model or protocol hopping.

## Reference(s):

- [DeepSeek model documentation](https://runapi.ai/models/deepseek.md)
- [DeepSeek provider documentation](https://runapi.ai/providers/deepseek.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [DeepSeek on RunAPI homepage](https://runapi.ai/models/deepseek)
- [DeepSeek compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code blocks and environment variable settings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes model selection, request validation, streaming, retry, and protocol compatibility guidance.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
