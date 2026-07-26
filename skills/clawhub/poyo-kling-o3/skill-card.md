## Description: <br>
Poyo Kling O3 helps agents prepare and submit PoYo Kling O3 video-generation requests, including text-to-video, image-to-video, reference-to-video, multi-shot payloads, polling, and webhook guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to build PoYo Kling O3 video-generation payloads, submit asynchronous jobs, and guide follow-up through status polling or webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys may be exposed if placed in browser code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager, and avoid echoing secrets in generated commands or responses. <br>
Risk: Prompts, source media URLs, reference images, or callback URLs may disclose confidential information to PoYo or webhook receivers. <br>
Mitigation: Review payload JSON before submission and send sensitive inputs only when the user trusts PoYo and the callback receiver. <br>
Risk: The submit script performs a live network request to PoYo when run with a prepared payload. <br>
Mitigation: Run submission only after explicit user intent from a trusted shell, then report the returned task_id for polling or webhook follow-up. <br>


## Reference(s): <br>
- [PoYo Kling O3 model page](https://poyo.ai/models/kling-o3-api) <br>
- [PoYo Kling O3 API docs](https://docs.poyo.ai/api-manual/video-series/kling-o3) <br>
- [Skill API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-kling-o3) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON payloads, curl commands, task IDs, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
