## Description: <br>
Seedream 5.0 Lite image generation and editing on PoYo via the documented PoYo generation API, including 2K/3K output, multi-reference editing, and aspect-ratio control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and submit Seedream 5.0 Lite image generation or editing requests through PoYo, including payload selection, curl examples, task submission, and follow-up polling guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, callback URLs, and reference image URLs are sent to PoYo for processing. <br>
Mitigation: Review request payloads before submission and avoid sending sensitive data unless PoYo use is intended. <br>
Risk: Requests require POYO_API_KEY and may consume account credits. <br>
Mitigation: Keep the API key in the environment, confirm output count and size before submission, and submit only payloads the user has approved. <br>


## Reference(s): <br>
- [PoYo Seedream 5.0 Lite model page](https://poyo.ai/models/seedream-5-0-lite-api) <br>
- [PoYo Seedream 5.0 Lite API docs](https://docs.poyo.ai/api-manual/image-series/seedream-5-0-lite) <br>
- [PoYo Seedream 5.0 Lite OpenAPI JSON](https://docs.poyo.ai/api-manual/image-series/seedream-5-0-lite.json) <br>
- [PoYo task status docs](https://docs.poyo.ai/api-manual/task-management/status) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model id, payload summary, reference-image status, returned task_id, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
