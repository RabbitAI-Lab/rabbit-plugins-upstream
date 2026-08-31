## Description:

Call DeepSeek models through RunAPI with OpenAI-compatible Chat Completions and Responses for text, image input, streaming, and a verified Flash function path.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to route DeepSeek text, vision, streaming, and limited function-calling workflows through RunAPI using OpenAI-compatible clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OpenAI-compatible clients may send requests to the wrong provider if shared environment variables are reused across projects.

Mitigation: Scope OPENAI_API_KEY and OPENAI_BASE_URL to the RunAPI workflow and confirm OPENAI_BASE_URL is https://runapi.ai/v1 before sending requests.

Risk: Requests are routed through RunAPI for DeepSeek model access.

Mitigation: Install and use the skill only when routing DeepSeek requests through RunAPI is intended.

## Reference(s):

- [RunAPI DeepSeek model documentation](https://runapi.ai/models/deepseek.md)
- [RunAPI DeepSeek provider page](https://runapi.ai/providers/deepseek.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI DeepSeek homepage](https://runapi.ai/models/deepseek)
- [DeepSeek compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [guidance, code, configuration, shell commands]

**Output Format:** [Markdown with Python examples and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides OpenAI-compatible API usage with required RunAPI environment variables.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
