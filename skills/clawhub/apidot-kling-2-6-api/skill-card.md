## Description: <br>
Use APIDot for Kling 2.6 API workflows, including text-to-video API, image-to-video API, native audio video generation, prompt-driven clips, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route Kling 2.6 video-generation integration questions to APIDot docs, model pages, request-planning notes, async task guidance, polling, webhooks, and API-key handling guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY or private media URLs could be exposed through browser code, logs, screenshots, chat output, or public repositories. <br>
Mitigation: Keep API keys in server-side environment variables or a backend secret manager, and avoid logging API keys, private prompts, private media URLs, generated video URLs, or callback URLs. <br>
Risk: Outdated or guessed model fields, pricing, availability, or commercial terms could lead to incorrect API integrations. <br>
Mitigation: Use the current APIDot docs and model pages for model-specific request fields, availability, limits, pricing, and product details before making live API calls. <br>
Risk: Async video jobs can be mishandled if task identifiers, terminal status, or duplicate webhook deliveries are not managed correctly. <br>
Mitigation: Persist task_id with request status and final video URLs, store final URLs only after terminal success, and make webhook handlers idempotent. <br>


## Reference(s): <br>
- [Local APIDot Kling 2.6 reference](references/api.md) <br>
- [APIDot docs](https://apidot.ai/docs) <br>
- [APIDot Kling 2.6 docs](https://apidot.ai/docs/kling-2-6) <br>
- [APIDot Kling 2.6 model page](https://apidot.ai/models/kling-2-6) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown guidance with APIDot documentation links, request-planning notes, async workflow guidance, and API-key handling reminders] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; includes no executable code, bundled clients, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
