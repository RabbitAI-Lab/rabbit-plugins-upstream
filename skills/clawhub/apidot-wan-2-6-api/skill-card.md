## Description: <br>
Use APIDot for Wan 2.6 API workflows, including Wan 2.6 text-to-video API, image-to-video API, video-to-video API, multi-shot video, 720p and 1080p planning, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this documentation-only skill to route APIDot Wan 2.6 integration questions to the right docs, model pages, async task pattern, polling guidance, and webhook planning notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys, private prompts, media URLs, callback URLs, or generated video URLs could be exposed during live integration work. <br>
Mitigation: Keep APIDOT_API_KEY in a backend secret store or server environment and avoid logging private prompts, media URLs, callback URLs, API keys, or generated video URLs. <br>
Risk: Wan 2.6 request fields, limits, availability, or commercial terms may change outside the static skill artifact. <br>
Mitigation: Verify current APIDot docs and model pages before coding payloads, selecting request modes, or making product claims. <br>
Risk: Async video jobs can be mishandled if task IDs, terminal states, retries, or duplicate webhook deliveries are not tracked correctly. <br>
Mitigation: Persist task_id, selected model, source media references, request status, and final URLs together; use backoff for transient failures and idempotent webhook handlers. <br>


## Reference(s): <br>
- [APIDot Wan 2.6 Reference](references/api.md) <br>
- [APIDot Documentation](https://apidot.ai/docs) <br>
- [Wan 2.6 API Documentation](https://apidot.ai/docs/wan-2-6) <br>
- [Wan 2.6 Model Page](https://apidot.ai/models/wan-2-6) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown guidance with documentation links and integration planning notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, bundled clients, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
