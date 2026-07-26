## Description: <br>
Poyo Hailuo 2 3 helps agents prepare and submit Hailuo 2.3 video generation requests on PoYo, including text-to-video, optional first-frame guidance, polling, and webhook follow-up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to construct PoYo Hailuo 2.3 video-generation payloads, submit approved jobs with a server-side POYO_API_KEY, and plan polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: POYO_API_KEY exposure could allow unauthorized PoYo API use. <br>
Mitigation: Keep POYO_API_KEY server-side in environment variables or a backend secret manager, and do not place it in browser code, public repositories, logs, screenshots, or chat output. <br>
Risk: Prompts, private source image URLs, or callback URLs may disclose sensitive information to PoYo or a webhook receiver. <br>
Mitigation: Review payloads before submitting and avoid confidential prompts, private image URLs, or sensitive callback URLs unless the user trusts PoYo and the receiving webhook. <br>
Risk: Live submissions can send user content to an external video-generation service. <br>
Mitigation: Make live API calls only when the user explicitly asks and provides a trusted server-side environment. <br>


## Reference(s): <br>
- [PoYo Hailuo 2.3 model page](https://poyo.ai/models/hailuo-2-3) <br>
- [PoYo Hailuo 2.3 API docs](https://docs.poyo.ai/api-manual/video-series/hailuo-2-3) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-hailuo-2-3) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the PoYo model id, prompt mode, duration, resolution, prompt_optimizer setting, returned task_id, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
