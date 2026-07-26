## Description: <br>
Guides agents and developers in calling GPT chat, reasoning, Codex, multimodal, tool-use, streaming, and embedding APIs through RunAPI using OpenAI-compatible and related client protocols. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to configure RunAPI credentials, choose GPT endpoints, and generate example requests for chat, Responses API, streaming, multimodal inputs, tool use, protocol compatibility, embeddings, and Codex-oriented workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, image references, and request content may be sent to RunAPI when following the skill examples. <br>
Mitigation: Use the skill only when RunAPI routing is intended, and avoid sending secrets or sensitive private data unless that use is approved. <br>
Risk: The skill relies on API credentials and a custom base URL for outbound model requests. <br>
Mitigation: Store OPENAI_API_KEY securely and set OPENAI_BASE_URL only in environments that should route requests to https://runapi.ai/v1. <br>


## Reference(s): <br>
- [RunAPI GPT model page](https://runapi.ai/models/gpt) <br>
- [RunAPI GPT documentation](https://runapi.ai/models/gpt.md) <br>
- [RunAPI OpenAI provider documentation](https://runapi.ai/providers/openai.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-gpt) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with code blocks, shell commands, configuration snippets, and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Examples may include API endpoints, environment variables, model IDs, request payloads, and client initialization snippets.] <br>

## Skill Version(s): <br>
0.2.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
