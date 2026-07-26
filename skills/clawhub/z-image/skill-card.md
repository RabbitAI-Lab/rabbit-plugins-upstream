## Description: <br>
Use PoYo AI Z-Image for prompt-based image generation through the PoYo generation API, including payload preparation, submission, and task tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to build PoYo Z-Image requests, submit text-to-image jobs, and track returned task identifiers for polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a PoYo API key and can submit prompts or payloads to an external image generation endpoint. <br>
Mitigation: Confirm the request payload and destination before execution, provide POYO_API_KEY through a secret-aware environment, and approve each external submission explicitly. <br>
Risk: Task tracking depends on preserving the task_id returned by the PoYo API. <br>
Mitigation: Report and store the returned task_id immediately so follow-up polling or webhook handling can be tied to the correct request. <br>


## Reference(s): <br>
- [PoYo Z-Image Model Page](https://poyo.ai/models/z-image) <br>
- [PoYo Z-Image API Docs](https://docs.poyo.ai/api-manual/image-series/z-image) <br>
- [PoYo Z-Image OpenAPI JSON](https://docs.poyo.ai/api-manual/image-series/z-image.json) <br>
- [PoYo Task Status Docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [PoYo Z Image API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the selected model id, request payload summary, reference-image status, returned task_id, and next-step polling or webhook guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
