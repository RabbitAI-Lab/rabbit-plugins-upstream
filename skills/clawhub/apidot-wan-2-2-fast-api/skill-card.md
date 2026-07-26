## Description: <br>
Routes agents to APIDot Wan 2.2 Fast documentation and integration guidance for text-to-video and image-to-video draft workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to find the correct APIDot Wan 2.2 Fast docs, plan async video generation jobs, handle task polling or webhooks, and keep API keys server-side. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys could be exposed if copied into browser code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in server-side environment variables or a backend secret store and avoid logging or displaying it. <br>
Risk: Private prompts, media URLs, callback URLs, or generated video URLs may be sensitive when submitted to or returned from video generation workflows. <br>
Mitigation: Submit only content appropriate for the project and avoid logging private prompts, media URLs, generated video URLs, or callback URLs. <br>
Risk: Wan 2.2 Fast request fields, limits, availability, and commercial terms may change over time. <br>
Mitigation: Check the current APIDot model page and API docs before making live calls or copying request shapes. <br>


## Reference(s): <br>
- [APIDot Documentation](https://apidot.ai/docs) <br>
- [APIDot Wan 2.2 Fast Model Page](https://apidot.ai/models/wan-2-2-fast) <br>
- [APIDot Wan 2.2 Fast API Docs](https://apidot.ai/docs/wan-2-2-fast) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Wan 2.2 Fast Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with links, API planning notes, and implementation patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; produces guidance and does not execute API calls or store credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
