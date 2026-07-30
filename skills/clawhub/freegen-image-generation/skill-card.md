## Description: <br>
Freegen image-gen API: TXT2IMG, I2I, Inpainting, RemoveBG, Upscale via local freegen container. Supports Flux, SDXL, SD1.5, Lightning models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runtanplan22](https://clawhub.ai/user/runtanplan22) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to call a local Freegen wrapper around Dezgo for image generation and editing workflows, including text-to-image, image-to-image, inpainting, background removal, and upscaling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill documents an unfiltered image-generation route for prompts that other tools may restrict. <br>
Mitigation: Use only in workspaces that explicitly accept that content-safety posture, and review generated prompts and images against applicable policy before use. <br>
Risk: Prompts and images may be sent through the Freegen and Dezgo service path. <br>
Mitigation: Avoid sensitive, confidential, or regulated content unless the workspace has approved the service path, privacy posture, and cost implications. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runtanplan22/skills/freegen-image-generation) <br>
- [Dezgo](https://dezgo.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Configuration] <br>
**Output Format:** [Markdown with JSON payload examples and JavaScript code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes endpoint descriptions, request payload shapes, model categories, cost notes, and error-handling guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
