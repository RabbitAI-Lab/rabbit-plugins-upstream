## Description: <br>
Use APIDot for Flux Kontext API workflows, including Flux Kontext Pro, Flux Kontext Max, text-to-image API, context-aware image editing, character consistency, local edits, typography-aware visual updates, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this documentation-only skill to route APIDot Flux Kontext integration work to the right model pages, docs, async workflow guidance, and API-key handling practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys may be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Store APIDOT_API_KEY only in server-side environment variables or a backend secret manager, and avoid displaying or logging it. <br>
Risk: Private prompts, source image URLs, generated image URLs, task IDs, or callback URLs may reveal sensitive workflow details. <br>
Mitigation: Avoid logging private prompts and media URLs, persist only required job metadata, and treat webhook handlers as idempotent. <br>
Risk: Live APIDot calls use an external service and may submit prompts or image URLs outside the local environment. <br>
Mitigation: Make live API calls only when intended and from a safe server-side environment. <br>
Risk: Outdated or guessed model fields can cause invalid Flux Kontext requests. <br>
Mitigation: Use current APIDot docs and model pages for model-specific request fields, availability, limits, and commercial terms. <br>


## Reference(s): <br>
- [APIDot Flux Kontext Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Flux Kontext Docs](https://apidot.ai/docs/flux-kontext) <br>
- [APIDot Flux Kontext Model Page](https://apidot.ai/models/flux-kontext) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code or configuration snippets when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no bundled executable code, clients, or automatic network calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
