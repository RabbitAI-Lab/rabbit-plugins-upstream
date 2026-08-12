## Description:

Use DeepSeek v4 Pro and v4 Flash through RunAPI with OpenAI-compatible Chat Completions, Responses, streaming, and supported compatibility clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure, call, and verify DeepSeek API requests through RunAPI in OpenAI-compatible clients. It supports text generation, streaming, one verified DeepSeek v4 Flash custom-function lifecycle, and conditional Anthropic Messages or Gemini contents compatibility paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users must provide a RunAPI API key and route DeepSeek requests through RunAPI.

Mitigation: Install only when this credential handling and request routing are acceptable for the intended environment.

Risk: Unsupported request shapes, automatic protocol changes, or unverified model features can produce failed or misleading API behavior.

Mitigation: Use the documented model IDs and protocol shapes, apply at most one evidence-backed correction or safe pre-response retry, and stop rather than switching model or protocol automatically.

## Reference(s):

- [DeepSeek on RunAPI documentation](https://runapi.ai/models/deepseek.md)
- [RunAPI DeepSeek provider page](https://runapi.ai/providers/deepseek.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI DeepSeek homepage](https://runapi.ai/models/deepseek)
- [DeepSeek compatibility protocols](references/compatibility-protocols.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-deepseek)
- [RunAPI publisher profile](https://clawhub.ai/user/runapi-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with Python snippets and environment variable configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a RunAPI API key through OPENAI_API_KEY and OPENAI_BASE_URL set to https://runapi.ai/v1.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
