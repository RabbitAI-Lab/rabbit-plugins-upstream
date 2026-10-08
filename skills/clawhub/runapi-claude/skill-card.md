## Description:

Guides developers in using Claude models through RunAPI with the Anthropic Messages protocol and optional OpenAI or Gemini client compatibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to configure RunAPI credentials and call Claude models for chat, streaming, vision, tools, reasoning, and token counting. It also guides developers migrating existing OpenAI or Gemini clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts sent through this integration go to RunAPI's service.

Mitigation: Use only when routing prompts to RunAPI is intended and permitted by your data-handling policy.

Risk: Using this integration requires a RunAPI API key.

Mitigation: Provide the key through the documented environment variable and protect it as a credential.

## Reference(s):

- [Claude on RunAPI documentation](https://runapi.ai/models/claude.md)
- [Claude on RunAPI model page](https://runapi.ai/models/claude)
- [RunAPI Anthropic provider documentation](https://runapi.ai/providers/anthropic.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Compatibility protocols](references/compatibility-protocols.md)
- [ClawHub skill release](https://clawhub.ai/runapi-ai/skills/runapi-claude)

## Skill Output:

**Output Type(s):** [Text, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with Python examples and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes request verification and retry boundaries; no executable files are produced.]

## Skill Version(s):

0.2.17 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
