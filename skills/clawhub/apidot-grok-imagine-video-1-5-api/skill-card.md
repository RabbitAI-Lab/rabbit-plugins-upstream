## Description: <br>
Grok Imagine Video 1.5 API on APIDot for xAI image-to-video generation, reference image animation, prompt-guided motion, short video clips, duration planning, 480p 720p planning, async task submission, task_id handling, polling, webhooks, API key safety, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route Grok Imagine Video 1.5 integration questions to APIDot documentation, model pages, async task planning, polling, webhook, and API-key safety guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys, private prompts, media URLs, generated video URLs, or callback URLs could be exposed if copied into browser code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY server-side, use a backend secret manager or environment variable, and avoid logging private prompts, media URLs, generated video URLs, callback URLs, or credentials. <br>
Risk: Model request fields, pricing, limits, or availability may change outside this documentation-only skill. <br>
Mitigation: Verify current APIDot model pages and docs before making live requests or relying on commercial terms. <br>
Risk: Async video workflows can lose task state or duplicate results if polling, retries, or webhooks are handled inconsistently. <br>
Mitigation: Persist task_id, selected model, source references, request status, and final video URLs together; use idempotent webhook handlers and retry only transient failures with backoff. <br>


## Reference(s): <br>
- [APIDot documentation](https://apidot.ai/docs) <br>
- [Grok Imagine Video 1.5 model page](https://apidot.ai/models/grok-imagine-video-1-5) <br>
- [Grok Imagine Video 1.5 API docs](https://apidot.ai/docs/grok-imagine-video-1-5) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Grok Imagine Video 1.5 reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with links and non-executable integration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no scripts, network calls, bundled clients, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
