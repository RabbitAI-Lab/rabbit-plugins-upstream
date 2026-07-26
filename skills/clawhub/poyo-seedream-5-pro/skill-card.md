## Description: <br>
Provides guidance for using PoYo Seedream 5.0 Pro image generation and editing, including model selection, request payload preparation, optional shell submission, and task tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to prepare and optionally submit PoYo Seedream 5.0 Pro text-to-image or reference-image editing jobs after reviewing payloads and API-key handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys could be exposed through logs, client-side code, screenshots, repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment variable or secret manager and send it only as an Authorization header. <br>
Risk: Private reference images, generated image URLs, or callback URLs could disclose sensitive data to the provider or receiver. <br>
Mitigation: Submit private inputs or callback URLs only when the user trusts PoYo and the callback receiver, and avoid placing generated URLs in public logs. <br>
Risk: Unreviewed payloads could submit unintended model settings, images, or prompts. <br>
Mitigation: Review the payload JSON before submission and make live API calls only after an explicit user request in a trusted server-side environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-seedream-5-pro) <br>
- [PoYo Seedream 5.0 Pro model page](https://poyo.ai/models/seedream-5-0-pro) <br>
- [PoYo Seedream 5.0 Pro API docs](https://docs.poyo.ai/api-manual/image-series/seedream-5-0-pro) <br>
- [PoYo task status docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [Local API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payload summaries and optional bash/curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the selected model, mode, payload summary, reference-image count, output settings, returned task_id, and next status-check step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
