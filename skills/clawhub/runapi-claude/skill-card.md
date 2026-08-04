## Description: <br>
Call the Claude API (claude-opus, claude-sonnet, claude-haiku) through RunAPI using the official Anthropic SDK, OpenAI SDK, Gemini contents clients, or compatible clients. Use when the user asks for Claude / Anthropic chat, streaming messages, multimodal vision input, tool use, extended thinking, token counting, OpenAI or Gemini protocol compatibility, or when they want to point an existing LLM SDK setup at RunAPI as the base URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to configure Claude-compatible chat, streaming, vision, tool use, reasoning, token counting, and protocol-compatible API calls through RunAPI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, image URLs, tool payloads, and API metadata are routed to an external RunAPI service. <br>
Mitigation: Install only for approved RunAPI use, and avoid sending secrets or regulated data unless the organization has approved that use. <br>
Risk: Misconfigured credentials or base URL settings can send Claude-compatible requests to the wrong endpoint or fail at runtime. <br>
Mitigation: Configure ANTHROPIC_API_KEY with a RunAPI token and ANTHROPIC_BASE_URL as https://runapi.ai before use. <br>
Risk: Long non-streaming generations can block an agent workflow. <br>
Mitigation: Use streaming for responses longer than a few hundred tokens or for extended-thinking and large max_tokens requests. <br>


## Reference(s): <br>
- [RunAPI Claude Model Page](https://runapi.ai/models/claude.md) <br>
- [RunAPI Anthropic Provider Page](https://runapi.ai/providers/anthropic.md) <br>
- [RunAPI Model Catalog](https://runapi.ai/models.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-claude) <br>
- [RunAPI Claude Homepage](https://runapi.ai/models/claude) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline Python, TypeScript, JSON, dotenv, and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ANTHROPIC_API_KEY and ANTHROPIC_BASE_URL for RunAPI-backed Claude requests.] <br>

## Skill Version(s): <br>
0.2.12 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
