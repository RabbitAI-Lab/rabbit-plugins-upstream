## Description: <br>
Unified LLM Gateway - One API for 70+ AI models. Route to GPT, Claude, Gemini, Qwen, Deepseek, Grok and more with a single API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xjordansg-yolo](https://clawhub.ai/user/0xjordansg-yolo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to route chat, vision, streaming, model comparison, and fallback requests across multiple LLM families through AIsa's OpenAI-compatible gateway with one API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, message history, image links, and request metadata submitted through the skill go to AIsa and routed model providers. <br>
Mitigation: Install only if those providers are approved for the intended data, and avoid sending secrets, private documents, internal image links, or regulated personal data unless your organization has approved that use. <br>
Risk: The AISA_API_KEY can expose account access, usage, and billing if it is mishandled. <br>
Mitigation: Keep AISA_API_KEY protected, avoid committing it to files, monitor usage and billing, and rotate the key if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/0xjordansg-yolo/skills/openclaw-aisa-llm-gateway) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [AIsa pricing and model availability](https://marketplace.aisa.one/pricing) <br>
- [AIsa API reference](https://aisa.mintlify.app/api-reference/introduction) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and Python examples; API responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY and network access to the AIsa API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
