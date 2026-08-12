## Description:

Call the GLM API (GLM 5 and 4 series) through RunAPI using OpenAI-compatible Chat Completions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure OpenAI-compatible clients for GLM chat, streaming, and compatibility-client requests through RunAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GLM requests are routed through RunAPI, which may affect billing, provider approval, and data-handling requirements.

Mitigation: Install only when RunAPI is an acceptable provider, confirm billing and data-handling terms, and avoid sending sensitive data unless approved for the use case.

Risk: The skill requires API credentials for RunAPI-compatible requests.

Mitigation: Use a scoped RunAPI key and provide credentials only through the documented environment variables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-glm)
- [RunAPI GLM documentation](https://runapi.ai/models/glm.md)
- [RunAPI GLM homepage](https://runapi.ai/models/glm)
- [RunAPI Z.ai provider page](https://runapi.ai/providers/z-ai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [GLM compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with Python code snippets and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires RunAPI credentials through OPENAI_API_KEY and OPENAI_BASE_URL.]

## Skill Version(s):

0.3.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
