## Description: <br>
Use APIDot for Seedream 5.0 Lite API workflows, including Seedream 5.0 Lite, image generation API, image editing API, multi-reference image generation, reference-guided editing, structured layout image workflows, async task submission, task_id handling, polling, task status, webhook integration, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route Seedream 5.0 Lite image generation and editing questions to APIDot documentation, model pages, examples, and async workflow guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys may be exposed if used in browser code, logs, public repositories, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in a backend secret store or server-side environment variable and avoid displaying or logging it. <br>
Risk: Prompts, private image URLs, generated image URLs, and callback URLs may contain sensitive data. <br>
Mitigation: Avoid logging sensitive prompts, image URLs, generated result URLs, callback URLs, or other private workflow data. <br>
Risk: Model fields, limits, availability, and commercial terms can change outside the skill artifact. <br>
Mitigation: Use current APIDot docs and model pages before preparing payloads or sending data. <br>


## Reference(s): <br>
- [APIDot Seedream 5.0 Lite Reference](references/api.md) <br>
- [APIDot Documentation](https://apidot.ai/docs) <br>
- [Seedream 5.0 Lite Model Page](https://apidot.ai/models/seedream-5-0-lite) <br>
- [Seedream 5.0 Lite API Docs](https://apidot.ai/docs/seedream-5-0-lite) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Webhooks](https://apidot.ai/docs/webhooks) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown guidance with links and integration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable code, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
