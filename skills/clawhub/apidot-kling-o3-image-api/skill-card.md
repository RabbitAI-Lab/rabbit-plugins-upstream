## Description: <br>
Use APIDot for Kling O3 Image API workflows, including text-to-image generation, image editing, reference-guided image generation, async task submission, polling, task status handling, webhook integration, and APIDot documentation routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route Kling O3 Image integration questions to APIDot documentation and to plan safe text-to-image, image editing, polling, and webhook workflows without bundled executable code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys, private prompts, image URLs, callback URLs, or generated outputs may be exposed if copied into browser code, public logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY server-side, use a backend secret manager or environment variable, and avoid logging private prompts, image URLs, callback URLs, API keys, and generated outputs. <br>
Risk: Model-specific request fields, limits, availability, or commercial terms may change outside this documentation-only skill. <br>
Mitigation: Use the live APIDot Kling O3 Image docs and model page as the source of truth before preparing payloads or making product commitments. <br>


## Reference(s): <br>
- [APIDot Kling O3 Image Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-kling-o3-image-api) <br>
- [APIDot documentation](https://apidot.ai/docs) <br>
- [Kling O3 Image model page](https://apidot.ai/models/kling-o3-image) <br>
- [Kling O3 Image API docs](https://apidot.ai/docs/kling-o3-image) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with documentation links and integration planning notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no scripts, bundled API clients, network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
