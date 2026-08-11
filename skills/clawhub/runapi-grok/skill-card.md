## Description:

Call Grok 4.3, 4.5, and Grok 4.20 non-reasoning through RunAPI with the official OpenAI SDK or compatible clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure RunAPI-hosted Grok models through OpenAI-compatible clients, including Chat Completions, Responses, streaming, function tools, and structured output workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests are sent to RunAPI as a third-party model provider, which may affect handling of secrets, regulated data, or confidential material.

Mitigation: Use this skill only when organizational policy approves RunAPI for the data being sent, and avoid transmitting sensitive data unless approved.

Risk: The skill requires API credentials for RunAPI-compatible clients.

Mitigation: Store API keys in environment variables or a secret manager, and avoid hard-coding credentials in prompts, scripts, or source files.

## Reference(s):

- [RunAPI Grok model page](https://runapi.ai/models/grok)
- [Grok 4.3 overview and pricing](https://runapi.ai/models/grok/4.3.md)
- [Grok 4.5 overview and pricing](https://runapi.ai/models/grok/4.5.md)
- [RunAPI xAI provider page](https://runapi.ai/providers/xai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-grok)
- [RunAPI publisher profile](https://clawhub.ai/user/runapi-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown with code examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OpenAI-compatible API usage patterns and environment variable requirements for RunAPI.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
