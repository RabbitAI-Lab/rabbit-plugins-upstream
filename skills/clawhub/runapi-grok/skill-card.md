## Description:

Call Grok 4.3, 4.5, and Grok 4.20 non-reasoning through RunAPI using OpenAI-compatible Chat Completions and Responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to configure Grok requests through RunAPI with OpenAI-compatible Chat Completions or Responses, including streaming, tools, structured output, and conditional compatibility protocols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes prompts and data to the external RunAPI service.

Mitigation: Use it only when routing Grok requests through RunAPI is intended, and review generated requests before sending sensitive data.

Risk: The skill requires API credentials for RunAPI/OpenAI-compatible clients.

Mitigation: Keep API keys in environment variables or a secret manager and avoid committing them to source control.

Risk: Incorrect request shapes or automatic model and protocol changes could cause failed or unintended calls.

Mitigation: Apply only one evidence-backed shape correction, retry transport only once when safe, and avoid automatic model or protocol hopping.

## Reference(s):

- [RunAPI Grok model documentation](https://runapi.ai/models/grok.md)
- [RunAPI xAI provider documentation](https://runapi.ai/providers/xai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Grok homepage](https://runapi.ai/models/grok)
- [Grok compatibility protocols](references/compatibility-protocols.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-grok)

## Skill Output:

**Output Type(s):** [guidance, code, configuration]

**Output Format:** [Markdown with Python code examples and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes model IDs, environment variable names, endpoint URLs, verification expectations, retry boundaries, and conditional compatibility guidance.]

## Skill Version(s):

0.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
