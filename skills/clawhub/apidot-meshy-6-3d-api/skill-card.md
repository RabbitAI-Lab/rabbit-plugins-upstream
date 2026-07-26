## Description: <br>
Use APIDot for Meshy 6 3D API workflows, including Meshy 6 API, text-to-3D API, image-to-3D API, multi-image-to-3D API, 3D asset generation, async task submission, task_id handling, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route APIDot Meshy 6 3D integration questions to the right docs, examples, reference notes, and async task patterns. It supports text-to-3D, image-to-3D, multi-image-to-3D, task polling, task_id handling, and webhook planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep the key in server-side environment variables or a backend secret manager and avoid logging private prompts, source media URLs, generated asset URLs, callback URLs, or credentials. <br>
Risk: APIDot request fields, pricing, limits, model availability, and commercial terms may change outside this documentation-only skill. <br>
Mitigation: Review the live APIDot docs and model pages before preparing payloads or relying on current product details. <br>
Risk: Async 3D generation workflows can lose track of jobs or duplicate visible assets if task IDs and callbacks are handled inconsistently. <br>
Mitigation: Persist task_id, selected model, user ID, source media references, request status, and final asset URLs together, and make webhook handlers idempotent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-meshy-6-3d-api) <br>
- [APIDot docs](https://apidot.ai/docs) <br>
- [APIDot Meshy 6 model page](https://apidot.ai/models/meshy-6-3d) <br>
- [APIDot Meshy 6 API docs](https://apidot.ai/docs/meshy-6-3d) <br>
- [APIDot webhooks docs](https://apidot.ai/docs/webhooks) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Meshy 6 Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, code] <br>
**Output Format:** [Markdown guidance with links, integration notes, and optional code or configuration snippets when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, bundled clients, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
