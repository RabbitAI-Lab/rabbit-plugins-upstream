## Description: <br>
Guides an agent through LinkFox image generation and editing workflows for text-to-image, image-to-image, background replacement, style transfer, product compositing, and model swapping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, ecommerce operators, and creative agents use this skill to generate or edit product and marketing images from prompts and optional reference images. It helps prepare image-generation API calls, upload local reference images when needed, and interpret returned image results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reference images and prompts are sent to LinkFox, and local image files may be uploaded as public URLs for the workflow. <br>
Mitigation: Use only images and prompts that are acceptable to share with LinkFox, and avoid private, regulated, or confidential content unless gateway, retention, and public-link behavior have been approved. <br>
Risk: The skill stores full API responses and cache files under the current working directory. <br>
Mitigation: Run it from an appropriate project workspace, review saved response files before sharing the workspace, and remove cached or generated response data when it is no longer needed. <br>
Risk: The artifact includes automatic feedback reporting behavior when results or user reactions indicate an issue or improvement. <br>
Mitigation: Review feedback content before sending and avoid including private user data, credentials, or confidential project details. <br>
Risk: Image generation consumes LinkFox credits and may incur additional cost for repeated calls. <br>
Mitigation: Tell the user before making cost-incurring calls, reuse cached results for identical requests when appropriate, and ask before retrying with changed parameters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-generate-image) <br>
- [AI drawing API reference](artifact/references/api.md) <br>
- [LinkFox skill guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses; generated image content may be displayed as Markdown images.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports prompts up to 1000 characters, up to 3 public reference image URLs, and aspect ratios 1:1, 3:4, 4:3, 9:16, and 16:9.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
