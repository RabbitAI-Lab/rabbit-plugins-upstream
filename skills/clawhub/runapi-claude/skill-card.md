## Description:

Call Claude models through RunAPI using the Anthropic Messages protocol. Use for Claude chat, streaming, vision, tools, reasoning, token counting, or an existing compatibility client that needs the conditional reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to configure agents or Anthropic-compatible clients to call Claude models through RunAPI for chat, streaming, vision, tools, reasoning, and token-counting workflows. Existing OpenAI or Gemini clients can use the compatibility reference only when that protocol is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, and tool-call payloads sent through this skill go to RunAPI using the configured API key.

Mitigation: Use the skill only where sending those payloads to RunAPI is acceptable, and protect ANTHROPIC_API_KEY as a credential.

Risk: Compatibility protocols can be misapplied to unsupported client or model shapes.

Mitigation: Use Anthropic Messages as the primary protocol and verify exact model support in RunAPI documentation before using OpenAI or Gemini compatibility paths.

## Reference(s):

- [RunAPI Claude model documentation](https://runapi.ai/models/claude.md)
- [RunAPI Anthropic provider documentation](https://runapi.ai/providers/anthropic.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Claude homepage](https://runapi.ai/models/claude)
- [Claude compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with inline code examples and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ANTHROPIC_API_KEY and ANTHROPIC_BASE_URL; users should verify exact model support against RunAPI documentation.]

## Skill Version(s):

0.2.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
