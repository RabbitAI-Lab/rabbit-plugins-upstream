## Description: <br>
Helps agents prepare and submit PoYo Nano Banana 2 Lite image generation and lightweight editing jobs through the PoYo async image API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Nano Banana 2 Lite generation or edit requests, produce payloads or curl commands, and submit prepared jobs when a trusted server-side shell with POYO_API_KEY is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: POYO_API_KEY values or authorization headers could be exposed if copied into client-side code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep the API key in server-side environment variables or a backend secret manager, and redact authorization headers from logs and responses. <br>
Risk: Private prompts, source image URLs, callback URLs, or generated outputs may be submitted to PoYo as part of image generation or editing jobs. <br>
Mitigation: Review payloads before submission and avoid sending private prompts, private image URLs, or callback URLs unless sharing them with PoYo is acceptable. <br>
Risk: Live submissions send data to an external async image service and require follow-up task tracking. <br>
Mitigation: Make live API calls only after an explicit user request from a trusted server-side shell, then save the returned task_id and use polling or a webhook for completion status. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-nano-banana-2-lite) <br>
- [PoYo Nano Banana 2 Lite model page](https://poyo.ai/models/nano-banana-2-lite) <br>
- [PoYo Nano Banana 2 Lite API docs](https://docs.poyo.ai/api-manual/image-series/nano-banana-2-lite) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [PoYo Nano Banana 2 Lite API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads and bash/curl code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a returned task_id when the user explicitly submits a prepared payload.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
