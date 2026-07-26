## Description: <br>
Helps agents plan, prepare, and optionally submit PoYo Tripo3D text-to-3D, image-to-3D, and multiview-to-3D asset generation requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical artists, and asset pipeline engineers use this skill to choose PoYo Tripo3D models, prepare request payloads, and submit or document 3D asset generation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed if copied into browser code, logs, public files, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager and avoid echoing it in generated commands or responses. <br>
Risk: Private prompts, object image URLs, generated asset URLs, or callback URLs may reveal confidential project details to PoYo or a callback receiver. <br>
Mitigation: Review payloads before submission and avoid sending confidential inputs unless the user accepts sharing them with PoYo and any callback endpoint. <br>


## Reference(s): <br>
- [PoYo Tripo H3.1 model page](https://poyo.ai/models/tripo-h31-3d) <br>
- [PoYo Tripo H3.1 API documentation](https://docs.poyo.ai/api-manual/3d-series/tripo-h31-3d) <br>
- [PoYo Tripo P1 API documentation](https://docs.poyo.ai/api-manual/3d-series/tripo-p1-3d) <br>
- [PoYo Tripo P1 model page](https://poyo.ai/models/tripo-p1-3d) <br>
- [Local PoYo Tripo3D API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-tripo-3d) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with JSON payloads and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model id, workflow type, request payload, task_id, and polling or webhook next steps; live submissions require POYO_API_KEY.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
