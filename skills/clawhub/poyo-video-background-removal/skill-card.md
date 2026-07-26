## Description: <br>
Remove backgrounds from hosted videos on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `poyo-ai/video-background-removal`, transparent video output, container and codec controls, audio preservation, async status polling, callbacks, and server-side integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo video background-removal payloads, generate curl commands, submit approved async jobs, and explain polling or webhook follow-up for hosted video cutout workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill submits hosted video URLs and optional callback URLs to PoYo for processing. <br>
Mitigation: Use it only when PoYo is the intended provider, review the payload before submission, and avoid sending private video or callback URLs unless they are appropriate for PoYo to process. <br>
Risk: The PoYo API key could be exposed if included in browser code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager and do not log raw authorization headers. <br>
Risk: The bundled submit script can make a live API request with curl when given a payload file. <br>
Mitigation: Run it only from a trusted shell after the user has confirmed the payload should be sent to PoYo. <br>


## Reference(s): <br>
- [PoYo Video Background Removal model page](https://poyo.ai/models/video-background-removal) <br>
- [PoYo Video Background Removal API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with JSON payloads and bash curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include task IDs, polling guidance, webhook notes, and server-side environment variable guidance for POYO_API_KEY.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
