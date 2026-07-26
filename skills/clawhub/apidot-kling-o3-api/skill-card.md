## Description: <br>
Routes agents to APIDot Kling O3 documentation and integration guidance for text-to-video, image-to-video, async task handling, polling, and webhook workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to find APIDot Kling O3 docs and plan Kling O3 video API integrations, including task submission, status polling, webhook delivery, and safe API key handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys could be exposed if copied into browser code, public repos, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in a backend secret store or server-side environment variable and avoid printing it in outputs. <br>
Risk: APIDot model fields, limits, availability, or commercial terms may change over time. <br>
Mitigation: Review the current APIDot docs and model page before preparing or sending requests. <br>
Risk: Private prompts, media URLs, callback URLs, or generated video URLs may contain sensitive workflow data. <br>
Mitigation: Avoid logging these values and persist only the task metadata needed for status tracking and delivery. <br>
Risk: Live API calls can send user data to APIDot unintentionally. <br>
Mitigation: Make live calls only after the user explicitly asks and provides a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot Kling O3 Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [Kling O3 Docs](https://apidot.ai/docs/kling-o3) <br>
- [Kling O3 Model Page](https://apidot.ai/models/kling-o3) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration guidance, Implementation guidance] <br>
**Output Format:** [Markdown guidance with links and optional configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; live API calls require explicit user request and a safe server-side APIDOT_API_KEY environment.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
