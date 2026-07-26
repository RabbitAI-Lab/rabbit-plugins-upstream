## Description: <br>
Use APIDot for Hunyuan 3D 3.1 API workflows, including Hunyuan 3D Pro and Rapid variants, text-to-3D API, image-to-3D API, multi-view guidance, PBR output planning, geometry controls, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan APIDot Hunyuan 3D 3.1 integrations for text-to-3D, image-to-3D, async task handling, polling, webhook delivery, and asset workflow decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys, private prompts, image URLs, callback URLs, or generated asset URLs could be exposed if copied into client code, logs, repositories, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY and sensitive request data in a server-side environment or secret manager, and avoid logging or displaying these values. <br>
Risk: Unsupported fields or stale model assumptions could produce invalid Hunyuan 3D 3.1 requests. <br>
Mitigation: Use the live APIDot Hunyuan 3D 3.1 docs before preparing requests, and do not copy controls across Pro, Rapid, text-to-3D, or image-to-3D variants unless documented. <br>
Risk: Webhook retries or duplicate deliveries could create duplicate visible assets in production pipelines. <br>
Mitigation: Persist task_id and related request state, and make webhook handlers idempotent. <br>


## Reference(s): <br>
- [APIDot Hunyuan 3D 3.1 Reference](references/api.md) <br>
- [Hunyuan 3D 3.1 model page](https://apidot.ai/models/hunyuan-3d-3-1) <br>
- [Hunyuan 3D 3.1 API docs](https://apidot.ai/docs/hunyuan-3d-3-1) <br>
- [APIDot 3D models](https://apidot.ai/models/3d) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions] <br>
**Output Format:** [Markdown guidance with API integration notes and optional code or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; it does not execute API calls or store credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
