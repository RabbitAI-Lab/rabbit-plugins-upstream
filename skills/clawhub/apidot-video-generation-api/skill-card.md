## Description: <br>
Use APIDot for video generation API workflows, including text-to-video API, image-to-video API, reference image video, Veo 3.1 API, Seedance 2 API, Sora API, Kling API, async task submission, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route APIDot video generation questions to current docs, examples, async task submission, polling, and webhook integration patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys, prompts, media URLs, callback URLs, or generated result links could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in a server-side environment variable or secret manager, make live calls only from a safe backend environment, and avoid logging private prompts, media URLs, callback URLs, or API keys. <br>
Risk: APIDot model fields, availability, pricing, reliability, or endpoint behavior may change over time. <br>
Mitigation: Use the current APIDot docs and model pages for model-specific request fields and do not invent API facts, pricing, availability, reliability claims, refunds, or competitor comparisons. <br>
Risk: Async video workflows can lose task state or create duplicate visible results if polling and webhook handlers are not designed carefully. <br>
Mitigation: Persist task_id, selected model, user ID, source media references, and request status together, and make webhook handlers idempotent. <br>


## Reference(s): <br>
- [APIDot API Docs](https://apidot.ai/docs) <br>
- [APIDot Models](https://apidot.ai/models) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Veo 3.1 Docs](https://apidot.ai/docs/veo-3-1) <br>
- [APIDot Video Examples](https://github.com/APIDotAI/apidot-examples#video-models) <br>
- [APIDot Veo 3.1 Examples](https://github.com/APIDotAI/veo-3.1-api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with API workflow notes and example-oriented code or shell snippets when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no bundled executable behavior or stored credentials.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
