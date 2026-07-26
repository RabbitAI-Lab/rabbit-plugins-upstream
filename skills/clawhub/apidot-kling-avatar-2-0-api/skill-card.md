## Description: <br>
Use APIDot for Kling Avatar 2.0 API workflows, including talking avatar video, image-and-audio-to-video, Standard and Pro variants, avatar performance direction, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan APIDot Kling Avatar 2.0 integrations, including talking-avatar video request planning, model variant selection, async task handling, polling, and webhook delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY, input media, callback URLs, or generated videos could be exposed through client-side code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep API keys server-side, restrict access to private media and generated videos, and avoid logging secrets, private URLs, callback URLs, prompts, or generated outputs. <br>
Risk: Outdated or guessed request fields, media limits, model availability, or commercial terms could lead to incorrect integration guidance. <br>
Mitigation: Verify exact request shapes, supported media, limits, model variants, and terms in APIDot's live documentation before making real API calls. <br>
Risk: Async task handling can lose task state or process duplicate webhook deliveries incorrectly. <br>
Mitigation: Persist task_id, model choice, media references, request status, and final video URLs together, and implement webhook handlers idempotently with retry-safe behavior. <br>


## Reference(s): <br>
- [APIDot Kling Avatar 2.0 API Docs](https://apidot.ai/docs/kling-avatar-2-0) <br>
- [APIDot Kling Avatar 2.0 Model Page](https://apidot.ai/models/kling-avatar-2-0) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Kling Avatar 2.0 Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with API planning notes and optional code or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no automatic API calls or executable behavior.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
