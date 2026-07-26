## Description: <br>
Omni Flash video generation on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `omni-flash`, text-to-video, single-image video, three-image reference fusion, video-input generation, 720p, 1080p, 4k, duration control, aspect ratio control, polling, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Omni Flash video-generation requests, submit trusted JSON payloads, and guide follow-up polling or webhook handling for text-to-video, image-to-video, reference-fusion, and video-input workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, media URLs, and callback URLs may be sent to PoYo during video-generation workflows. <br>
Mitigation: Review payloads before submission and use confidential prompts, media, or callback receivers only when PoYo is approved for that data. <br>
Risk: POYO_API_KEY is required for live API submission and could be exposed through logs, frontend code, screenshots, repositories, or chat output. <br>
Mitigation: Keep the key in a server-side environment variable or secret manager and avoid logging or displaying it. <br>
Risk: The helper can submit live asynchronous generation jobs when run from a trusted shell. <br>
Mitigation: Make live API calls only after explicit user approval, validate the prepared JSON payload, and save the returned task_id for polling or webhook follow-up. <br>


## Reference(s): <br>
- [PoYo Omni Flash API Reference](references/api.md) <br>
- [PoYo Omni Flash model page](https://poyo.ai/models/omni-flash) <br>
- [PoYo Omni Flash API docs](https://docs.poyo.ai/api-manual/video-series/omni-flash) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-omni-flash) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads, curl examples, shell commands, and concise status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model id, workflow type, request payload or parameter summary, media inputs, task_id, and polling or webhook next step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
