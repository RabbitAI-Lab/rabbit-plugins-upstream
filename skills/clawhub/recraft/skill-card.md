## Description: <br>
Generate, vectorize, upscale, replace background, variate, remove background, and transform images via Recraft API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nkrcrft](https://clawhub.ai/user/nkrcrft) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creative users use this skill to call Recraft image generation and editing workflows from an agent, including image generation, image-to-image transformation, background operations, vectorization, upscaling, and variations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected input images are sent to Recraft for processing. <br>
Mitigation: Use the skill only when external sharing with Recraft is permitted, and avoid sensitive or regulated images unless that sharing is approved. <br>
Risk: The skill requires a Recraft API token and can print account details with the user-info command. <br>
Mitigation: Store the token in RECRAFT_API_TOKEN or the configured OpenClaw secret location, and run user-info only when local command output may include Recraft account information. <br>


## Reference(s): <br>
- [Recraft homepage](https://www.recraft.ai/) <br>
- [Recraft API profile](https://www.recraft.ai/profile/api) <br>
- [Recraft API base URL](https://external.api.recraft.ai/v1) <br>
- [ClawHub skill page](https://clawhub.ai/nkrcrft/skills/recraft) <br>
- [Publisher profile](https://clawhub.ai/user/nkrcrft) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and saved image or SVG file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated assets are saved to user-selected filenames; supported chat providers can auto-attach paths emitted as MEDIA lines.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
