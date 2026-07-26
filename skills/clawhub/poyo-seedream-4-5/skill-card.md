## Description: <br>
Helps agents prepare and submit PoYo Seedream 4.5 image generation and editing requests, including high-resolution, multi-reference, and follow-up status workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare Seedream 4.5 generation or edit payloads, submit them to PoYo with POYO_API_KEY, and report task IDs for follow-up status checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, reference image URLs, callback URLs, and request payloads are sent to PoYo when a request is submitted. <br>
Mitigation: Review payloads before submission and avoid sensitive prompts, private image URLs, or callback URLs unless the user is comfortable sending them to PoYo. <br>
Risk: The skill depends on a bearer API key and curl for external API calls. <br>
Mitigation: Set POYO_API_KEY knowingly, avoid exposing it in chat or logs, and confirm the request target before running submission commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-seedream-4-5) <br>
- [PoYo Seedream 4.5 model page](https://poyo.ai/models/seedream-4-5-api) <br>
- [PoYo Seedream 4.5 API docs](https://docs.poyo.ai/api-manual/image-series/seedream-4-5) <br>
- [PoYo Seedream 4.5 OpenAPI JSON](https://docs.poyo.ai/api-manual/image-series/seedream-4-5.json) <br>
- [PoYo task status docs](https://docs.poyo.ai/api-manual/task-management/status) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payload examples and shell command usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model id, request payload summary, reference-image status, returned task_id, and polling or webhook next step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
