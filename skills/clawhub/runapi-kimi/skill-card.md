## Description:

Call the Kimi API (kimi-k3, kimi-k2.7-code, kimi-k2.6, kimi-k2.5) through RunAPI using the official OpenAI SDK or compatible clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure OpenAI-compatible, Anthropic-compatible, or Gemini-compatible clients for Kimi models through RunAPI. It provides setup guidance, API examples, streaming guidance, model selection notes, and capability boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests are sent through RunAPI, so using the wrong base URL or token can route traffic through an unintended service.

Mitigation: Set OPENAI_BASE_URL to https://runapi.ai/v1 and store the RunAPI token in OPENAI_API_KEY, RUNAPI_TOKEN, or a secret manager.

Risk: API keys may be exposed if copied into committed code, shared snippets, or shell history.

Mitigation: Keep tokens in environment variables or a secret manager and avoid inlining real credentials in code examples.

Risk: Unsupported Kimi request features can fail before a task is created.

Mitigation: For kimi-k3 and kimi-k2.7-code, send basic text requests, avoid raw reasoning, tool history, multimodal content, structured-output fields, cache controls, and stateful continuation.

## Reference(s):

- [Kimi model overview, pricing, and rate limits](https://runapi.ai/models/kimi.md)
- [RunAPI Kimi homepage](https://runapi.ai/models/kimi)
- [Moonshot AI provider comparison](https://runapi.ai/providers/moonshot-ai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-kimi)
- [RunAPI publisher profile](https://clawhub.ai/user/runapi-ai)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with dotenv, Python, TypeScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes environment variable requirements, streaming guidance, supported model IDs, and Kimi capability boundaries.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
