## Description: <br>
Guides agents through PoYo Hunyuan 3D v3.1 asset generation, including model selection, request payloads, curl submission, polling, and webhook guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical artists use this skill to prepare and submit PoYo Hunyuan 3D v3.1 text-to-3D or image-to-3D asset generation jobs, choose Pro or Rapid models, and plan polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: POYO_API_KEY can be exposed if placed in frontend code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Use POYO_API_KEY only from a server-side or trusted shell environment and keep it in environment variables or a backend secret manager. <br>
Risk: Prompts, source image URLs, generated asset URLs, and callback URLs may contain confidential or proprietary information shared with PoYo. <br>
Mitigation: Avoid submitting confidential inputs or private endpoints unless the user has approved that data sharing with PoYo. <br>
Risk: Live API calls submit external generation jobs and may process user data outside the local environment. <br>
Mitigation: Do not make live API calls unless the user explicitly asks and provides a safe server-side environment. <br>


## Reference(s): <br>
- [PoYo Hunyuan 3D v3.1 model page](https://poyo.ai/models/hunyuan-3d-3-1) <br>
- [PoYo Hunyuan 3D v3.1 API documentation](https://docs.poyo.ai/api-manual/3d-series/hunyuan-3d-3-1) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-hunyuan-3d-3-1) <br>
- [Local API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON payloads and bash/curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a returned task_id when the user explicitly requests live submission from a trusted shell with POYO_API_KEY configured.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
