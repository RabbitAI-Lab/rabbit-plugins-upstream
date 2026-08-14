## Description:

Call the DeepSeek API through RunAPI using OpenAI-compatible Chat Completions and Responses for text, streaming, the verified Flash function path, and conditional compatibility clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure authenticated DeepSeek requests through RunAPI, verify responses and usage, handle streaming, and apply compatibility protocols only when an existing client requires them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setting OPENAI_API_KEY and OPENAI_BASE_URL for this workflow can affect OpenAI-compatible clients that read those variables.

Mitigation: Confirm the intent to route DeepSeek requests through RunAPI and scope these variables to clients that should use RunAPI.

## Reference(s):

- [RunAPI DeepSeek model documentation](https://runapi.ai/models/deepseek.md)
- [RunAPI DeepSeek provider documentation](https://runapi.ai/providers/deepseek.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI DeepSeek homepage](https://runapi.ai/models/deepseek)
- [DeepSeek compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Python code blocks and environment variable configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes response verification, streaming, retry, and stop-boundary guidance for RunAPI DeepSeek calls.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
