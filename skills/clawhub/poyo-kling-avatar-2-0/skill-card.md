## Description: <br>
Helps agents prepare and submit PoYo Kling Avatar 2.0 audio-driven avatar video jobs, then guide polling or webhook follow-up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare one-image, one-audio PoYo Kling Avatar 2.0 requests, submit them when explicitly authorized, and explain status polling or webhook handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed if placed in browser code, public files, logs, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager and avoid echoing secrets in generated examples or logs. <br>
Risk: Avatar reference images, driving audio, private prompts, and callback URLs may contain sensitive personal or operational information. <br>
Mitigation: Submit private likeness images, confidential audio, private prompts, or sensitive callback URLs only when the user trusts PoYo and the callback endpoint. <br>
Risk: Live avatar generation requests may send user-provided media and prompts to PoYo. <br>
Mitigation: Make live API calls only when explicitly requested by the user and after reviewing the payload JSON. <br>


## Reference(s): <br>
- [PoYo Kling Avatar 2.0 Model Page](https://poyo.ai/models/kling-avatar-2-0) <br>
- [PoYo Kling Avatar 2.0 API Documentation](https://docs.poyo.ai/api-manual/video-series/kling-avatar-2-0) <br>
- [Local API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/poyo-kling-avatar-2-0) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payload examples and bash or curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model IDs, final payloads or parameter summaries, task IDs from submitted requests, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
