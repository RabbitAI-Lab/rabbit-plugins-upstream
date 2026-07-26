## Description: <br>
Use APIDot for 3D generation API workflows, including text-to-3D, image-to-3D, multi-image-to-3D, Meshy 6, Tripo H3.1, Tripo P1, task handling, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route APIDot 3D generation questions to the right docs, examples, and async integration patterns for text-to-3D, image-to-3D, multi-image-to-3D, polling, and webhook workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys, private prompts, private source image URLs, generated asset URLs, or callback URLs could be exposed if copied into browser code, public logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in server-side secrets, avoid logging sensitive prompts or URLs, and do not place credentials in frontend bundles or public artifacts. <br>
Risk: Live APIDot API calls may create unintended external requests or operational side effects if made during exploratory guidance. <br>
Mitigation: Make live calls only when the user explicitly asks and provides a safe server-side environment configured for APIDot integration work. <br>
Risk: Model-specific fields, availability, or examples may change over time, causing incorrect 3D generation requests if stale details are reused. <br>
Mitigation: Use the current APIDot docs, model pages, and official examples for request fields, polling, webhook behavior, and model-specific implementation details. <br>


## Reference(s): <br>
- [APIDot API Docs](https://apidot.ai/docs) <br>
- [APIDot 3D Models](https://apidot.ai/models/3d) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [Meshy 6 3D Docs](https://apidot.ai/docs/meshy-6-3d) <br>
- [Tripo H3.1 3D Docs](https://apidot.ai/docs/tripo-h31-3d) <br>
- [Tripo P1 3D Docs](https://apidot.ai/docs/tripo-p1-3d) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with links and optional code, shell, or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no executable files, bundled API clients, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
