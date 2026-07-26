## Description: <br>
Use PoYo AI Veo 3.1 for frame-conditioned video generation through the `https://api.poyo.ai/api/generate/submit` endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and submit PoYo VEO 3.1 video-generation jobs, choose fast or quality model variants, configure reference images and output settings, and track returned task IDs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends video prompts, reference image URLs, callback URLs, and a PoYo API key to the PoYo API. <br>
Mitigation: Use it only when intending to submit data to PoYo, avoid sensitive or private media unless PoYo handling is trusted, and keep POYO_API_KEY out of logs and shared payloads. <br>
Risk: Generated payloads may include externally reachable callback URLs. <br>
Mitigation: Use callback URLs only when the endpoint is controlled by the user and appropriate for receiving task completion data. <br>


## Reference(s): <br>
- [PoYo VEO 3 1 API Reference](references/api.md) <br>
- [PoYo Veo 3.1 model page](https://poyo.ai/models/veo-3-1) <br>
- [PoYo Veo 3.1 API docs](https://docs.poyo.ai/api-manual/video-series/veo-3-1) <br>
- [PoYo Veo 3.1 OpenAPI JSON](https://docs.poyo.ai/api-manual/video-series/veo-3-1.json) <br>
- [PoYo task status docs](https://docs.poyo.ai/api-manual/task-management/status) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the selected model ID, final payload or parameter summary, reference image involvement, returned task_id, and next polling or webhook step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
