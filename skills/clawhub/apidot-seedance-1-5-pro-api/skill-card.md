## Description: <br>
Guides agents to APIDot Seedance 1.5 Pro documentation and integration patterns for text-to-video, image-to-video, async task handling, polling, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to plan APIDot Seedance 1.5 Pro video generation integrations, choose the right APIDot documentation path, and handle async task IDs, polling, and webhook delivery without embedding credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys or private prompts could be exposed if copied into browser code, logs, public repositories, screenshots, or chat output. <br>
Mitigation: Store APIDOT_API_KEY only in server-side environment variables or a backend secret manager, and avoid logging private prompts, media URLs, callback URLs, API keys, or generated video URLs. <br>
Risk: Model-specific request fields, availability, limits, or commercial terms may change outside the static skill artifact. <br>
Mitigation: Check the current APIDot Seedance 1.5 Pro docs and model page before preparing live requests or relying on product details. <br>
Risk: Live APIDot calls may submit user prompts or media to an external service. <br>
Mitigation: Make live calls only when the user explicitly asks and provides a safe server-side environment for secrets and private media references. <br>


## Reference(s): <br>
- [APIDot Documentation](https://apidot.ai/docs) <br>
- [APIDot Seedance 1.5 Pro Model Page](https://apidot.ai/models/seedance-1-5-pro) <br>
- [APIDot Seedance 1.5 Pro API Docs](https://apidot.ai/docs/seedance-1-5-pro) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [ClawHub Skill Page](https://clawhub.ai/jiehao71727/skills/apidot-seedance-1-5-pro-api) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with documentation links and integration planning notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only output; no executable files, bundled API clients, network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
