## Description:

Call GPT generation and OpenAI text embedding models through RunAPI using OpenAI-compatible clients. Use for chat, Responses, embeddings, streaming, tools, vision, or an existing compatibility client that needs the conditional reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure OpenAI-compatible clients for GPT generation, embeddings, streaming, tools, and vision through RunAPI. Existing Anthropic Messages or Gemini contents clients can use the compatibility reference only when that protocol is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Model prompts, inputs, outputs, and embedding text are sent to RunAPI when clients use the configured base URL.

Mitigation: Install only when routing GPT or embedding requests through RunAPI is intended, and use a RunAPI-issued key for OPENAI_API_KEY.

Risk: A client could accidentally send unrelated provider credentials to RunAPI if OPENAI_API_KEY is reused without checking OPENAI_BASE_URL.

Mitigation: Keep RunAPI credentials separate from other provider keys and verify OPENAI_BASE_URL is set to https://runapi.ai/v1 before making requests.

## Reference(s):

- [GPT model documentation](https://runapi.ai/models/gpt.md)
- [OpenAI provider documentation](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI GPT homepage](https://runapi.ai/models/gpt)
- [GPT compatibility protocols](references/compatibility-protocols.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-gpt)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with inline code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces client setup guidance, request examples, result verification checks, and stop-boundary rules; it does not execute code or persist files.]

## Skill Version(s):

0.2.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
