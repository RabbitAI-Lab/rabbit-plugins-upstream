## Description: <br>
Use APIDot as one API surface for image generation, video generation, chat, music, and 3D generation workflows, with guidance for API key safety, polling, webhooks, task status, and official APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to plan APIDot integrations for image, video, chat, music, and 3D generation workflows while following APIDot documentation and API key safety practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Store APIDOT_API_KEY only in server-side environment variables or a backend secret manager. <br>
Risk: Model availability, pricing, request fields, or endpoint behavior may change over time. <br>
Mitigation: Verify current APIDot product details in the official docs, model pages, and examples before implementation. <br>
Risk: Generated integration code may make real APIDot API calls or mishandle asynchronous task status and webhooks. <br>
Mitigation: Review generated code before running it, persist task IDs, handle webhook retries idempotently, and avoid retrying invalid payloads unchanged. <br>


## Reference(s): <br>
- [APIDot API docs](https://apidot.ai/docs) <br>
- [APIDot models](https://apidot.ai/models) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot API key dashboard](https://apidot.ai/dashboard/api-key) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with links and optional code or shell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No bundled executable output; generated integration details should be checked against current APIDot docs.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
