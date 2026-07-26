## Description: <br>
Generate, vectorize, upscale, replace background, variate, remove background, and transform images via Recraft API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nkrcrft](https://clawhub.ai/user/nkrcrft) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creative operators use this skill to generate and edit raster or vector images through Recraft API commands, including background operations, variation, upscaling, and account-information checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected images are sent to Recraft and may include confidential or sensitive content. <br>
Mitigation: Use the skill only with data approved for Recraft, and avoid confidential images unless Recraft is approved for that data. <br>
Risk: The user-info command can print account details such as email or credit information into shared logs. <br>
Mitigation: Run user-info only in private contexts and avoid sharing logs that may contain account information. <br>
Risk: The skill writes generated outputs to user-specified file paths. <br>
Mitigation: Choose output paths carefully and review filenames before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nkrcrft/skills/recraft-ai) <br>
- [Recraft](https://www.recraft.ai/) <br>
- [Recraft API Key Profile](https://www.recraft.ai/profile/api) <br>
- [Recraft External API Endpoint](https://external.api.recraft.ai/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [PNG or SVG image files with brief terminal status text and MEDIA path lines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uv and a RECRAFT_API_TOKEN; prompts and selected input images are sent to Recraft API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
