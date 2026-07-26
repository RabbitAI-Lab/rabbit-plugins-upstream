## Description: <br>
Use APIDot for Seedance 2.0 Mini API workflows, including short video generation, prompt-only and media-guided jobs, task polling, webhooks, and docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to answer APIDot Seedance 2.0 Mini integration questions, choose the right documentation path, and plan async video-generation flows without embedding live API calls in the skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An APIDot API key could be exposed if it is placed in client code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY server-side in environment variables or a backend secret manager, and avoid printing or storing it in user-visible channels. <br>
Risk: Prompts, source media URLs, generated video URLs, callback URLs, customer data, and task IDs may contain sensitive workflow information. <br>
Mitigation: Treat these values as sensitive by default, avoid logging them, and share them only when the user explicitly permits disclosure. <br>
Risk: APIDot pricing, model availability, supported fields, and request limits may change after the skill release. <br>
Mitigation: Verify current APIDot docs, pricing, and model pages before making live calls or committing integration behavior. <br>


## Reference(s): <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Seedance 2.0 Mini Model Page](https://apidot.ai/models/seedance-2-mini) <br>
- [Seedance 2.0 Mini API Docs](https://apidot.ai/docs/seedance-2-mini) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [ClawHub Skill Page](https://clawhub.ai/jiehao71727/skills/apidot-seedance-2-mini-api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration instructions] <br>
**Output Format:** [Markdown text with documentation links and integration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable code, stored credentials, or automatic network calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
