## Description: <br>
Generate images from text prompts using xAI's Grok image generation API, with options for output format, batch size, and OpenClaw media attachment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mexicanamerican](https://clawhub.ai/user/mexicanamerican) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to generate image files or base64 image output from text prompts through xAI's Grok image generation API. It is suited for agent workflows that need to create images and attach generated media paths to responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and generation parameters are sent to xAI as a third-party API provider. <br>
Mitigation: Avoid submitting secrets, personal data, or confidential business information in prompts, and review xAI account and data-handling requirements before use. <br>
Risk: The skill requires an xAI API key, which could be exposed if stored insecurely. <br>
Mitigation: Use a scoped API key where possible and store it in a secrets manager or temporary environment variable instead of committing it to files. <br>
Risk: The release depends on the Python requests package and external network access. <br>
Mitigation: Review or pin dependencies before production use and run the skill only in environments where outbound calls to xAI are expected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mexicanamerican/skills/xai-image-gen) <br>
- [Publisher profile](https://clawhub.ai/user/mexicanamerican) <br>
- [xAI console](https://console.x.ai) <br>
- [xAI image generation endpoint](https://api.x.ai/v1/images/generations) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Shell commands, Configuration] <br>
**Output Format:** [Generated image files or base64 text, with CLI status output and OpenClaw MEDIA path lines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an xAI API key in XAI_API_KEY and network access to xAI; supports prompt text, model, filename, response format, batch count, and verbose mode.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, skill.json, and artifact documentation) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
