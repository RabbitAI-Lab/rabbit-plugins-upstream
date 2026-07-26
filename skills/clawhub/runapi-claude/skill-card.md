## Description: <br>
Call the Claude API through RunAPI using Anthropic, OpenAI, Gemini-compatible, or other compatible clients for chat, streaming, multimodal input, tool use, extended thinking, token counting, and protocol-compatible integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to configure Claude API calls through RunAPI, including SDK setup, streaming, multimodal requests, token counting, and OpenAI or Gemini protocol compatibility. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Claude prompts and API traffic may be routed to RunAPI using a RunAPI token. <br>
Mitigation: Install and use the skill only when RunAPI is the intended Claude API route, and configure credentials explicitly through ANTHROPIC_API_KEY and ANTHROPIC_BASE_URL. <br>
Risk: Broad Claude-related trigger wording may activate the skill for generic Claude help when stricter RunAPI-specific routing is desired. <br>
Mitigation: Review the trigger wording before deployment and narrow it if the environment should separate general Claude guidance from RunAPI API usage. <br>


## Reference(s): <br>
- [RunAPI Claude Model Documentation](https://runapi.ai/models/claude.md) <br>
- [RunAPI Anthropic Provider Documentation](https://runapi.ai/providers/anthropic.md) <br>
- [RunAPI Model Catalog](https://runapi.ai/models.md) <br>
- [RunAPI Claude Homepage](https://runapi.ai/models/claude) <br>
- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-claude) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/runapi-ai) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code blocks and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires RunAPI credentials via ANTHROPIC_API_KEY and ANTHROPIC_BASE_URL for the described API flows.] <br>

## Skill Version(s): <br>
0.2.11 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
