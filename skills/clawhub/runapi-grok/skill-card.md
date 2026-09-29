## Description:

Guides developers in using Grok models through RunAPI for chat, reasoning, streaming, tools, and structured output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to configure RunAPI credentials and call supported Grok models through OpenAI-compatible endpoints, with conditional guidance for existing Anthropic or Gemini clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, image URLs, and tool outputs sent through RunAPI may expose sensitive data to an external provider.

Mitigation: Confirm the intended provider and avoid sending sensitive data without authorization.

Risk: API requests and hosted web search may incur costs.

Mitigation: Check usage and pricing before enabling requests or hosted web search.

## Reference(s):

- [RunAPI Grok documentation](https://runapi.ai/models/grok.md)
- [RunAPI Grok model page](https://runapi.ai/models/grok)
- [RunAPI xAI provider documentation](https://runapi.ai/providers/xai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [Text, Code, Configuration instructions]

**Output Format:** [Text or Markdown with Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include streaming events, tool calls, and usage information.]

## Skill Version(s):

0.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
