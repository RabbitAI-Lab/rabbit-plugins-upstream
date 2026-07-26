## Description: <br>
Use PoYo AI Hailuo 02 for prompt-optimized video generation and image-to-video workflows through the `https://api.poyo.ai/api/generate/submit` endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to prepare or submit Hailuo 02 and Hailuo 02 Pro video-generation jobs to PoYo, including text-to-video and image-to-video payloads. It helps capture task IDs and choose whether to poll status or wait for webhook callbacks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, image URLs, callback URLs, and generated media are sent to PoYo's external API. <br>
Mitigation: Use only when external PoYo processing is intended, and avoid sending secrets, private images, regulated data, or sensitive business content unless permitted by the user's PoYo account and policies. <br>
Risk: The skill can submit authenticated video-generation jobs using POYO_API_KEY. <br>
Mitigation: Keep the API key in the environment, review payloads before submission, and preserve returned task IDs for follow-up status checks. <br>


## Reference(s): <br>
- [PoYo Hailuo 02 API Reference](references/api.md) <br>
- [PoYo Hailuo 02 Model Page](https://poyo.ai/models/hailuo-02) <br>
- [PoYo Hailuo 02 API Docs](https://docs.poyo.ai/api-manual/video-series/hailuo-02) <br>
- [PoYo Task Status Docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [PoYo Hailuo 02 OpenAPI JSON](https://docs.poyo.ai/api-manual/video-series/hailuo-02.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/hailuo2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payload examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include chosen model ID, final payload or parameter summary, reference-image status, returned task_id, and the next polling or webhook step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
