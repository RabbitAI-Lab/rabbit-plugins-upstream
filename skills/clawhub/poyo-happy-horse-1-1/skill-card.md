## Description: <br>
Helps agents prepare, submit, and follow up on PoYo Happy Horse 1.1 text-to-video, image-to-video, and reference-to-video generation jobs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to build PoYo Happy Horse 1.1 video-generation requests, choose request parameters, submit trusted payloads, and explain polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A PoYo API key can be exposed if included in browser code, public files, logs, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment variable or secret manager and avoid echoing or logging it. <br>
Risk: Prompts, media URLs, reference images, and callback URLs may contain private data submitted to PoYo or a callback receiver. <br>
Mitigation: Submit only content the user is comfortable sharing with PoYo and any callback endpoint involved in the workflow. <br>
Risk: Live submissions can consume PoYo credits. <br>
Mitigation: Make live API calls only after explicit user approval and from a trusted shell or backend environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-happy-horse-1-1) <br>
- [PoYo Happy Horse 1.1 model page](https://poyo.ai/models/happy-horse-1-1) <br>
- [PoYo Happy Horse 1.1 API documentation](https://docs.poyo.ai/api-manual/video-series/happy-horse-1-1) <br>
- [PoYo API key dashboard](https://poyo.ai/dashboard/api-key) <br>
- [Local API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON payload examples and bash/curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require POYO_API_KEY and explicit user approval for live API calls; submitted jobs return a task_id for polling or webhook follow-up.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
