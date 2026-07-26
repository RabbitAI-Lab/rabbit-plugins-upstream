## Description: <br>
Upscale and enhance images with the inference.sh CLI using image upscaling models such as Real-ESRGAN, Topaz Image Upscaler, Thera, and FLUX Dev Upscaler. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, creators, and image-production users use this skill to generate inference.sh CLI commands for upscaling low-resolution images, AI art, old photos, web assets, thumbnails, and print-ready images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs users to install and use the inference.sh CLI. <br>
Mitigation: Install only if inference.sh is trusted, review the installer, and use the published SHA-256 checksums or manual installation path when appropriate. <br>
Risk: Image upscaling sends image URLs and prompts to a cloud service. <br>
Mitigation: Avoid submitting sensitive private photos, proprietary images, confidential prompts, or regulated data unless the provider's data handling is understood and approved. <br>
Risk: Generated commands may run external services and process user-supplied media. <br>
Mitigation: Review commands and input URLs before execution, and confirm that the selected model and service are appropriate for the user's content and use case. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/okaris/skills/image-upscaling) <br>
- [inference.sh Running Apps](https://inference.sh/docs/apps/running) <br>
- [inference.sh Image Generation Example](https://inference.sh/docs/examples/image-generation) <br>
- [inference.sh Apps Overview](https://inference.sh/docs/apps/overview) <br>
- [inference.sh CLI Checksums](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces infsh CLI commands with JSON inputs for image URLs and prompts.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
