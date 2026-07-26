## Description: <br>
Use APIDot for FLUX.2 API workflows, including Flux 2 API, image generation API, image editing API, multi-reference editing, text-to-image, reference image generation, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route FLUX.2 APIDot integration questions to the right model pages, API docs, async task guidance, and webhook notes. It supports planning image generation, editing, reference-guided workflows, polling, and production callback handling without embedding executable clients or credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys or private prompts could be exposed if copied into browser code, logs, public repositories, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY server-side in environment variables or a secret manager, and avoid logging API keys, private prompts, private image URLs, generated image URLs, or callback URLs. <br>
Risk: Guessed or stale FLUX.2 request fields can produce invalid payloads or misleading integration guidance. <br>
Mitigation: Use the current APIDot FLUX.2 docs and model page as the source of truth before preparing copyable request shapes or model-specific fields. <br>
Risk: Unintended live API calls may send private data or consume paid API resources. <br>
Mitigation: Make live APIDot calls only after an explicit user request and only from a safe server-side environment with appropriate credentials. <br>


## Reference(s): <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot FLUX.2 Model Page](https://apidot.ai/models/flux-2) <br>
- [APIDot FLUX.2 API Docs](https://apidot.ai/docs/flux-2) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot FLUX.2 Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown guidance with API integration notes and optional code or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; live API calls require explicit user request and a safe server-side APIDOT_API_KEY environment.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
