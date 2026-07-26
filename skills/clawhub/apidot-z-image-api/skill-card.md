## Description: <br>
Use APIDot for Z-Image API workflows, including Alibaba Z-Image, text-to-image API, prompt-based image generation, photorealistic image candidates, aspect ratio planning, safety checker planning, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route APIDot Z-Image questions to the correct docs and plan prompt-based image generation integrations, including async task submission, task_id persistence, polling, webhooks, and API-key handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Real APIDot API calls require an API key and may expose sensitive prompts, callback URLs, generated image URLs, or credentials if handled carelessly. <br>
Mitigation: Keep APIDOT_API_KEY server-side, use a secret manager or server environment variables, and avoid logging keys, private prompts, callback URLs, or generated image URLs. <br>
Risk: Model-specific fields, availability, limits, and commercial terms may change in APIDot documentation. <br>
Mitigation: Use the current APIDot docs and model pages as the source of truth before preparing request payloads or making product claims. <br>
Risk: Async image jobs can be mishandled if task IDs, retries, polling, or webhook callbacks are not persisted and deduplicated. <br>
Mitigation: Persist task_id, selected model, prompt metadata, status, and final URLs together; treat webhook handlers as idempotent and retry only transient failures with backoff. <br>


## Reference(s): <br>
- [APIDot Z-Image Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Z-Image Model Page](https://apidot.ai/models/z-image) <br>
- [APIDot Z-Image API Docs](https://apidot.ai/docs/z-image) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text with optional code and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files or automatic network calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
