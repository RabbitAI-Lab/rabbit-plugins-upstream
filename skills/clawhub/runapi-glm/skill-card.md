## Description:

Call the GLM API (GLM 5.3 and earlier GLM 5 and 4 series) through RunAPI using OpenAI-compatible Chat Completions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure and call GLM models through RunAPI's OpenAI-compatible Chat Completions endpoint for text chat and streaming workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GLM prompts and responses are routed through RunAPI using a RunAPI API key.

Mitigation: Confirm this routing is intended, use a RunAPI-scoped key, and avoid sending sensitive prompts unless account and data handling requirements allow it.

Risk: Using unsupported protocols or undeclared GLM-5.3 capabilities can produce failed or misleading requests.

Mitigation: Use OpenAI-compatible Chat Completions for glm-5.3 and add tools, reasoning controls, structured output, or multimodal input only when the current RunAPI contract verifies support.

## Reference(s):

- [RunAPI GLM documentation](https://runapi.ai/models/glm.md)
- [RunAPI GLM homepage](https://runapi.ai/models/glm)
- [RunAPI Z.AI provider page](https://runapi.ai/providers/z-ai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [GLM compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [guidance, code, configuration]

**Output Format:** [Markdown with Python code snippets and environment variable settings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a RunAPI API key and OPENAI_BASE_URL set to https://runapi.ai/v1.]

## Skill Version(s):

0.3.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
