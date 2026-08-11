## Description:

Call the MiMo API (mimo-v2.5-pro and mimo-v2.5) through RunAPI using OpenAI-compatible Chat Completions or Responses clients, or Anthropic-compatible Messages clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure and call RunAPI-hosted MiMo models for text generation, streaming, supported image understanding, and OpenAI- or Anthropic-compatible client integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supported image URLs are sent to RunAPI's MiMo service.

Mitigation: Install only when that external service use is intended, and review RunAPI's current pricing and data handling information before use.

Risk: API tokens can be exposed if copied into source files or logs.

Mitigation: Store RunAPI tokens in environment variables or a secret manager.

Risk: Requests outside the verified MiMo subset may fail or behave differently than expected.

Mitigation: Use the documented OpenAI-compatible RunAPI endpoint and keep image requests within the synchronous mimo-v2.5 Chat Completions subset.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-mimo)
- [RunAPI MiMo model page](https://runapi.ai/models/mimo)
- [MiMo model documentation](https://runapi.ai/models/mimo.md)
- [Xiaomi provider page](https://runapi.ai/providers/xiaomi.md)
- [RunAPI model catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration]

**Output Format:** [Markdown with code examples and environment variable guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces client setup guidance for RunAPI MiMo requests; agents should keep credentials in environment variables or a secret manager.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
