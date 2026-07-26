## Description: <br>
Helps agents prepare, submit, and follow up on PoYo Wan 2.5 text-to-video or image-to-video generation jobs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to build or submit PoYo Wan 2.5 video generation requests, including payload parameters, async task submission, and polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys or sensitive request data could be exposed through browser code, logs, prompts, screenshots, payloads, callback URLs, or generated media URLs. <br>
Mitigation: Keep POYO_API_KEY in server-side secrets, review payload JSON before submission, and avoid sending sensitive prompts or private URLs unless PoYo handling is acceptable. <br>
Risk: A live submission can create media or consume credits before the request has been reviewed. <br>
Mitigation: Make live API calls only after explicit user approval from a trusted shell, then report and retain the returned task_id for polling or webhook follow-up. <br>


## Reference(s): <br>
- [PoYo Wan 2.5 model page](https://poyo.ai/models/wan-2-5) <br>
- [PoYo Wan 2.5 text-to-video API docs](https://docs.poyo.ai/api-manual/video-series/wan2.5-text-to-video) <br>
- [PoYo Wan 2.5 image-to-video API docs](https://docs.poyo.ai/api-manual/video-series/wan2.5-image-to-video) <br>
- [Artifact API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads and curl or bash commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May submit a prepared JSON payload when POYO_API_KEY is configured and the user explicitly requests a live API call.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
