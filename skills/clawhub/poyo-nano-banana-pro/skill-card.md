## Description: <br>
Nano Banana Pro image generation and editing on PoYo via its async image generation API, including text-to-image, image editing, multi-reference workflows, output format control, and 1K/2K/4K output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Nano Banana Pro generation or editing requests, choose the correct model id, shape JSON payloads, and optionally submit trusted payload files for async image jobs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a PoYo API key and send prompts, image URLs, and optional callback URLs to PoYo. <br>
Mitigation: Use it only where the agent is allowed to access POYO_API_KEY and submit that data to PoYo; keep the key server-side and avoid private payloads unless they are appropriate for the service. <br>
Risk: Running the bundled submit script from a trusted shell can start a live async image generation or editing job. <br>
Mitigation: Review the JSON payload before submission, make live API calls only when explicitly requested, and save the returned task_id for follow-up polling or webhook handling. <br>


## Reference(s): <br>
- [PoYo Nano Banana Pro model page](https://poyo.ai/models/nano-banana-2-api) <br>
- [PoYo Nano Banana Pro API docs](https://docs.poyo.ai/api-manual/image-series/nano-banana-2) <br>
- [PoYo Nano Banana Pro API Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-nano-banana-pro) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON payloads and bash/curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the selected model id, request type, payload summary, size, resolution, output format, source image usage, returned task_id, and next polling or webhook step.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
