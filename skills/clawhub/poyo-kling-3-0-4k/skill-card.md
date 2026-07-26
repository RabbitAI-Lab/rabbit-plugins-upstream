## Description: <br>
Helps agents prepare, submit, and follow up on PoYo Kling 3.0 4K video generation jobs for text-to-video, image-to-video, multi-shot, audio, polling, and webhook workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create PoYo Kling 3.0 4K generation payloads, submit trusted requests with a server-side POYO_API_KEY, and explain polling or webhook follow-up for generated video tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: POYO_API_KEY exposure could allow unauthorized PoYo API use. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager, and never place it in browser code, public repositories, logs, screenshots, or chat output. <br>
Risk: Prompts, source image URLs, callback URLs, or media may contain private information sent to PoYo or a webhook receiver. <br>
Mitigation: Review payloads before submission and avoid sending confidential inputs unless the user trusts PoYo and the callback receiver. <br>
Risk: Prepared payloads may submit unintended video generation jobs if run without review. <br>
Mitigation: Make live API calls only after explicit user approval in a trusted shell, then report the returned task_id for follow-up polling. <br>


## Reference(s): <br>
- [PoYo Kling API model page](https://poyo.ai/models/kling-3-api) <br>
- [PoYo Kling 3.0 4K API docs](https://docs.poyo.ai/api-manual/video-series/kling-3-0-4k) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-kling-3-0-4k) <br>
- [Bundled API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON payloads and bash curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a returned task_id and next-step polling or webhook guidance when a request is submitted.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
