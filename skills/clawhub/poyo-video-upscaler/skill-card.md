## Description: <br>
Upscale hosted videos on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `poyo-ai/video-upscaler`, public video URLs, scale control, async status polling, callbacks, and server-side integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare PoYo video-upscaling requests, generate server-side curl or shell command guidance, submit trusted payloads when explicitly requested, and explain task polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys can be exposed if copied into browser code, logs, public repositories, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager, and redact authorization headers from outputs and logs. <br>
Risk: Hosted source video URLs, callback URLs, task IDs, and generated output URLs may reveal private project data. <br>
Mitigation: Review payloads before submission and avoid sending private URLs unless the project policy allows sharing them with PoYo. <br>
Risk: A live API submission can send media-processing data to the hosted PoYo service. <br>
Mitigation: Make live calls only after the user explicitly requests submission, confirms the payload, and provides a trusted server-side shell environment. <br>


## Reference(s): <br>
- [PoYo Video Upscaler API Reference](references/api.md) <br>
- [PoYo Video Upscaler model page](https://poyo.ai/models/video-upscaler) <br>
- [PoYo API key dashboard](https://poyo.ai/dashboard/api-key) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model id, source video URL handling notes, scale value, request payload summary, returned task_id when submitted, and next-step polling or webhook guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
