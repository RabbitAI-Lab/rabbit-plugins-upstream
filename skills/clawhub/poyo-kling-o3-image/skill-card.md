## Description: <br>
Kling O3 image generation and editing on PoYo for prompt-only generation, reference-image editing, aspect ratio and resolution control, polling, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and submit PoYo Kling O3 image-generation or image-editing jobs, then guide polling or webhook follow-up for asynchronous results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: POYO_API_KEY could be exposed if placed in browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep the key in server-side environment variables or a backend secret manager and avoid echoing it in commands or generated output. <br>
Risk: Prompts, source image URLs, or callback URLs may contain confidential information sent to PoYo or a webhook receiver. <br>
Mitigation: Review payloads before submission and send sensitive material only when the user trusts PoYo and the webhook receiver. <br>
Risk: A live submission can create an external asynchronous image-generation task. <br>
Mitigation: Make live API calls only when the user explicitly asks, a safe server-side environment is available, and the payload has been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-kling-o3-image) <br>
- [PoYo Kling O3 Image model page](https://poyo.ai/models/kling-o3-image) <br>
- [PoYo Kling O3 API documentation](https://docs.poyo.ai/api-manual/image-series/kling-o3) <br>
- [Local PoYo Kling O3 Image API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a PoYo task_id and polling or webhook next steps when a live API request is submitted.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
