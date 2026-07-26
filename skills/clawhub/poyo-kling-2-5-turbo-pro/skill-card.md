## Description: <br>
Kling 2.5 Turbo Pro video generation on PoYo via the PoYo async generate API for text-to-video, image-to-video, frame-guided video, polling, and webhook workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Kling 2.5 Turbo Pro video-generation requests, submit trusted payloads, and explain polling or webhook follow-up. It supports text-to-video, first-frame image-to-video, and first/last-frame video workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed through browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY server-side in environment variables or a secret manager, and never echo or log the credential. <br>
Risk: Prompts, source image URLs, callback URLs, or generated media URLs may contain confidential information sent to PoYo or callback receivers. <br>
Mitigation: Review payloads before live submission and avoid sending private data unless the user trusts PoYo and the callback endpoint. <br>
Risk: The helper can submit live video-generation jobs with a user-provided API key. <br>
Mitigation: Submit only prepared JSON payloads from a trusted shell after explicit user approval. <br>


## Reference(s): <br>
- [PoYo Kling 2.5 Turbo Pro Model Page](https://poyo.ai/models/kling-2-5-turbo-pro) <br>
- [PoYo Kling 2.5 Turbo Pro API Docs](https://docs.poyo.ai/api-manual/video-series/kling-2-5-turbo-pro) <br>
- [PoYo API Key Page](https://poyo.ai/dashboard/api-key) <br>
- [PoYo Kling 2.5 Turbo Pro API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/poyo-kling-2-5-turbo-pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, request mode, payload summary, final JSON payload, curl command, task_id after submission, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
