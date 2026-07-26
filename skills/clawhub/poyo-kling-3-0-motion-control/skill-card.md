## Description: <br>
Kling 3.0 motion control video generation on PoYo via the PoYo generate API, using one reference image, one reference video, character orientation control, optional prompts, polling, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and submit PoYo Kling 3.0 motion-control video jobs that combine a reference image with a reference video. It is useful for building payloads, choosing character orientation and resolution, and planning polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys can be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment or secret manager and avoid echoing it in generated commands or responses. <br>
Risk: Submitting private media, prompts, or callback URLs shares that data with PoYo and any callback receiver. <br>
Mitigation: Review payloads before submission and send private assets or callback URLs only when the user trusts PoYo and the receiver. <br>
Risk: Live API calls can create video-generation jobs with external service effects. <br>
Mitigation: Make live submissions only after the user explicitly asks and provides a trusted shell environment. <br>


## Reference(s): <br>
- [PoYo Kling 3.0 Motion Control model page](https://poyo.ai/models/kling-3-0-motion-control) <br>
- [PoYo Kling 3.0 Motion Control API docs](https://docs.poyo.ai/api-manual/video-series/kling-3-0-motion-control) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [Local API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-kling-3-0-motion-control) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payload examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, payload summary, media roles, selected character orientation, resolution, task_id, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
