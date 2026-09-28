## Description:

Guides agents in using Grok models through RunAPI with supported request formats, streaming, tools, and response checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure RunAPI credentials and call supported Grok models through OpenAI-compatible interfaces, with conditional guidance for existing Anthropic or Gemini clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An OpenAI-compatible client may send a RunAPI key or Grok request to an unintended provider if its endpoint is misconfigured.

Mitigation: Confirm the intended RunAPI routing before use; set OPENAI_API_KEY to a RunAPI token and OPENAI_BASE_URL to https://runapi.ai/v1.

## Reference(s):

- [Grok on RunAPI](https://runapi.ai/models/grok.md)
- [RunAPI Grok model page](https://runapi.ai/models/grok)
- [RunAPI xAI provider documentation](https://runapi.ai/providers/xai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with Python examples and API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers supported model and protocol choices, response verification, and retry boundaries.]

## Skill Version(s):

0.2.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
