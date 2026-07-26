## Description: <br>
Use APIDot for Tripo H3.1 3D API workflows, including text-to-3D, image-to-3D, multiview-to-3D, async task submission, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to find APIDot Tripo H3.1 documentation, plan text-to-3D, image-to-3D, and multiview-to-3D request flows, and design async polling or webhook handling for generated 3D assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys or private asset workflow data could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in a server-side secret store and avoid logging API keys, private prompts, source image URLs, generated asset URLs, or callback URLs. <br>
Risk: Generated webhook, polling, or asset-storage code may mishandle async task state or duplicate callback delivery. <br>
Mitigation: Review generated integration code before use, persist task IDs and terminal status carefully, and make webhook handlers idempotent. <br>
Risk: Model request fields, limits, availability, or commercial terms may change outside the skill artifact. <br>
Mitigation: Use the current APIDot docs and model pages as the source of truth before preparing copyable request payloads or making product commitments. <br>


## Reference(s): <br>
- [APIDot Tripo H3.1 Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Tripo H3.1 3D Docs](https://apidot.ai/docs/tripo-h31-3d) <br>
- [APIDot Tripo H3.1 Model Page](https://apidot.ai/models/tripo-h31-3d) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with links and optional code or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; does not make network requests or store credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
