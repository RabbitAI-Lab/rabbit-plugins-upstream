## Description: <br>
Use when someone wants to upscale or sharpen an existing image for print, large crops, or higher-quality delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to guide agents through Pruna image upscaling workflows for existing images, including collecting required image and output-size inputs and preparing API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected images are sent to Pruna's API for processing. <br>
Mitigation: Avoid uploading private or sensitive images unless Pruna's data handling terms fit the intended use. <br>
Risk: The workflow uses PRUNA_API_KEY for authenticated API calls. <br>
Mitigation: Confirm the key is available only in the execution environment and do not paste it into prompts, logs, or shared files. <br>
Risk: Upscaling or realism enhancement can change visual details in the source image. <br>
Mitigation: Confirm target megapixels and enhancement settings with the user, and use realism enhancement only when the source is already photoreal. <br>


## Reference(s): <br>
- [p-image-upscale model docs](https://docs.api.pruna.ai/guides/models/p-image-upscale) <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-upscale) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a source image URL or upload, PRUNA_API_KEY, target megapixels, output format, and optional enhancement settings.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
