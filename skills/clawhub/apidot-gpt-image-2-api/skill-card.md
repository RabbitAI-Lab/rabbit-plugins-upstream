## Description: <br>
Use APIDot for GPT Image 2 API workflows, including text-to-image API, image editing API, image-to-image API, reference image generation, async task submission, task_id handling, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan APIDot GPT Image 2 integrations, route to the current APIDot docs and examples, and handle async image generation or editing workflows safely. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys or private image workflow data could be exposed if copied into frontend code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in server-side environment variables or a backend secret manager, and avoid logging API keys, private prompts, private image URLs, generated image URLs, or callback URLs. <br>
Risk: Outdated or guessed GPT Image 2 payload fields could produce incorrect integration guidance. <br>
Mitigation: Use the current APIDot model page, docs, and examples before preparing copyable request payloads or making real API calls. <br>
Risk: Async image generation jobs can be mishandled if task identifiers, retries, or webhooks are not persisted consistently. <br>
Mitigation: Persist task_id, selected model, user ID, source media references, request status, and final image URLs together, and treat webhook handlers as idempotent. <br>


## Reference(s): <br>
- [APIDot GPT Image 2 Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot GPT Image 2 Docs](https://apidot.ai/docs/gpt-image-2) <br>
- [APIDot GPT Image 2 Model Page](https://apidot.ai/models/gpt-image-2) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot GPT Image 2 Examples](https://github.com/APIDotAI/gpt-image-2-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional code, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; the skill itself does not run commands, make network requests, or store credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
