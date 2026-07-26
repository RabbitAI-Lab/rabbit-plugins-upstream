## Description: <br>
Helps agents prepare and submit PoYo Kling O3 4K video-generation jobs, including text-to-video, image-to-video, reference-to-video, multi-shot payloads, polling, and webhook guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill to create valid PoYo Kling O3 4K request payloads, submit asynchronous generation jobs with curl, and explain follow-up polling or webhook handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a PoYo API key for network submission. <br>
Mitigation: Keep POYO_API_KEY server-side, avoid exposing it in browser code, logs, screenshots, repositories, or chat output, and make live calls only from trusted environments. <br>
Risk: Video-generation prompts, source media URLs, and callback URLs may contain confidential information. <br>
Mitigation: Review payloads before submission and avoid sending private prompts, private media URLs, or sensitive callback URLs unless PoYo and the callback receiver are trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-kling-o3-4k) <br>
- [PoYo Kling O3 API model page](https://poyo.ai/models/kling-o3-api) <br>
- [PoYo Kling O3 4K API docs](https://docs.poyo.ai/api-manual/video-series/kling-o3-4k) <br>
- [Skill API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payload examples and bash curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a PoYo task_id after an explicit live submission.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
