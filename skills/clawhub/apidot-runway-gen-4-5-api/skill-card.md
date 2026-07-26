## Description: <br>
Use APIDot for Runway Gen-4.5 API workflows, including Runway Gen-4.5, text-to-video API, image-to-video API, cinematic motion, physics-aware video generation, duration planning, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route Runway Gen-4.5 API integration questions to APIDot documentation, model pages, async task patterns, polling, webhook delivery, and implementation notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys, prompts, media URLs, callback URLs, or generated video URLs could be exposed if copied into frontend code, logs, screenshots, public repos, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY and private workflow data server-side, avoid logging sensitive values, and use backend secret management for real API calls. <br>
Risk: Runway Gen-4.5 request fields, availability, limits, or commercial terms could change over time. <br>
Mitigation: Use the current APIDot docs and model pages before preparing payloads or making commercial, performance, reliability, or availability claims. <br>
Risk: Async video jobs may be mishandled if task IDs, statuses, callback events, or final URLs are not persisted consistently. <br>
Mitigation: Persist task_id, selected model, user ID, source media references, request status, and final video URLs together; treat webhook handlers as idempotent. <br>


## Reference(s): <br>
- [APIDot Documentation](https://apidot.ai/docs) <br>
- [APIDot Runway Gen-4.5 Model Page](https://apidot.ai/models/runway-gen-4-5) <br>
- [APIDot Runway Gen-4.5 API Docs](https://apidot.ai/docs/runway-gen-4-5) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Runway Gen-4.5 Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown guidance with API integration notes and links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, bundled clients, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
