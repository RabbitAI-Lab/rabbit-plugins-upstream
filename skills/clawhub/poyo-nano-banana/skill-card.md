## Description: <br>
PoYo Nano Banana helps agents prepare, submit, and follow up on PoYo image generation or image editing jobs through the PoYo submit endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to build Nano Banana or Nano Banana Edit payloads, submit authenticated PoYo image generation or editing jobs, and keep the returned task_id available for polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, callback URLs, and referenced image URLs are sent to the external PoYo API. <br>
Mitigation: Use the skill only when that external processing is acceptable, and avoid confidential, regulated, or private images unless approved for PoYo processing. <br>
Risk: API keys can be exposed if passed directly on the command line or included in shared logs. <br>
Mitigation: Prefer POYO_API_KEY from the environment and avoid pasting credentials into prompts, payload examples, or transcripts. <br>


## Reference(s): <br>
- [PoYo Nano Banana model page](https://poyo.ai/models/nano-banana-api) <br>
- [PoYo Nano Banana API docs](https://docs.poyo.ai/api-manual/image-series/nano-banana) <br>
- [PoYo Nano Banana OpenAPI JSON](https://docs.poyo.ai/api-manual/image-series/nano-banana.json) <br>
- [PoYo task status docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [Local API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the chosen model id, payload summary, reference-image status, returned task_id, and polling or webhook next step.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
