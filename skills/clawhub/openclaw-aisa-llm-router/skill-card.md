## Description: <br>
Unified LLM Gateway provides an OpenAI-compatible interface for routing agent requests to GPT, Claude, Gemini, Qwen, Deepseek, Grok, and other model families through AIsa with a single API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisadocs](https://clawhub.ai/user/aisadocs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to configure and call a third-party LLM gateway for chat, streaming responses, vision analysis, model comparison, fallback routing, and model selection. It is intended for workflows that can route prompts and image references through AIsa under the user's API key and account terms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, documents, image URLs, or base64 images may be sent to AIsa and routed to downstream model providers. <br>
Mitigation: Use the skill only after reviewing AIsa's privacy, retention, routing, and billing terms; avoid secrets, regulated data, private documents, screenshots, and sensitive image URLs unless those terms are acceptable. <br>
Risk: A leaked or overly broad AISA_API_KEY could allow unauthorized gateway use. <br>
Mitigation: Use a dedicated, revocable API key, store it as an environment variable, and rotate or revoke it if exposure is suspected. <br>
Risk: Model choice, long outputs, retries, and comparisons can create unexpected usage costs. <br>
Mitigation: Set token limits, choose lower-cost models where suitable, monitor response usage and cost metadata, and track account credits. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aisadocs/skills/openclaw-aisa-llm-router) <br>
- [Publisher profile](https://clawhub.ai/user/aisadocs) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [AIsa API reference](https://aisa.mintlify.app/api-reference/introduction) <br>
- [AIsa model pricing](https://marketplace.aisa.one/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples, Python code, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce chat responses, streamed text chunks, image-analysis responses, model-comparison JSON, and model lists via the provided client and API examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
