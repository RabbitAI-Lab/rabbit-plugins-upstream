## Description: <br>
Use APIDot for Flux Dev API workflows, including FLUX.1 Dev, Black Forest Labs image generation, text-to-image, single-reference image-to-image, prompt adherence, realistic detail, task_id, polling, webhooks, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to route FLUX.1 Dev image-generation questions to APIDot documentation, plan text-to-image or single-reference image-to-image workflows, and handle async polling or webhook delivery safely. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys could be exposed if copied into client code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in server-side environment variables or a backend secret manager, and avoid logging or displaying it. <br>
Risk: Prompts, source image URLs, generated image URLs, callback URLs, customer data, and task IDs may contain sensitive workflow data. <br>
Mitigation: Treat those values as sensitive, share them only when the user explicitly permits it, and make live API calls only when intentionally requested in a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot Flux Dev Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Flux Dev Model Page](https://apidot.ai/models/flux-dev) <br>
- [APIDot Flux Dev API Docs](https://apidot.ai/docs/flux-dev) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with links and implementation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; produces no executable files and makes no automatic API calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
