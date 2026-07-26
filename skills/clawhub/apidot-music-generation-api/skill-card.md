## Description: <br>
Use APIDot for music generation API workflows, including text-to-music API, song generation API, Generate Music API, MiniMax Music 2.6 API, async task submission, task_id handling, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route APIDot music-generation questions to the relevant APIDot docs, examples, and async integration patterns for task submission, polling, and webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY is required for real API calls and could be exposed if placed in browser code, logs, public repositories, screenshots, or chat output. <br>
Mitigation: Store APIDOT_API_KEY only in server-side environment variables or a backend secret manager, and avoid echoing credentials in generated examples. <br>
Risk: APIDot model fields, pricing, terms, and availability may change outside the skill artifact. <br>
Mitigation: Verify current APIDot docs, pricing, terms, and data-handling expectations before building or operating live integrations. <br>
Risk: Prompts, generated audio URLs, callback URLs, or related metadata may contain sensitive user or workflow data. <br>
Mitigation: Avoid logging private prompts, generated audio URLs, callback URLs, and API keys; review APIDot data-handling expectations before sending prompts or audio through the service. <br>


## Reference(s): <br>
- [APIDot API Docs](https://apidot.ai/docs) <br>
- [APIDot Music Models](https://apidot.ai/models/music) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [Generate Music Docs](https://apidot.ai/docs/generate-music) <br>
- [MiniMax Music 2.6 Docs](https://apidot.ai/docs/minimax-music-2-6) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown guidance with optional code snippets and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no bundled scripts, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
