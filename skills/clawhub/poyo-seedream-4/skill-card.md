## Description: <br>
Helps agents prepare and submit PoYo Seedream 4 image-generation and editing requests, including payloads, curl commands, polling guidance, and server-side integration notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare PoYo Seedream 4 payloads, server-side curl commands, async polling or webhook guidance, and integration notes for text-to-image and image-editing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys or authorization headers could be exposed in browser code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY server-side in environment variables or a secret manager and avoid printing raw authorization headers. <br>
Risk: Private prompts, source image URLs, generated output URLs, callback URLs, or task identifiers may be shared with PoYo during use. <br>
Mitigation: Review payloads before submission and avoid sending private data unless sharing it with PoYo is acceptable. <br>
Risk: A live API submission can create an external task when the prepared payload is sent. <br>
Mitigation: Submit only after the user confirms the payload and the command is run from a trusted server-side environment. <br>


## Reference(s): <br>
- [PoYo Seedream 4 API Reference](references/api.md) <br>
- [PoYo Seedream 4 Model Page](https://poyo.ai/models/seedream-4) <br>
- [PoYo Seedream 4 API Docs](https://docs.poyo.ai/api-manual/image-series/seedream-4) <br>
- [PoYo Seedream 4 OpenAPI JSON](https://docs.poyo.ai/api-manual/image-series/seedream-4.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include request payloads, model IDs, task IDs, and next-step polling or webhook guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
