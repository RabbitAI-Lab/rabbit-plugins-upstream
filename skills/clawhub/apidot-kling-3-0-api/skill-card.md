## Description: <br>
Use APIDot for Kling 3.0 API workflows, including Kling 3.0 Standard, Kling 3.0 Pro, Kling 3.0 4K, text-to-video API, image-to-video API, multi-shot video, Native Audio, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route Kling 3.0 video-generation integration work through APIDot documentation, including model selection, async task handling, polling, webhooks, and API-key handling. It is intended for guidance and documentation lookup, not for making live API calls by itself. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys, private prompts, media URLs, callback URLs, or generated video URLs could be exposed if copied into browser code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep APIDot API keys in server-side environment variables or a backend secret manager, and avoid logging private prompts, media URLs, callback URLs, API keys, or generated video URLs. <br>
Risk: APIDot model availability, supported request fields, limits, and commercial terms may change after this documentation-only skill is published. <br>
Mitigation: Verify current APIDot docs and model pages before preparing paid, production, or copyable API requests. <br>
Risk: Live API calls could spend credits or send private media to an external service when the user did not intend that behavior. <br>
Mitigation: Do not make live API calls unless the user explicitly asks and provides a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot Kling 3.0 Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Kling 3.0 Model Page](https://apidot.ai/models/kling-3-0) <br>
- [APIDot Kling 3.0 API Docs](https://apidot.ai/docs/kling-3-0) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with links, implementation notes, and optional code or configuration snippets when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no bundled scripts, API clients, network calls, or credential storage.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
