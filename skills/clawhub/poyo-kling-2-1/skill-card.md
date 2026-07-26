## Description: <br>
Helps agents prepare and submit PoYo Kling 2.1 image-to-video generation tasks for Standard or Pro models, including start frames, optional Pro end frames, duration, negative prompts, polling, and webhook guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to assemble PoYo Kling 2.1 Standard or Pro image-to-video requests, submit prepared JSON payloads from a trusted shell, and explain follow-up polling or webhook handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, image URLs, callback URLs, and generated media workflow data may be submitted to PoYo during use. <br>
Mitigation: Use only trusted PoYo and callback endpoints, and avoid submitting private media or confidential prompts unless the user has approved that data flow. <br>
Risk: POYO_API_KEY could be exposed through chat, logs, browser code, or public repositories. <br>
Mitigation: Keep the key in server-side environment variables or a secret manager and redact it from output, logs, screenshots, and frontend bundles. <br>


## Reference(s): <br>
- [PoYo Kling 2.1 model page](https://poyo.ai/models/kling-2-1) <br>
- [PoYo Kling 2.1 API docs](https://docs.poyo.ai/api-manual/video-series/kling-2-1) <br>
- [Local PoYo Kling 2.1 API Reference](references/api.md) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include prepared request payloads, task IDs after submission, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
