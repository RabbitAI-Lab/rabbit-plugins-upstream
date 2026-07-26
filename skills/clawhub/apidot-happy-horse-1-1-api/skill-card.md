## Description: <br>
Provides documentation-only guidance for APIDot Happy Horse 1.1 video-generation workflows, including request planning, async task handling, polling, and webhook integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external builders use this skill to plan Happy Horse 1.1 integrations through APIDot, including text-to-video, image-to-video, reference-to-video, status polling, and webhook delivery. It helps route users to current APIDot documentation without making network requests or storing credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Provide APIDOT_API_KEY only through a server-side secret or environment variable and avoid echoing credentials in generated guidance. <br>
Risk: External APIDot request fields, limits, availability, or commercial terms may change after this release. <br>
Mitigation: Verify the current APIDot Happy Horse 1.1 docs and model page before making requests or giving copyable payloads. <br>
Risk: Private prompts, media URLs, callback URLs, and generated outputs may leak through logs or overly broad persistence. <br>
Mitigation: Keep logs minimal, avoid storing sensitive request data unless needed, and treat webhook handlers and stored task records as sensitive backend data. <br>
Risk: Live API calls from an unsafe environment could disclose credentials or user media. <br>
Mitigation: Make live APIDot calls only when the user explicitly asks and provides a safe server-side execution environment. <br>


## Reference(s): <br>
- [Local APIDot Happy Horse 1.1 Reference](references/api.md) <br>
- [APIDot Happy Horse 1.1 Docs](https://apidot.ai/docs/happy-horse-1-1) <br>
- [APIDot Happy Horse 1.1 Model Page](https://apidot.ai/models/happy-horse-1-1) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [ClawHub Skill Page](https://clawhub.ai/jiehao71727/skills/apidot-happy-horse-1-1-api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with links and non-executable integration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable code, automatic API calls, bundled clients, or credential storage.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
