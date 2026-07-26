## Description: <br>
Grok Imagine video generation on PoYo via the PoYo generation API, covering text-to-video, image-to-video, short clip duration, and mode selection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to prepare and submit PoYo Grok Imagine video-generation requests, including prompt, optional reference image, duration, aspect ratio, and mode choices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, image URLs, callback URLs, and the POYO_API_KEY are shared with PoYo when requests are submitted. <br>
Mitigation: Review payloads before submission, avoid sensitive data unless appropriate for PoYo processing, and keep POYO_API_KEY in runtime secret handling rather than in checked-in files. <br>
Risk: The helper sends raw JSON directly to the external API. <br>
Mitigation: Validate the model id, prompt, duration, aspect ratio, mode, image URL count, and callback URL before running the submission script. <br>


## Reference(s): <br>
- [PoYo Grok Imagine API Reference](references/api.md) <br>
- [PoYo Grok Imagine Model Page](https://poyo.ai/models/grok-imagine) <br>
- [PoYo Grok Imagine API Docs](https://docs.poyo.ai/api-manual/video-series/grok-imagine) <br>
- [PoYo Task Status Docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [PoYo Grok Imagine OpenAPI JSON](https://docs.poyo.ai/api-manual/video-series/grok-imagine.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the chosen model id, payload summary, reference-image status, returned task_id, and polling or webhook next step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
