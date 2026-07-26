## Description: <br>
Generate images with FLUX models through the inference.sh CLI, including text-to-image, image-to-image, and LoRA-based style adaptation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, creators, and agent operators use this skill to prepare and run inference.sh commands for FLUX image generation, custom LoRA styles, and image-to-image transformations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on a third-party CLI installer and cloud image-generation service. <br>
Mitigation: Install only if inference.sh is trusted; review the installer or use the documented manual checksum path before running it. <br>
Risk: Prompts, private image URLs, personal data, secrets, or sensitive images may be sent to a third-party processing service. <br>
Mitigation: Do not submit confidential or sensitive inputs unless that third-party processing is acceptable for the workflow. <br>


## Reference(s): <br>
- [Flux Image on ClawHub](https://clawhub.ai/okaris/skills/flux-image) <br>
- [inference.sh](https://inference.sh) <br>
- [inference.sh CLI installer](https://cli.inference.sh) <br>
- [Manual install checksums](https://dist.inference.sh/cli/checksums.txt) <br>
- [Running Apps](https://inference.sh/docs/apps/running) <br>
- [Image Generation Example](https://inference.sh/docs/examples/image-generation) <br>
- [Streaming Results](https://inference.sh/docs/api/sdk/streaming) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The referenced CLI commands can submit prompts, image URLs, and LoRA inputs to inference.sh-hosted image generation services.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
