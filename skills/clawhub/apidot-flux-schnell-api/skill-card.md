## Description: <br>
Use APIDot for Flux Schnell API workflows, including FLUX.1 Schnell, Black Forest Labs image generation, fast low-cost text-to-image drafts, prompt exploration, batch creative iteration, task_id, polling, webhooks, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route Flux Schnell integration work to APIDot's current docs, model page, and async workflow guidance for fast text-to-image draft generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY can be exposed if placed in frontend code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep the API key in server-side environment variables or a backend secret manager and avoid echoing it in generated guidance. <br>
Risk: Prompts, generated image URLs, callback URLs, task IDs, and customer data may contain sensitive information. <br>
Mitigation: Treat these values as sensitive by default and avoid logging or sharing them unless the user explicitly says they can be shared. <br>
Risk: Live APIDot calls could spend credits or process user data unintentionally. <br>
Mitigation: Only make live calls when the user explicitly asks and provides a safe server-side environment. <br>
Risk: Model-specific fields, limits, pricing, availability, and commercial terms may change. <br>
Mitigation: Use current APIDot docs and model pages for request fields, limits, availability, and commercial details instead of relying on copied examples. <br>


## Reference(s): <br>
- [APIDot Flux Schnell Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [Flux Schnell Model Page](https://apidot.ai/models/flux-schnell) <br>
- [Flux Schnell API Docs](https://apidot.ai/docs/flux-schnell) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with links, workflow notes, and security reminders] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable code, bundled API client, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
