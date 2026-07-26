## Description: <br>
Ai Image Gen helps an agent generate and edit images through a configured Gemini Flash Image service, including text-to-image, image-to-image, style conversion, multiple aspect ratios, and up to 4K output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and design teams use this skill to have an agent prepare prompts, select image models and dimensions, call the configured image-generation service, and return generated image files or paths for commercial creative workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and reference images are sent to the configured image-generation service. <br>
Mitigation: Use the skill only with prompts and reference images that are acceptable to send to that service. <br>
Risk: The skill requires an image-generation API key. <br>
Mitigation: Set the API key through environment variables and avoid pasting, logging, storing, or committing secrets. <br>
Risk: Generated image files are written to local output paths. <br>
Mitigation: Choose explicit output paths and review them before execution to avoid overwriting local files. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/thcjp/skills/ai-image-gen) <br>
- [Clawdis Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, JSON] <br>
**Output Format:** [Markdown guidance with shell commands, JSON status examples, and generated image file paths such as PNG outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on the configured image-generation API, selected model, prompt detail, reference image quality, and explicit local output path.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
