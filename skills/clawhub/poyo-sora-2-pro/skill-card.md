## Description: <br>
Use PoYo AI Sora 2 Pro to prepare and submit 15s or 25s video-generation jobs with optional storyboard, style preset, image-to-video, and payload guidance through PoYo's submit endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to build PoYo Sora 2 Pro request payloads, submit video-generation tasks with curl or the included shell helper, and track returned task IDs for polling or callbacks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User prompts, image URLs, and callback URLs are sent to PoYo's external API. <br>
Mitigation: Use the skill only when PoYo's privacy and retention terms fit the data, and avoid submitting confidential prompts, private image URLs, or sensitive callback URLs. <br>
Risk: The PoYo API key can be exposed if it is passed directly on the command line or included in shared logs. <br>
Mitigation: Prefer setting POYO_API_KEY as an environment variable and avoid recording commands or outputs that contain credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-sora-2-pro) <br>
- [PoYo Sora 2 Pro model page](https://poyo.ai/models/sora-2-pro) <br>
- [PoYo Sora 2 Pro API docs](https://docs.poyo.ai/api-manual/video-series/sora-2-pro) <br>
- [PoYo Sora 2 Pro OpenAPI JSON](https://docs.poyo.ai/api-manual/video-series/sora-2-pro.json) <br>
- [PoYo task status docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [Local API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON payloads and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a chosen model id, request payload or concise parameter summary, reference-image status, returned task_id, and polling or webhook next step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
