## Description: <br>
Helps agents prepare, submit, and follow up on PoYo Kling 1.6 video-generation jobs for text-to-video, image-to-video, first/last-frame, element-reference, polling, and webhook workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to construct valid PoYo Kling 1.6 Standard or Pro requests, submit prepared JSON payloads from a trusted shell when requested, and report the resulting task identifier with polling or webhook next steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API credentials can be exposed if copied into browser code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Store POYO_API_KEY only in a trusted server-side environment or secret manager and avoid echoing it in generated commands or responses. <br>
Risk: Prompts, source images, reference image URLs, and callback URLs may contain sensitive information sent to PoYo or a webhook receiver. <br>
Mitigation: Review payloads before submission and avoid confidential prompts, private image URLs, or sensitive callback URLs unless the user accepts that data handling. <br>
Risk: Submitting a prepared payload makes a live external API call. <br>
Mitigation: Submit only when the user explicitly requests execution from a trusted shell and has provided the required server-side environment. <br>


## Reference(s): <br>
- [PoYo Kling 1.6 API Reference](artifact/references/api.md) <br>
- [PoYo Kling 1.6 API Docs](https://docs.poyo.ai/api-manual/video-series/kling-1-6) <br>
- [PoYo Kling 1.6 Model Page](https://poyo.ai/models/kling-1-6) <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/poyo-kling-1-6) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash or curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the selected model id, request mode, parameter summary, submitted task_id, and polling or webhook next step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
