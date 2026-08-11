## Description:

This skill helps agents call GPT chat, reasoning, Codex, vision, tool-use, and embedding models through RunAPI using OpenAI-compatible and compatible-client protocols.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to configure RunAPI as an OpenAI-compatible provider for GPT chat, Responses API calls, embeddings, streaming, multimodal prompts, tool use, and Codex-style coding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests may be routed through RunAPI unintentionally if OPENAI_BASE_URL is applied to unrelated OpenAI-compatible workflows.

Mitigation: Use a RunAPI-scoped API key and confirm OPENAI_BASE_URL is set to https://runapi.ai/v1 only for workflows intended to use RunAPI.

Risk: Endpoint or model mismatches can cause failed requests, especially for embeddings, pro models, or models with a limited Responses API subset.

Mitigation: Follow the RunAPI GPT documentation for endpoint selection, route embedding models only to /v1/embeddings, and use Responses API guidance for models that require it.

## Reference(s):

- [RunAPI GPT model documentation](https://runapi.ai/models/gpt.md)
- [RunAPI OpenAI provider page](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI GPT homepage](https://runapi.ai/models/gpt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with code blocks and environment-variable configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OpenAI-compatible SDK setup, endpoint selection guidance, model routing notes, and API-key environment variables.]

## Skill Version(s):

0.2.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
