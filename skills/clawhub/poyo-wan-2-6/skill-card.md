## Description: <br>
Helps agents prepare and submit PoYo Wan 2.6 text-to-video, image-to-video, and video-to-video generation jobs with model-specific payload guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to choose a Wan 2.6 model variant, assemble a valid PoYo generation payload, submit it with POYO_API_KEY, and track task status by task_id, polling, or webhook. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [PoYo Wan 2.6 Model Page](https://poyo.ai/models/wan-2-6) <br>
- [PoYo Wan 2.6 API Docs](https://docs.poyo.ai/api-manual/video-series/wan-2-6) <br>
- [PoYo Task Status Docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [PoYo Wan 2.6 OpenAPI JSON](https://docs.poyo.ai/api-manual/video-series/wan-2-6.json) <br>
- [Local API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with JSON payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and POYO_API_KEY. Generation prompts and media URLs are sent to PoYo; use callback_url only for endpoints the user controls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
