## Description: <br>
Kling 3.0 Motion Control API on APIDot routes agents to APIDot docs, model pages, and async integration guidance for motion transfer, controllable animation, polling, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this documentation-only skill to plan APIDot Kling 3.0 Motion Control integrations for motion transfer from a reference video onto a character image, including task submission, polling, webhook callbacks, and source-of-truth docs routing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A live integration may expose APIDOT_API_KEY if credentials are placed in browser code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY only in server-side environment variables or a backend secret manager, and avoid echoing secrets in generated guidance. <br>
Risk: Private prompts, media URLs, callback URLs, and generated video URLs may leak through application logging or support workflows. <br>
Mitigation: Avoid logging private media, callback URLs, generated outputs, and prompt metadata unless the application has an explicit redaction policy. <br>
Risk: APIDot model fields, availability, limits, pricing, or commercial terms may change after this documentation-only skill is published. <br>
Mitigation: Verify request fields and product terms against the current APIDot model page and API docs before sending live requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-kling-3-0-motion-control-api) <br>
- [APIDot docs](https://apidot.ai/docs) <br>
- [Kling 3.0 Motion Control model page](https://apidot.ai/models/kling-3-0-motion-control) <br>
- [Kling 3.0 Motion Control API docs](https://apidot.ai/docs/kling-3-0-motion-control) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Kling 3.0 Motion Control Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with API documentation links and integration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only output; no executable files, automatic network activity, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
