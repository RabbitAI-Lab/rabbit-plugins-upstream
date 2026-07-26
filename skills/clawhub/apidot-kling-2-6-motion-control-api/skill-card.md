## Description: <br>
Use APIDot for Kling 2.6 Motion Control API workflows, including motion transfer, reference video to character animation, image-to-video API, reference-to-video API, dance transfer, action transfer, controllable animation, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this documentation-only skill to route Kling 2.6 Motion Control integration work to APIDot model pages, API docs, async task patterns, polling guidance, and webhook guidance. It supports planning motion-transfer and controllable character animation workflows without making network requests or storing credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys, private prompts, media URLs, callback URLs, or generated video URLs could be exposed if copied into client-side code, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in server-side environment variables or a backend secret manager, and avoid logging private prompts, media URLs, callback URLs, generated video URLs, or API keys. <br>
Risk: Outdated or guessed APIDot request fields, model availability, limits, or commercial terms could lead to incorrect integration guidance. <br>
Mitigation: Verify current APIDot docs and model pages before making real calls, and do not infer unsupported request fields or product claims from other model families. <br>
Risk: Async task or webhook handling mistakes could lose task state or create duplicate visible results. <br>
Mitigation: Persist task_id, selected model, user ID, media references, request status, and final video URLs together; treat webhook handlers as idempotent and retry transient failures with backoff. <br>


## Reference(s): <br>
- [APIDot Kling 2.6 Motion Control Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [Kling 2.6 Motion Control Model Page](https://apidot.ai/models/kling-2-6-motion-control) <br>
- [Kling 2.6 Motion Control API Docs](https://apidot.ai/docs/kling-2-6-motion-control) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration] <br>
**Output Format:** [Markdown guidance with links and non-executable integration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, automatic network requests, or credential storage.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
