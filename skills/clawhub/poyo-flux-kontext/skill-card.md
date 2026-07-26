## Description: <br>
Flux Kontext image generation and editing on PoYo / poyo.ai via the PoYo task submission API, including model selection, payload preparation, polling guidance, and webhook guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and optionally submit PoYo Flux Kontext text-to-image and single-image editing requests. It helps choose the correct model, assemble request payloads, protect API credentials, and plan polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: POYO_API_KEY could be exposed through client-side code, logs, repositories, screenshots, or chat output. <br>
Mitigation: Keep the API key in a server-side environment variable or backend secret manager and avoid echoing it in generated commands or responses. <br>
Risk: Private prompts, source image URLs, or callback URLs may be submitted to PoYo or a callback receiver. <br>
Mitigation: Submit only content the user is willing to share with PoYo and the callback receiver, and avoid confidential inputs unless that trust decision is explicit. <br>
Risk: A live API call can create an external task before the user has reviewed the payload. <br>
Mitigation: Prepare payloads for review first and submit only when the user explicitly requests execution from a trusted shell. <br>


## Reference(s): <br>
- [PoYo Flux Kontext model page](https://poyo.ai/models/flux-kontext) <br>
- [PoYo Flux Kontext API documentation](https://docs.poyo.ai/api-manual/image-series/flux-kontext) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [Skill API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON payloads and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model IDs, request payloads, output settings, polling instructions, webhook guidance, and returned task IDs when a submission occurs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
