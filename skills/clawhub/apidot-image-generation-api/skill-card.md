## Description: <br>
Use APIDot for image generation API and image editing API workflows, including text-to-image API, image-to-image API, GPT Image 2 API, Nano Banana API, Nano Banana Pro API, Seedream API, Flux API, async task submission, polling, task status, and webhook integration based on APIDot docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this documentation-only skill to plan APIDot image generation and image editing integrations, route users to current APIDot docs and examples, and design async polling or webhook workflows without exposing API keys. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys could be exposed if copied into browser code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in server-side secrets only and avoid logging keys, private prompts, private image URLs, or callback URLs. <br>
Risk: Live API calls may send prompts or image URLs to APIDot and may incur provider costs. <br>
Mitigation: Make live calls only after explicit user approval in a safe server-side environment, and review APIDot terms, pricing, and data handling before production use. <br>
Risk: Model availability and request fields can change over time. <br>
Mitigation: Use current APIDot docs and model pages for model-specific fields instead of copying fields across model families. <br>
Risk: Polling or webhook workflows can produce duplicate or inconsistent visible results if callbacks are retried. <br>
Mitigation: Persist task IDs and statuses, store final image URLs only after terminal success, and make webhook handlers idempotent. <br>


## Reference(s): <br>
- [APIDot API docs](https://apidot.ai/docs) <br>
- [APIDot image models](https://apidot.ai/models/image) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot webhooks](https://apidot.ai/docs/webhooks) <br>
- [GPT Image 2 docs](https://apidot.ai/docs/gpt-image-2) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with links and optional code or configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; live API calls require explicit user request and a server-side APIDOT_API_KEY.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
