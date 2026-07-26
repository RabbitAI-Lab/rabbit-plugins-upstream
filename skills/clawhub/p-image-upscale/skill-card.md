## Description: <br>
Use when someone wants to upscale or sharpen an existing image for print, large crops, or higher-quality delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to upscale an existing image through Pruna's p-image-upscale model, choosing target megapixels and enhancement options for print, large crops, or higher-quality delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Pruna API key and sends user-provided images to Pruna's external API. <br>
Mitigation: Use an API key appropriate for the agent session and upload only images the user is willing to send to Pruna. <br>
Risk: Optional realism enhancement can change the appearance of synthetic or edited images. <br>
Mitigation: Confirm enhancement settings with the user and reserve realism enhancement for already photoreal sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-upscale) <br>
- [p-image-upscale model docs](https://docs.api.pruna.ai/guides/models/p-image-upscale) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with curl commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY and a user-provided source image; typical options include target megapixels, output format, detail enhancement, and realism enhancement.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
