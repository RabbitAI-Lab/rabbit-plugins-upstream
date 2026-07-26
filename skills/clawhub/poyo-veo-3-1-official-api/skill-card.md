## Description: <br>
Helps agents prepare PoYo Veo 3.1 Official video generation payloads, submit asynchronous generation tasks, and guide polling or webhook follow-up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create text-to-video, image-to-video, first/last-frame, and reference-guided video generation requests for PoYo Veo 3.1 Official models. It is useful when a workflow needs a ready payload, curl or shell submission, task status polling, or webhook guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, media URLs, callback URLs, and related request details are sent to PoYo. <br>
Mitigation: Avoid secrets, internal-only URLs, regulated data, and private media unless external sharing with PoYo and the callback receiver is approved. <br>
Risk: The PoYo API key can be exposed if copied into client code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager and redact it from generated examples and logs. <br>
Risk: Live submissions create asynchronous external generation tasks. <br>
Mitigation: Submit only when the user explicitly requests it from a trusted shell, then preserve the returned task_id for polling or webhook follow-up. <br>


## Reference(s): <br>
- [PoYo Veo 3.1 Official API Reference](references/api.md) <br>
- [PoYo Veo 3.1 Official Model Page](https://poyo.ai/models/veo-3-1-official) <br>
- [PoYo Veo 3.1 Official API Docs](https://docs.poyo.ai/api-manual/video-series/veo-3-1-official) <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/poyo-veo-3-1-official-api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash or curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model id, generation mode, request parameters, source media notes, returned task_id, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
