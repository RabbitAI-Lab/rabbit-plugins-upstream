## Description:

Call Grok 4.6 through RunAPI Responses only; use Grok 4.3, 4.5, or Grok 4.20 non-reasoning through their verified OpenAI-compatible interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call Grok models through RunAPI's documented OpenAI-compatible endpoints, including Responses workflows, streaming, structured output, image input, and compatible client integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and image URLs are sent to RunAPI when the skill's API examples are used.

Mitigation: Review data-sharing requirements before use and avoid sending sensitive content unless RunAPI is approved for that data.

Risk: OPENAI_API_KEY is required and should contain a RunAPI key for the configured base URL.

Mitigation: Store the key in the agent's secret-management path and pair it with OPENAI_BASE_URL=https://runapi.ai/v1.

Risk: Unsupported hosted tools, file inputs, or stateful continuation fields can cause rejected requests.

Mitigation: Use the documented Grok 4.6 request shape and change rejected shapes once using the provider's structured error.

## Reference(s):

- [RunAPI Grok documentation](https://runapi.ai/models/grok.md)
- [RunAPI xAI provider page](https://runapi.ai/providers/xai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Grok homepage](https://runapi.ai/models/grok)
- [Grok compatibility protocols](references/compatibility-protocols.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-grok)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python examples, endpoint configuration, and protocol-specific verification guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OPENAI_API_KEY and OPENAI_BASE_URL for RunAPI-compatible clients]

## Skill Version(s):

0.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
