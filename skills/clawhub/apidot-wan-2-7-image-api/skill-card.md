## Description: <br>
Routes Wan 2.7 Image API questions to APIDot documentation, model pages, reference notes, and async integration guidance for text-to-image, image editing, image-to-image, multi-reference generation, polling, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to plan Wan 2.7 Image integrations on APIDot, choose the right APIDot docs or model page, and follow safe async job patterns for polling and webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys, prompts, private image URLs, callback URLs, or generated URLs may be exposed if users later implement real APIDot calls in unsafe environments or logs. <br>
Mitigation: Keep APIDOT_API_KEY server-side or in a secret manager, avoid browser bundles and public logs, and avoid logging private prompts, image URLs, callback URLs, generated URLs, or API keys. <br>
Risk: Wan 2.7 Image request fields, limits, availability, and commercial terms may change over time. <br>
Mitigation: Use the live APIDot docs and model pages as the source of truth before preparing copyable request payloads or making product claims. <br>
Risk: Webhook retries or duplicate callbacks can create duplicate visible results in production workflows. <br>
Mitigation: Persist task IDs and request state, and make webhook handlers idempotent before exposing results to users. <br>


## Reference(s): <br>
- [APIDot Wan 2.7 Image Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-wan-2-7-image-api) <br>
- [APIDot docs](https://apidot.ai/docs) <br>
- [APIDot Wan 2.7 Image model page](https://apidot.ai/models/wan-2-7-image) <br>
- [APIDot Wan 2.7 Image docs](https://apidot.ai/docs/wan-2-7-image) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with links and integration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, automatic network calls, bundled API clients, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
