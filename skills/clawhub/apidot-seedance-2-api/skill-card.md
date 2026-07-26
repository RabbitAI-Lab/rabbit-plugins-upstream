## Description: <br>
Use APIDot for Seedance 2 API workflows, including seedance-2-fast, text-to-video API, image-to-video API, native audio video generation, reference image video, reference video, reference audio, async task submission, task_id handling, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan and implement APIDot Seedance 2 video generation workflows, including request-mode selection, async task submission, status polling, webhook integration, and safe optional payload submission from a server-side shell. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY exposure could grant access to live APIDot API usage. <br>
Mitigation: Keep the key in server-side environment variables or a backend secret manager, and avoid placing it in browser code, public repositories, logs, screenshots, chat output, payload files, or command history. <br>
Risk: Live Seedance 2 requests can submit unreviewed prompts or private media references to APIDot. <br>
Mitigation: Make live API calls only after explicit user approval from a trusted server-side environment, and review every JSON payload before submission. <br>
Risk: Outdated or guessed API fields can cause failed requests or misleading integration guidance. <br>
Mitigation: Use the current APIDot docs, model page, and examples for request fields, model availability, limits, and commercial terms. <br>


## Reference(s): <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Seedance 2 Model Page](https://apidot.ai/models/seedance-2) <br>
- [APIDot Seedance 2 API Docs](https://apidot.ai/docs/seedance-2) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [Seedance 2 API Examples](https://github.com/APIDotAI/seedance-2-api) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Seedance 2 Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/jiehao71727/skills/apidot-seedance-2-api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code, shell commands, configuration guidance, and API workflow notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference an optional user-invoked shell script that requires curl and a server-side APIDOT_API_KEY.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
