## Description: <br>
Helps agents prepare, submit, and track Kling 3.0 video generation jobs through PoYo's API for text-to-video, image-to-video, multi-shot, reference-element, sound, polling, and webhook workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to create PoYo Kling 3.0 request payloads, submit trusted JSON with curl when explicitly requested, and report task IDs plus polling or webhook next steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed through browser code, logs, public repositories, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY server-side in environment variables or a backend secret manager, and never pass it as a command-line argument. <br>
Risk: Prompts, private image URLs, or callback URLs may disclose sensitive information to PoYo or a callback receiver. <br>
Mitigation: Avoid submitting confidential prompts, private source images, or sensitive callback URLs unless the user trusts PoYo and the callback receiver. <br>
Risk: Unreviewed payloads can trigger unintended external video-generation requests. <br>
Mitigation: Review payloads before submission and make live API calls only when the user explicitly asks from a safe server-side environment. <br>


## Reference(s): <br>
- [PoYo Kling 3 API model page](https://poyo.ai/models/kling-3-api) <br>
- [PoYo Kling 3.0 API docs](https://docs.poyo.ai/api-manual/video-series/kling-3-0) <br>
- [Local PoYo Kling 3.0 API reference](references/api.md) <br>
- [ClawHub Kling 3 release page](https://clawhub.ai/coolhackboy/skills/kling-3) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include PoYo task IDs and polling or webhook next steps when a request is submitted.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
