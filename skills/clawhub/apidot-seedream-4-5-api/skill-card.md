## Description: <br>
Use APIDot for Seedream 4.5 API workflows, including image generation, image editing, image-to-image, reference image generation, prompt-based image creation, async task submission, task_id handling, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route Seedream 4.5 integration questions to APIDot documentation, examples, and safe async workflow guidance for image generation and editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys could be exposed if copied into browser code, logs, public repositories, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY server-side in environment variables or a backend secret manager, and avoid echoing secrets in generated guidance. <br>
Risk: Private prompts, image URLs, generated image URLs, or callback URLs could be leaked through frontend code or logs. <br>
Mitigation: Avoid logging private request data and keep media references, callbacks, and generated URLs in backend-controlled storage. <br>
Risk: APIDot pricing, limits, availability, or request fields may change after the skill release. <br>
Mitigation: Verify current APIDot docs and model pages before making live API calls or preparing copyable request payloads. <br>


## Reference(s): <br>
- [APIDot Documentation](https://apidot.ai/docs) <br>
- [APIDot Seedream 4.5 Model Page](https://apidot.ai/models/seedream-4-5) <br>
- [APIDot Seedream 4.5 API Docs](https://apidot.ai/docs/seedream-4-5) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Seedream 4.5 Examples](https://github.com/APIDotAI/seedream-4.5-api) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [Local APIDot Seedream 4.5 Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown guidance with API integration notes and links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
