## Description:

Call the GLM API (glm-5.2, glm-5.1, glm-5-turbo, glm-5, glm-4.7, glm-4.6, glm-4.5, glm-4.5-air) through RunAPI using the official OpenAI SDK or compatible clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to configure OpenAI-compatible clients for GLM requests through RunAPI, including chat completions, streaming, and Anthropic- or Gemini-compatible protocol paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires calls to an external RunAPI/GLM service, which can expose submitted prompts or content to that provider.

Mitigation: Use the skill only when RunAPI processing is approved, and avoid sending secrets, regulated data, or customer content unless policy permits it.

Risk: API tokens are required for operation and could be leaked if copied into source files, commits, or shell history.

Mitigation: Store tokens in environment variables or a secret manager and avoid hard-coding credentials in examples or committed files.

Risk: Unsupported GLM capabilities such as multimodal input, structured output, reasoning controls, and hosted tools may fail if requested.

Mitigation: Keep GLM requests text-only and do not remove rejected fields and retry unless the user explicitly accepts the semantic change.

## Reference(s):

- [RunAPI GLM model overview](https://runapi.ai/models/glm)
- [RunAPI GLM model documentation](https://runapi.ai/models/glm.md)
- [RunAPI Z.ai provider documentation](https://runapi.ai/providers/z-ai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-glm)
- [RunAPI publisher profile](https://clawhub.ai/user/runapi-ai)

## Skill Output:

**Output Type(s):** [guidance, configuration, code, shell commands]

**Output Format:** [Markdown with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces OpenAI-compatible, Anthropic-compatible, and Gemini-compatible request examples for text-only GLM use.]

## Skill Version(s):

0.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
