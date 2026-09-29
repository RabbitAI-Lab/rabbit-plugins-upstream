## Description:

Guides developers in calling Claude models through RunAPI using Anthropic Messages, with optional compatibility guidance for existing OpenAI or Gemini clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers configure Claude-compatible clients to call RunAPI for chat, streaming, and supported multimodal or tool workflows. Existing OpenAI or Gemini clients can use the separate compatibility guidance when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, files, images, tool outputs, and usage metadata may be sent to RunAPI.

Mitigation: Confirm the intended data sharing and review RunAPI's terms and data handling before use.

Risk: API credentials or unexpected usage costs may be exposed through careless setup.

Mitigation: Use a RunAPI key with normal credential hygiene and check pricing for the intended use case.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/runapi-ai/skills/runapi-claude)
- [RunAPI Claude documentation](https://runapi.ai/models/claude.md)
- [RunAPI Claude model page](https://runapi.ai/models/claude)
- [RunAPI Anthropic provider documentation](https://runapi.ai/providers/anthropic.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a RunAPI API key and a supported model ID.]

## Skill Version(s):

0.2.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
