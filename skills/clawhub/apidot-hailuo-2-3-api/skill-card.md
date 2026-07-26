## Description: <br>
Use APIDot for Hailuo 2.3 API workflows, including MiniMax Hailuo 2.3, text-to-video API, image-to-video API, start image guidance, prompt optimization, duration and resolution planning, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route Hailuo 2.3 video-generation integration work to APIDot documentation, model pages, reference notes, and async task patterns. It supports planning text-to-video, image-to-video, polling, webhook, credential-handling, and request-shape decisions without bundling executable code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys may be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Store APIDOT_API_KEY only in server-side environment variables or a backend secret manager, and avoid emitting credentials in generated guidance. <br>
Risk: Outdated or guessed APIDot model fields, availability, pricing, or limits could lead to incorrect Hailuo 2.3 integrations. <br>
Mitigation: Use current APIDot docs and model pages for model-specific request fields, commercial terms, availability, and supported options. <br>
Risk: Webhook retries or repeated callbacks could create duplicate visible results in production workflows. <br>
Mitigation: Treat webhook handlers as idempotent and persist task_id, selected model, request status, source media references, and final video URLs together. <br>


## Reference(s): <br>
- [APIDot Hailuo 2.3 Reference](references/api.md) <br>
- [APIDot docs](https://apidot.ai/docs) <br>
- [APIDot Hailuo 2.3 model page](https://apidot.ai/models/hailuo-2-3) <br>
- [APIDot Hailuo 2.3 API docs](https://apidot.ai/docs/hailuo-2-3) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-hailuo-2-3-api) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown guidance with links, implementation notes, and optional code or configuration suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; no bundled scripts, automatic network calls, stored credentials, or executable clients.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
