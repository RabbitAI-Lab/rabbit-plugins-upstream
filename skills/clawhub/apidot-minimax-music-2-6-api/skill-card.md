## Description: <br>
Use APIDot for MiniMax Music 2.6 API workflows, including AI music generation, lyrics, instrumentals, audio export planning, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan APIDot MiniMax Music 2.6 integrations, including request-mode selection, async task handling, polling, webhook delivery, and safe API-key handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY could be exposed if used in browser code, logs, screenshots, chat output, or public repositories. <br>
Mitigation: Keep APIDOT_API_KEY in a backend secret store or server-side environment variable and avoid logging secrets. <br>
Risk: Private prompts, callback URLs, or generated audio URLs could be disclosed through logs or chat output. <br>
Mitigation: Avoid logging prompts, callback URLs, and generated audio URLs; store final audio URLs only after successful terminal task status. <br>
Risk: APIDot pricing, request fields, limits, model availability, or commercial terms may change. <br>
Mitigation: Verify current APIDot pricing, fields, and model availability in the official APIDot docs before real API use. <br>


## Reference(s): <br>
- [APIDot MiniMax Music 2.6 Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [MiniMax Music 2.6 Model Page](https://apidot.ai/models/minimax-music-2-6) <br>
- [MiniMax Music 2.6 API Docs](https://apidot.ai/docs/minimax-music-2-6) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown guidance with optional code and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; produces integration guidance and routing to current APIDot sources.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
