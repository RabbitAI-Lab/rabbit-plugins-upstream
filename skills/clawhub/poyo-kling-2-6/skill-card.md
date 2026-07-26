## Description: <br>
This skill helps agents prepare, submit, and follow up on PoYo Kling 2.6 text-to-video or image-to-video jobs with optional native audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create reviewed payloads for PoYo Kling 2.6 video generation, including text-to-video and image-to-video requests with duration, aspect ratio, audio, polling, or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: POYO_API_KEY could be exposed or misused if handled outside a trusted server-side environment. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a secret manager, and never include it in browser code, logs, screenshots, repositories, or chat output. <br>
Risk: Confidential prompts, private media URLs, callback URLs, or generated media URLs may be sent to PoYo or a callback receiver. <br>
Mitigation: Submit such data only when the user trusts PoYo and the callback receiver, and review payloads before submission. <br>
Risk: Unreviewed payloads could submit unintended video-generation jobs. <br>
Mitigation: Require explicit user approval before making live API calls and report the returned task_id for follow-up tracking. <br>


## Reference(s): <br>
- [PoYo Kling 2.6 model page](https://poyo.ai/models/kling-2-6) <br>
- [PoYo Kling 2.6 API docs](https://docs.poyo.ai/api-manual/video-series/kling-2-6) <br>
- [Local API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-kling-2-6) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a returned task_id and a next-step recommendation to poll status or wait for a webhook.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
