## Description: <br>
Generate AI images with any model using ImageRouter API (requires API key). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dawe35](https://clawhub.ai/user/dawe35) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and image-generation users use this skill to discover ImageRouter image models and run curl commands for text-to-image, image-to-image, masking, and generated image download workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, selected images, masks, and API-key-authenticated requests are sent to ImageRouter. <br>
Mitigation: Avoid private, regulated, or proprietary content unless the user accepts ImageRouter's handling of that data. <br>
Risk: Generated responses may include download URLs and local output paths for saved image files. <br>
Mitigation: Review generated download URLs and output paths before saving files locally. <br>
Risk: The workflow requires an ImageRouter API key for authenticated requests. <br>
Mitigation: Handle API keys as secrets and avoid placing real keys in shared logs, committed files, or reusable command snippets. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dawe35/skills/image-router) <br>
- [ImageRouter](https://imagerouter.io) <br>
- [ImageRouter Models](https://imagerouter.io/models) <br>
- [ImageRouter API Keys](https://imagerouter.io/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and an ImageRouter API key; generated image responses may include hosted URLs or base64 output.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
