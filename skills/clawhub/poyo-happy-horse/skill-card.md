## Description: <br>
Happy Horse video generation on PoYo via async API task submission for text-to-video, image-to-video, and reference-driven short video workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare Happy Horse payloads, submit PoYo video-generation tasks, and plan polling or webhook follow-up. It supports text-only prompts and source-media workflows with optional image URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed if copied into frontend code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY server-side in environment variables or a secret manager and avoid displaying the key in generated examples or responses. <br>
Risk: Prompts, private media URLs, and callback URLs are sent to PoYo when a live task is submitted. <br>
Mitigation: Review payloads before submission and avoid sending private prompts, private media URLs, or callback URLs unless the user accepts sharing them with PoYo. <br>
Risk: Live API calls create external network requests and asynchronous video-generation tasks. <br>
Mitigation: Make live calls only when the user explicitly asks and a trusted server-side environment with POYO_API_KEY is available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-happy-horse) <br>
- [PoYo Happy Horse model page](https://poyo.ai/models/happy-horse) <br>
- [PoYo Happy Horse API docs](https://docs.poyo.ai/api-manual/video-series/happy-horse) <br>
- [PoYo Happy Horse API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the PoYo model id, request payload, source-media status, returned task_id, and polling or webhook next steps; live submission requires POYO_API_KEY.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
