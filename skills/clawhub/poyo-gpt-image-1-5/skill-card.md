## Description: <br>
Use PoYo AI GPT Image 1.5 through the https://api.poyo.ai/api/generate/submit endpoint to prepare PoYo-compatible generation or edit payloads, submit jobs, and poll task status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to generate or edit media with PoYo GPT Image 1.5 models, prepare request payloads, submit authenticated jobs, and preserve task IDs for polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, image URLs, masks, callback URLs, and payload files are sent to PoYo as part of the skill's stated API workflow. <br>
Mitigation: Use the skill only when that transfer is acceptable, and avoid submitting secrets, private internal URLs, sensitive images, or sensitive payload data. <br>
Risk: Authenticated submissions require a PoYo API key. <br>
Mitigation: Provide the key through POYO_API_KEY or an explicit argument only at execution time, and do not embed it in saved payloads, examples, or shared logs. <br>


## Reference(s): <br>
- [PoYo GPT Image 1.5 model page](https://poyo.ai/models/gpt-image-1-5-api) <br>
- [PoYo GPT Image 1.5 API docs](https://docs.poyo.ai/api-manual/image-series/gpt-image-1.5) <br>
- [PoYo GPT Image 1.5 OpenAPI JSON](https://docs.poyo.ai/api-manual/image-series/gpt-image-1.5.json) <br>
- [PoYo task status docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [Local API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads, curl examples, and shell command usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include chosen model id, payload summary, reference-image usage, returned task_id, and next-step polling or webhook guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
