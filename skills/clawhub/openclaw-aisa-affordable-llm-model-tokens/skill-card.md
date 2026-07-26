## Description: <br>
Unified LLM Gateway - One API for 70+ AI models. Route to GPT, Claude, Gemini, Qwen, Deepseek, Grok and more with a single API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xjordansg-yolo](https://clawhub.ai/user/0xjordansg-yolo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to send chat, streaming, vision, and model-comparison requests through AIsa's OpenAI-compatible LLM gateway with one API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, conversation content, image URLs or image data, request metadata, and the AISA API key are sent to AIsa and may be routed to downstream model providers. <br>
Mitigation: Use a protected API key, avoid sending secrets or regulated data unless approved, and rotate the key if it is exposed. <br>
Risk: Token usage can create unexpected cost across routed models. <br>
Mitigation: Set token limits where appropriate, monitor usage and cost metadata, and review credits before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/0xjordansg-yolo/skills/openclaw-aisa-affordable-llm-model-tokens) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [AIsa pricing](https://marketplace.aisa.one/pricing) <br>
- [AIsa API reference](https://aisa.mintlify.app/api-reference/introduction) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance, API calls] <br>
**Output Format:** [Markdown guidance with bash, Python, and JSON examples; CLI and API calls return JSON or streamed text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY for API calls; model responses may include usage and cost metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
