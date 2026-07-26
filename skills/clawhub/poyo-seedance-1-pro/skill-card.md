## Description: <br>
Seedance 1.0 Pro video generation on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `seedance-1.0-pro`, text-to-video, image-to-video, 720p or 1080p clips, 5s or 10s duration, task submission, polling, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to prepare Seedance 1.0 Pro text-to-video or image-to-video requests, submit reviewed PoYo generation jobs, and understand polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requests are sent to PoYo and may include prompts, source image URLs, callback URLs, and generation settings. <br>
Mitigation: Review payloads before submission and avoid confidential prompts, private media URLs, personal data, or internal callback URLs unless the user accepts PoYo as the external processor. <br>
Risk: The skill depends on POYO_API_KEY for live task submission. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment or secret manager and never expose it in browser code, public repositories, logs, screenshots, or chat output. <br>
Risk: Callback URLs can expose internal systems if unsafe endpoints are submitted. <br>
Mitigation: Use only HTTPS callback URLs controlled by the user and avoid localhost, private network, or internal-only endpoints. <br>


## Reference(s): <br>
- [PoYo Seedance 1.0 Pro API Reference](references/api.md) <br>
- [PoYo Seedance 1.0 Pro model page](https://poyo.ai/models/seedance-1-pro) <br>
- [PoYo Seedance 1.0 Pro API docs](https://docs.poyo.ai/api-manual/video-series/seedance-1.0-pro) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-seedance-1-pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payload examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, request mode, payload summary, selected resolution and duration, source-image status, returned task_id, and next-step guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
