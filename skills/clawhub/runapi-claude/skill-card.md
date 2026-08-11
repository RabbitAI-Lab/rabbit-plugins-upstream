## Description:

Guides agents to call Claude models through RunAPI using Anthropic-compatible, OpenAI-compatible, Gemini-compatible, and shell-based API examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to configure Claude requests through RunAPI for chat, streaming, vision, tool use, token counting, and protocol-compatible client integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, image URLs, tool requests, and attached content are sent to RunAPI when the skill's guidance is followed.

Mitigation: Avoid sending secrets, sensitive files, or private data unless the user is comfortable with RunAPI's handling policies.

Risk: RunAPI API keys are required for the documented integrations.

Mitigation: Store ANTHROPIC_API_KEY in an environment variable or secret manager and avoid hard-coding credentials in source files.

Risk: Vision examples rely on publicly fetchable image URLs, which can expose referenced content to the provider.

Mitigation: Use only intended public image resources and avoid private or sensitive URLs in multimodal requests.

## Reference(s):

- [RunAPI Claude model documentation](https://runapi.ai/models/claude.md)
- [RunAPI Anthropic provider page](https://runapi.ai/providers/anthropic.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Claude homepage](https://runapi.ai/models/claude)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ANTHROPIC_API_KEY and ANTHROPIC_BASE_URL for RunAPI-backed Claude use.]

## Skill Version(s):

0.2.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
