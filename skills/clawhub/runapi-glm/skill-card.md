## Description:

Call the GLM API (GLM 5 and 4 series) through RunAPI using OpenAI-compatible Chat Completions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure GLM chat, streaming, and compatibility-client requests through RunAPI with OpenAI-compatible Chat Completions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Existing OpenAI-compatible clients could be unintentionally routed to RunAPI if OPENAI_BASE_URL is changed broadly.

Mitigation: Set OPENAI_BASE_URL=https://runapi.ai/v1 only in the intended RunAPI environment and use a RunAPI-specific OPENAI_API_KEY.

Risk: Requests may assume GLM capabilities that are not verified by the current RunAPI contract.

Mitigation: Start with text chat history and add tools, reasoning, structured output, or multimodal input only when the current RunAPI contract explicitly verifies support.

## Reference(s):

- [GLM model documentation](https://runapi.ai/models/glm.md)
- [Z.ai provider documentation](https://runapi.ai/providers/z-ai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI GLM homepage](https://runapi.ai/models/glm)
- [GLM compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires RunAPI credentials and explicit endpoint configuration.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
