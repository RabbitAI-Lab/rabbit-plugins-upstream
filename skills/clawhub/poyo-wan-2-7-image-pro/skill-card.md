## Description: <br>
Helps agents prepare and submit PoYo Wan 2.7 Image Pro text-to-image and image-editing requests, including payload fields, polling, and webhook follow-up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Wan 2.7 Image Pro generation or editing payloads, submit trusted async image jobs, and guide polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed through browser code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY server-side in environment variables or a backend secret manager and avoid printing or committing it. <br>
Risk: Prompts, source image URLs, or callback URLs may contain confidential information sent to PoYo or a webhook receiver. <br>
Mitigation: Submit private prompts, images, or callback URLs only when the user trusts PoYo and the callback receiver. <br>
Risk: Live image-generation submissions can spend external API quota or create unintended tasks. <br>
Mitigation: Make live submissions only after the user explicitly requests them and the payload has been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-wan-2-7-image-pro) <br>
- [PoYo Wan 2.7 Image model page](https://poyo.ai/models/wan-2-7-image) <br>
- [PoYo Wan 2.7 Image Pro API docs](https://docs.poyo.ai/api-manual/image-series/wan-2-7-image-pro) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and curl or shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a returned task_id and next-step guidance to poll status or wait for a webhook after live submission.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
