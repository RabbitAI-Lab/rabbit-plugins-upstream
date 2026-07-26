## Description: <br>
Kling 2.5 Turbo Pro API on APIDot provides documentation routing and integration guidance for text-to-video, image-to-video, async task handling, polling, webhooks, and API key safety. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to find the right APIDot Kling 2.5 Turbo Pro documentation and plan integrations for prompt-only, start-frame, or start-and-end-frame video generation workflows. It is most useful for request planning, async task status handling, webhook delivery, and safe API key handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys could be exposed if copied into browser code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in server-side environment variables or a backend secret manager, and avoid logging prompts, media URLs, generated video URLs, callback URLs, or credentials. <br>
Risk: Model fields, availability, limits, or commercial terms may change outside the static skill text. <br>
Mitigation: Verify current APIDot docs and model pages before making real API calls or relying on model-specific request fields. <br>
Risk: Live API calls can use credentials, submit private media, or incur costs if run from an unsafe environment. <br>
Mitigation: Treat this skill as API documentation guidance and make live calls only when the user explicitly asks and provides a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot Documentation](https://apidot.ai/docs) <br>
- [APIDot Kling 2.5 Turbo Pro Model Page](https://apidot.ai/models/kling-2-5-turbo-pro) <br>
- [APIDot Kling 2.5 Turbo Pro API Docs](https://apidot.ai/docs/kling-2-5-turbo-pro) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Kling 2.5 Turbo Pro Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions] <br>
**Output Format:** [Markdown guidance with reference links and integration planning notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no bundled executable files or automatic network calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
