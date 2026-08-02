## Description: <br>
Use when someone wants to upscale or sharpen an existing image for print, large crops, or higher-quality delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content teams use this skill to upscale a provided image through Pruna's hosted API for print-ready, large-crop, or higher-quality delivery. It guides agents to confirm credentials, the source image, target megapixels, enhancement settings, output format, and the relevant API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using this skill uploads the selected image and processing settings to Pruna's hosted API. <br>
Mitigation: Avoid uploading sensitive personal, confidential, or proprietary images unless the user accepts Pruna's handling of that data. <br>
Risk: The skill recommends companion skill installs before use. <br>
Mitigation: Review the companion skills and allow only the installs needed for the current workflow. <br>


## Reference(s): <br>
- [Pruna p-image-upscale model documentation](https://docs.api.pruna.ai/guides/models/p-image-upscale) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with curl command examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY and sends the selected image plus processing settings to Pruna's hosted API.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
