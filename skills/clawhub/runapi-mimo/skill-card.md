## Description: <br>
Call the MiMo API (mimo-v2.5-pro and mimo-v2.5) through RunAPI using OpenAI-compatible Chat Completions or Responses clients, or Anthropic-compatible Messages clients. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to configure OpenAI-compatible or Anthropic-compatible clients for MiMo text generation through RunAPI, including basic requests and streaming. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and outputs are sent to RunAPI and Xiaomi MiMo when the configured clients are used. <br>
Mitigation: Use the skill only for text-generation workflows covered by the supported subset and review data-sharing requirements before sending sensitive content. <br>
Risk: RunAPI tokens could be exposed if copied into code or logs. <br>
Mitigation: Keep API keys in environment variables or a secret manager, as directed by the skill and security guidance. <br>
Risk: Unsupported advanced or multimodal fields could produce rejected requests or unexpected integration behavior. <br>
Mitigation: Keep requests text-only and avoid tools, reasoning controls, hosted capabilities, documents, audio, images, and other fields outside the verified subset. <br>


## Reference(s): <br>
- [MiMo model overview and pricing](https://runapi.ai/models/mimo.md) <br>
- [RunAPI MiMo homepage](https://runapi.ai/models/mimo) <br>
- [Xiaomi provider page](https://runapi.ai/providers/xiaomi.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with environment variable setup and Python or TypeScript code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Covers text-only MiMo requests, streaming, OpenAI-compatible clients, and Anthropic-compatible Messages clients.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
