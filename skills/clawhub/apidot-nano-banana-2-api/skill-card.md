## Description: <br>
Use APIDot for Nano Banana 2 API workflows, including Gemini 3.1 Flash Image API, nano-banana-2, nano-banana-2-edit, text-to-image API, image editing API, readable text image generation, async task submission, task_id handling, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this documentation-only skill to find APIDot Nano Banana 2 docs, plan image generation or editing workflows, and follow async task polling or webhook integration guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys could be exposed if copied into browser code, logs, public repositories, screenshots, or chat output. <br>
Mitigation: Store APIDOT_API_KEY only in a backend secret store or server-side environment variable, and avoid logging or displaying it. <br>
Risk: Private prompts, image URLs, generated image URLs, or callback URLs may contain sensitive user or workflow data. <br>
Mitigation: Avoid logging private prompts and media URLs, validate source image URLs before submitting jobs, and treat webhook handlers as idempotent. <br>
Risk: Model fields, pricing, availability, limits, or commercial terms may change after the skill release. <br>
Mitigation: Verify the current APIDot docs, model page, pricing, and request fields before making live API calls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-nano-banana-2-api) <br>
- [APIDot documentation](https://apidot.ai/docs) <br>
- [APIDot Nano Banana 2 model page](https://apidot.ai/models/nano-banana-2) <br>
- [APIDot Nano Banana 2 docs](https://apidot.ai/docs/nano-banana-2) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Nano Banana 2 examples](https://github.com/APIDotAI/nano-banana-2-api) <br>
- [Local APIDot Nano Banana 2 reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API integration notes and links to current APIDot references.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, bundled clients, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
