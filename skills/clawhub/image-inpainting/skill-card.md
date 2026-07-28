## Description: <br>
Mask-driven image inpainting on RunComfy via the runcomfy CLI, routing to Z-Image Turbo Inpainting when a mask is available and to instruction-driven edit models when the target region must be described. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to direct agents through RunComfy image inpainting workflows for object removal, watermark cleanup, region replacement, blemish fixes, and other controlled local still-image edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image and mask URLs are sent to RunComfy for third-party processing. <br>
Mitigation: Use the skill only when the user intentionally requests RunComfy-backed image edits and is comfortable sending the relevant image inputs to that service. <br>
Risk: Broad edit requests such as object or watermark removal can be invoked unintentionally. <br>
Mitigation: Confirm the requested edit and target region before invoking runcomfy for broad or sensitive local-image edits. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/image-inpainting) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [Z-Image Turbo Inpainting](https://www.runcomfy.com/models/tongyi-mai/z-image/turbo/inpainting?utm_source=clawhub&utm_medium=skill&utm_campaign=image-inpainting) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=image-inpainting) <br>
- [Z-Image Turbo Inpainting LoRA](https://www.runcomfy.com/models/tongyi-mai/z-image/turbo/inpainting/lora?utm_source=clawhub&utm_medium=skill&utm_campaign=image-inpainting) <br>
- [Best image editing models collection](https://www.runcomfy.com/models/collections/best-image-editing-models?utm_source=clawhub&utm_medium=skill&utm_campaign=image-inpainting) <br>
- [Z-Image base and LoRA variants](https://www.runcomfy.com/models/tongyi-mai/z-image/turbo?utm_source=clawhub&utm_medium=skill&utm_campaign=image-inpainting) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown with inline bash commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the runcomfy CLI, RUNCOMFY_TOKEN, and RunComfy configuration for execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
