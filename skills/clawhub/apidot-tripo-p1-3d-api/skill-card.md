## Description: <br>
Use APIDot for Tripo P1 3D API workflows, including Tripo P1 API, text-to-3D API, image-to-3D API, 3D asset generation, async task submission, task_id handling, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan APIDot Tripo P1 3D integrations for text-to-3D, image-to-3D, async task polling, webhook callbacks, and 3D asset handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys, private prompts, source image URLs, callback URLs, or generated asset URLs could be exposed if copied into client code or logs. <br>
Mitigation: Keep APIDOT_API_KEY in a server-side secret store and avoid logging private prompts, media URLs, callback URLs, generated asset URLs, or credentials. <br>
Risk: APIDot model fields, availability, limits, or commercial terms may change outside this documentation-only release. <br>
Mitigation: Verify current APIDot docs and model pages before making real requests or relying on production behavior. <br>
Risk: Incorrect retry or webhook handling can duplicate generated assets or lose task state. <br>
Mitigation: Persist task_id and related request state, use idempotent webhook handlers, and retry only transient failures with backoff. <br>


## Reference(s): <br>
- [APIDot Tripo P1 Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Tripo P1 3D Docs](https://apidot.ai/docs/tripo-p1-3d) <br>
- [APIDot Tripo P1 Model Page](https://apidot.ai/models/tripo-p1-3d) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions] <br>
**Output Format:** [Markdown guidance with optional code and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no bundled executable code or automatic network calls.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
