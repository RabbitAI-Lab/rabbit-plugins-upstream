## Description: <br>
Helps agents prepare, submit, and follow up on PoYo Sora 2 Pro Official video generation jobs using the PoYo API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create text-to-video or single-image guided video payloads for PoYo, submit asynchronous Sora 2 Pro Official tasks, and plan polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY server-side in environment variables or a backend secret manager and avoid echoing it in generated commands or responses. <br>
Risk: Prompts, source image URLs, or callback URLs may contain confidential information sent to PoYo or a webhook receiver. <br>
Mitigation: Review payloads before submission and avoid sending confidential prompts, private image URLs, or sensitive callback URLs unless the user trusts PoYo and the receiver. <br>
Risk: Live API calls can start billable or irreversible video generation jobs. <br>
Mitigation: Submit only when the user explicitly asks and provides a trusted server-side environment. <br>


## Reference(s): <br>
- [PoYo Sora 2 Pro Official API Reference](references/api.md) <br>
- [PoYo Sora 2 Pro Official model page](https://poyo.ai/models/sora-2-official) <br>
- [PoYo Sora 2 Pro Official API docs](https://docs.poyo.ai/api-manual/video-series/sora-2-pro-official) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-sora-2-pro-official-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and curl or shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the selected model id, request mode, payload summary, generated task_id, and next polling or webhook step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
