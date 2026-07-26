## Description: <br>
Use APIDot for Grok Imagine API workflows, including image generation, image editing, text-to-video, image-to-video, async task handling, polling, webhooks, and APIDot documentation routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to route Grok Imagine integration questions to APIDot documentation and plan async image or video workflows with API key handling, task polling, and webhook delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY exposure could occur if credentials are placed in browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep the key in server-side environment variables or a backend secret manager and avoid echoing it in prompts, generated code, logs, or UI output. <br>
Risk: Model fields, availability, limits, or commercial terms may change outside this documentation-only skill. <br>
Mitigation: Use the live APIDot docs and model pages as the source of truth before preparing payloads or making production calls. <br>
Risk: Private prompts, media URLs, generated result URLs, or callback URLs could leak through logs or workflow records. <br>
Mitigation: Avoid logging private prompts, private media URLs, generated media URLs, callback URLs, and related request metadata unless the user has approved an appropriate secure storage plan. <br>
Risk: Live API calls can affect external services and may create cost, privacy, or operational impact. <br>
Mitigation: Make live APIDot calls only when the user explicitly asks and provides a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot Grok Imagine Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Grok Imagine Model Page](https://apidot.ai/models/grok-imagine) <br>
- [APIDot Grok Imagine Docs](https://apidot.ai/docs/grok-imagine) <br>
- [APIDot Grok Imagine Video 1.5 Docs](https://apidot.ai/docs/grok-imagine-video-1-5) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration] <br>
**Output Format:** [Markdown guidance with documentation links and integration planning notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only output; no executable files, bundled clients, stored credentials, or automatic network calls.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
