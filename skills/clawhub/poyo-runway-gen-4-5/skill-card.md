## Description: <br>
Runway Gen-4.5 video generation on PoYo via the PoYo submit API, supporting text-to-video, optional single-image guidance, clip duration and aspect-ratio controls, seeded output, polling, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill to prepare PoYo Runway Gen-4.5 video-generation payloads, submit trusted jobs, and explain polling or webhook follow-up. It is intended for text-to-video and optional single-image guided video workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: POYO_API_KEY exposure could grant unauthorized access to the user's PoYo account. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment variable or secret manager and never place it in browser code, logs, repositories, screenshots, or chat output. <br>
Risk: Prompts, reference image URLs, callback URLs, and generated video jobs are submitted to PoYo. <br>
Mitigation: Use the skill only when the user trusts PoYo with those inputs and avoid submitting confidential source images, private prompts, or private callback URLs without that trust. <br>
Risk: Live submissions can create external jobs and may have account or cost effects. <br>
Mitigation: Submit requests only after explicit user approval from a trusted shell with a prepared payload. <br>


## Reference(s): <br>
- [PoYo Runway Gen-4.5 API Reference](references/api.md) <br>
- [PoYo Runway Gen-4.5 Model Page](https://poyo.ai/models/runway-gen-4-5) <br>
- [PoYo Runway Gen-4.5 API Docs](https://docs.poyo.ai/api-manual/video-series/runway-gen-4-5) <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/poyo-runway-gen-4-5) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a returned task_id and the recommended next step to poll status or wait for a webhook.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
