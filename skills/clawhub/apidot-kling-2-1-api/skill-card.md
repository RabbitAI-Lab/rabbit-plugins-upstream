## Description: <br>
Use APIDot for Kling 2.1 API workflows, including Kling 2.1 Standard, Kling 2.1 Pro, image-to-video API, start-frame guidance, optional end-frame control, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan APIDot Kling 2.1 image-to-video integrations, route questions to current APIDot documentation, and handle async task submission, polling, and webhook workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys, private prompts, media URLs, callback URLs, or generated video URLs could be exposed during integration work. <br>
Mitigation: Keep APIDOT_API_KEY in a server-side secret store, avoid browser bundles and logs for secrets or private media, and review generated guidance before use. <br>
Risk: APIDot model fields, limits, pricing, and availability may change outside the documentation packaged with this skill. <br>
Mitigation: Verify current request fields, limits, pricing, and commercial terms in the live APIDot docs and model pages before making real API calls. <br>
Risk: Async video generation workflows can duplicate visible results if polling, retries, or webhook callbacks are handled incorrectly. <br>
Mitigation: Persist task_id and status with the user workflow, use idempotent webhook handlers, and retry only transient failures with backoff. <br>


## Reference(s): <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Kling 2.1 Model Page](https://apidot.ai/models/kling-2-1) <br>
- [APIDot Kling 2.1 API Docs](https://apidot.ai/docs/kling-2-1) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Kling 2.1 Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration instructions] <br>
**Output Format:** [Markdown guidance with links and implementation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only output; no executable code, network calls, install automation, or credential storage.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
