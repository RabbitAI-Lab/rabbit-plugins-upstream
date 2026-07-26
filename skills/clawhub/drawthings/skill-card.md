## Description: <br>
Generate images with DrawThings Stable Diffusion through a local Automatic1111-compatible API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dustinparsons](https://clawhub.ai/user/dustinparsons) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, designers, and agents use this skill to generate image files from text prompts through a local DrawThings or compatible Stable Diffusion API, including batches, presets, custom dimensions, and reproducible seeds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts may contain secrets, private client data, or regulated information that could be exposed if DRAWTHINGS_URL or --api-url points to a non-local service. <br>
Mitigation: Use the default local DrawThings endpoint or another trusted endpoint, and avoid placing secrets, private client data, or regulated information in prompts. <br>
Risk: Generated PNG files and sidecar metadata can include prompts and generation parameters that may be inappropriate to share. <br>
Mitigation: Review generated files and metadata before sharing or publishing them, and save outputs only to appropriate local locations. <br>
Risk: Large dimensions, high step counts, or large batches can consume local compute, memory, and time. <br>
Mitigation: Start with smaller dimensions, fewer steps, or a small batch size, then increase settings only when the local system can handle the workload. <br>


## Reference(s): <br>
- [DrawThings API Reference](references/api-reference.md) <br>
- [Recommended Models for DrawThings](references/models.md) <br>
- [CivitAI Model Repository](https://civitai.com) <br>
- [Hugging Face Models](https://huggingface.co/models) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [PNG image files with optional JSON metadata and terminal status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses DRAWTHINGS_URL or the default local API endpoint; prompts and generation settings may be saved with generated files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
