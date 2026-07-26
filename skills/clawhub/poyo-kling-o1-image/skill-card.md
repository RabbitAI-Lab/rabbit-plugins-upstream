## Description: <br>
Poyo Kling O1 Image helps agents prepare and submit PoYo Kling O1 image-editing requests with reference images, optional element guidance, polling, and webhook follow-up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create PoYo API payloads for Kling O1 reference-image editing, submit asynchronous jobs when authorized, and guide polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys or private image URLs could be exposed if they are used in browser code, logs, public repositories, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment or secret manager and avoid logging prompts, private image URLs, generated image URLs, or callback URLs. <br>
Risk: Submitting confidential prompts, source images, generated image URLs, or callback URLs sends them to PoYo and any configured callback receiver. <br>
Mitigation: Submit only data the user is permitted to share and only when the user trusts PoYo and the callback receiver. <br>
Risk: The submit helper makes a live network request to PoYo when run with a payload file. <br>
Mitigation: Review payload JSON and run the script only from a trusted shell after the user explicitly authorizes submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-kling-o1-image) <br>
- [PoYo Kling O1 Image model page](https://poyo.ai/models/kling-o1-image) <br>
- [PoYo Kling O1 API documentation](https://docs.poyo.ai/api-manual/image-series/kling-o1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payload examples and optional curl or bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a PoYo task_id after an authorized submission.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
