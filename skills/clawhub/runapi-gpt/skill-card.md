## Description:

Call GPT generation and OpenAI text embedding models through RunAPI using OpenAI-compatible clients for chat, Responses, embeddings, streaming, tools, vision, or existing compatibility clients that need the conditional reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure OpenAI-compatible clients for GPT generation, text embeddings, streaming, vision, tools, and realtime audio through RunAPI. It also provides conditional compatibility guidance for existing Anthropic Messages or Gemini contents clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, files, images, audio, and tool-related request data may be sent to RunAPI during normal use.

Mitigation: Install only when RunAPI is the intended model provider, use a RunAPI-specific API key, and confirm OPENAI_BASE_URL is set to https://runapi.ai/v1.

Risk: Unsupported model, endpoint, or protocol combinations can fail or produce misleading integration guidance.

Mitigation: Follow the documented endpoint boundaries, keep embedding models on /v1/embeddings, and load compatibility protocols only for existing Anthropic Messages or Gemini contents clients.

## Reference(s):

- [RunAPI GPT model documentation](https://runapi.ai/models/gpt.md)
- [RunAPI GPT model page](https://runapi.ai/models/gpt)
- [RunAPI OpenAI provider documentation](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [GPT compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes model and protocol boundaries, required environment variables, verification checks, and stop conditions.]

## Skill Version(s):

0.2.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
