## Description: <br>
Use APIDot model catalog guidance to choose currently available APIDot image, video, chat, music, and 3D model pages, avoid offline model routes, prevent duplicate skill selection, and route users to the right APIDot docs and model-specific skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route APIDot model-selection and integration questions to the right APIDot model catalog page, category guidance, or model-specific skill. It helps avoid unsupported model routes and keeps API-key handling guidance visible. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDot keys in server-side environment variables or a backend secret manager, and avoid logging private prompts, media URLs, callbacks, user identifiers, or credentials. <br>
Risk: Model availability, pricing, performance, or commercial terms could be misstated if the agent relies on stale memory. <br>
Mitigation: Use the current APIDot model catalog and model pages before making availability or product-detail claims. <br>
Risk: Live APIDot API calls could be made from an unsuitable environment. <br>
Mitigation: Only make live calls when the user explicitly requests them and provides a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot API Docs](https://apidot.ai/docs) <br>
- [APIDot Model Catalog](https://apidot.ai/models) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [ClawHub Skill Page](https://clawhub.ai/jiehao71727/skills/apidot-model-catalog-api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with links, routing recommendations, and API-key handling notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable output or automatic network calls] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
