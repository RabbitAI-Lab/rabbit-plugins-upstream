## Description: <br>
Helps agents submit Kling 2.6 Motion Control jobs to PoYo for motion transfer, character animation, orientation control, and 720p or 1080p video output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and submit PoYo Kling 2.6 Motion Control requests that animate a character image from a reference video, then preserve the returned task_id for polling or callback follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and image or video URLs are sent to PoYo using POYO_API_KEY. <br>
Mitigation: Avoid submitting sensitive personal or proprietary media unless PoYo's terms and data handling are acceptable for the intended use. <br>
Risk: The skill depends on a third-party PoYo API key and external API availability. <br>
Mitigation: Confirm POYO_API_KEY is configured and handle task submission or status failures before relying on generated task_ids. <br>


## Reference(s): <br>
- [PoYo Kling 2.6 Motion Control model page](https://poyo.ai/models/kling-2-6-motion-control) <br>
- [PoYo Kling 2.6 Motion Control API docs](https://docs.poyo.ai/api-manual/video-series/kling-2.6-motion-control) <br>
- [PoYo Kling 2.6 Motion Control OpenAPI JSON](https://docs.poyo.ai/api-manual/video-series/kling-2.6-motion-control.json) <br>
- [PoYo task status docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-kling-2-6-motion-control) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the chosen model id, final payload or parameter summary, whether reference images are involved, returned task_id, and the next polling or webhook step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
