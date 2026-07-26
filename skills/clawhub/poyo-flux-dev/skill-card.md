## Description: <br>
FLUX Dev image generation and single-image editing on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use when the user explicitly requests PoYo or `flux-dev` for text-to-image, image-to-image editing, output size, image count, PNG or JPEG output, async polling, or webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to prepare and submit PoYo FLUX Dev text-to-image or single-image editing requests, including payload validation, async task submission, status polling guidance, and webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API key exposure or unauthorized live submission. <br>
Mitigation: Keep POYO_API_KEY server-side, require explicit user approval before live API calls, and avoid logging secrets. <br>
Risk: Confidential prompts, private source-image URLs, or callback URLs may be sent to PoYo or a callback receiver. <br>
Mitigation: Review payloads before submission and omit confidential or private data unless the user confirms those parties are trusted. <br>
Risk: Unsupported sizes, output counts, or malformed editing payloads can cause failed generation jobs. <br>
Mitigation: Validate payloads against the bundled API reference and current PoYo documentation before production use. <br>


## Reference(s): <br>
- [PoYo FLUX Dev API Reference](references/api.md) <br>
- [PoYo FLUX Dev model page](https://poyo.ai/models/flux-dev) <br>
- [PoYo FLUX Dev API documentation](https://docs.poyo.ai/api-manual/image-series/flux-dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and optional bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a reviewed request payload, selected generation or editing parameters, returned task_id, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
