## Description: <br>
Use APIDot for Seedream 4 API workflows, including 4K image generation, image editing, image-to-image planning, reference image generation, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan APIDot Seedream 4 image generation and editing integrations, route questions to current APIDot documentation, and design async polling or webhook workflows without embedding credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY could be exposed if copied into browser code, logs, public repositories, screenshots, or chat output. <br>
Mitigation: Store APIDOT_API_KEY only in server-side secrets or a backend secret manager and avoid logging credentials. <br>
Risk: Private prompts, source image URLs, generated image URLs, or callback URLs could leak through logs or chat output. <br>
Mitigation: Avoid logging private prompts, image URLs, generated outputs, and callback URLs; share only sanitized examples. <br>
Risk: Live API calls could run in an unintended environment. <br>
Mitigation: Make live APIDot calls only after the user explicitly chooses a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot Seedream 4 Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [Seedream 4 Model Page](https://apidot.ai/models/seedream-4) <br>
- [Seedream 4 API Docs](https://apidot.ai/docs/seedream-4) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown text with API integration guidance and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, automatic network calls, bundled API clients, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
