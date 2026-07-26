## Description: <br>
Use PoYo AI Grok Imagine Video for short text-to-video and image-to-video generation with motion-style controls through the PoYo generation API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to prepare and submit PoYo Grok Imagine video generation jobs, including text-to-video and image-to-video requests with duration, aspect ratio, mode, and callback settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, reference image URLs, and generated task data are sent to PoYo when requests are submitted. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and avoid submitting sensitive prompts or image URLs. <br>
Risk: Callback URLs can disclose task status or generated-result metadata to the configured endpoint. <br>
Mitigation: Use trusted HTTPS callback endpoints and avoid webhooks for sensitive generations unless the endpoint and data flow are approved. <br>
Risk: The skill requires a PoYo API key for authenticated submissions. <br>
Mitigation: Provide the key through POYO_API_KEY or a secure secret manager, and avoid pasting credentials into shared prompts, files, or logs. <br>


## Reference(s): <br>
- [PoYo Grok Imagine API Reference](references/api.md) <br>
- [PoYo Grok Imagine model page](https://poyo.ai/models/grok-imagine) <br>
- [PoYo Grok Imagine API docs](https://docs.poyo.ai/api-manual/video-series/grok-imagine) <br>
- [PoYo task status docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [PoYo Grok Imagine OpenAPI JSON](https://docs.poyo.ai/api-manual/video-series/grok-imagine.json) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-grok-imagine) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the chosen model id, final payload or parameter summary, reference-image usage, returned task_id, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
