## Description: <br>
Use APIDot for Sora 2 Official API workflows, including OpenAI Sora API, sora-2-official, sora-2-pro-official, text-to-video API, image-to-video API, prompt-to-video generation, async task submission, task_id handling, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this documentation-only skill to route APIDot Sora 2 Official questions to current model docs, examples, request-planning notes, polling guidance, and webhook integration guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An APIDot API key could be exposed if placed in browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY only in server-side environment variables or a backend secret manager, and avoid logging secrets. <br>
Risk: Model-specific request fields, limits, availability, or commercial terms could become outdated. <br>
Mitigation: Verify current APIDot docs and model pages before preparing request payloads or making claims about product behavior. <br>
Risk: Prompts, private media URLs, callback URLs, or generated video URLs may contain sensitive user data. <br>
Mitigation: Avoid logging private prompts, media URLs, callback URLs, generated video URLs, or other sensitive workflow data. <br>
Risk: Live API calls may incur cost or send user data to APIDot without an intended server-side environment. <br>
Mitigation: Treat the skill as a reference guide and make live API calls only when the user explicitly asks and provides a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot Sora 2 Official Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Sora 2 Official Docs](https://apidot.ai/docs/sora-2-official) <br>
- [APIDot Sora 2 Official Model Page](https://apidot.ai/models/sora-2-official) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Sora 2 Official Examples](https://github.com/APIDotAI/sora-2-official-api) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with documentation links, routing notes, and integration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, bundled clients, stored credentials, or automatic API calls.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
