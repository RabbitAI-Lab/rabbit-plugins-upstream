## Description: <br>
Use APIDot for Kling 3.0 Turbo API workflows, including fast video previews, Kling 3.0 Turbo Standard, Kling 3.0 Turbo Pro, text-to-video, image-to-video, multi-shot video, multi_prompt, task_id, polling, webhooks, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route Kling 3.0 Turbo integration questions to APIDot documentation, model pages, async job patterns, polling guidance, and webhook guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys, prompts, media URLs, generated video URLs, callback URLs, customer data, and task IDs may be sensitive. <br>
Mitigation: Keep APIDOT_API_KEY server-side, avoid exposing secrets or private media in logs or chat output, and treat workflow identifiers and URLs as sensitive unless the user says they can be shared. <br>
Risk: Live APIDot calls may spend credits or affect production workflows. <br>
Mitigation: Do not make live API calls unless the user explicitly asks and provides a safe server-side environment. <br>
Risk: Model-specific request fields, limits, availability, and commercial terms can change. <br>
Mitigation: Use the current APIDot docs and model pages instead of inventing API facts or copying fields from other model families. <br>


## Reference(s): <br>
- [APIDot Kling 3.0 Turbo Reference](references/api.md) <br>
- [APIDot Documentation](https://apidot.ai/docs) <br>
- [Kling 3.0 Turbo Model Page](https://apidot.ai/models/kling-3-0-turbo) <br>
- [Kling 3.0 Turbo API Docs](https://apidot.ai/docs/kling-3-0-turbo) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown guidance with references to API documentation and integration patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; no bundled scripts, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
