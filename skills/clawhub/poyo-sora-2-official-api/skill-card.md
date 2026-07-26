## Description: <br>
Sora 2 Official video generation on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `sora-2-official`, text-to-video, optional single-image guided video, 4/8/12/16/20 second duration, vertical or landscape video, polling, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Sora 2 Official text-to-video or single-image guided video requests, submit prepared JSON payloads when explicitly asked, and explain polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed through browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment or secret manager and avoid echoing credentials in generated examples or command output. <br>
Risk: Prompts, source image URLs, or callback URLs may contain confidential or sensitive information sent to PoYo or a webhook receiver. <br>
Mitigation: Review payloads before submission and avoid confidential prompts, private image URLs, or sensitive callback URLs unless the user trusts PoYo and the callback endpoint. <br>
Risk: A live submission starts an external asynchronous video-generation task. <br>
Mitigation: Submit only when the user explicitly requests execution from a trusted shell with a prepared payload, then report the returned task_id for controlled follow-up. <br>


## Reference(s): <br>
- [PoYo Sora 2 Official API Reference](references/api.md) <br>
- [PoYo Sora 2 Official Model Page](https://poyo.ai/models/sora-2-official) <br>
- [PoYo Sora 2 Official API Docs](https://docs.poyo.ai/api-manual/video-series/sora-2-official) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration guidance, API payloads] <br>
**Output Format:** [Markdown with JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, request mode, payload summary, duration, aspect ratio, reference-image status, task_id after submission, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
