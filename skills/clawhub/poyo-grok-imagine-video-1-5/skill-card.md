## Description: <br>
Grok Imagine Video 1.5 image-to-video generation on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `grok-imagine-video-1.5`, one source image, prompt-driven motion, 480p or 720p output, duration control, polling, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Grok Imagine Video 1.5 image-to-video payloads, submit trusted asynchronous generation jobs, and explain polling or webhook follow-up for one source image. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys can be exposed if placed in browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment or backend secret manager and avoid echoing it in generated commands or output. <br>
Risk: Submitting a job sends prompts and image URLs to PoYo and may expose callback URLs to the configured receiver. <br>
Mitigation: Submit only non-confidential images, prompts, and callback URLs unless the user trusts PoYo and the callback receiver. <br>
Risk: Live API calls can spend credits or transmit data unintentionally. <br>
Mitigation: Make live submissions only when the user explicitly asks and provides a trusted shell environment with POYO_API_KEY configured. <br>


## Reference(s): <br>
- [PoYo Grok Imagine Video 1.5 API Reference](artifact/references/api.md) <br>
- [PoYo Grok Imagine Video 1.5 Model Page](https://poyo.ai/models/grok-imagine-video-1-5) <br>
- [PoYo Grok Imagine Video 1.5 API Docs](https://docs.poyo.ai/api-manual/video-series/grok-imagine-video-1-5) <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/poyo-grok-imagine-video-1-5) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with JSON payloads and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, payload summary, source image role, duration, resolution, returned task_id, and next-step polling or webhook guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
