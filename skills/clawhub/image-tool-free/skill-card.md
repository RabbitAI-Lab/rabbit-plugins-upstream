## Description: <br>
图像处理基础版 helps an agent inspect, crop, resize, convert, compress, and manage metadata for image files, with support for common web formats such as PNG, JPEG, WebP, and AVIF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual users use this skill to guide an agent through lightweight image-processing tasks such as checking image properties, optimizing images for the web, converting formats, and managing EXIF or ICC metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to run local commands and modify image files. <br>
Mitigation: Review proposed commands and operate on copies or backed-up files before applying destructive edits. <br>
Risk: The skill includes mixed privacy and network guidance, including optional callbacks and external API access. <br>
Mitigation: Prefer local-only workflows, avoid callback URLs unless required, and review any network use before execution. <br>
Risk: Image metadata can contain sensitive information. <br>
Mitigation: Inspect and strip EXIF or other metadata before sharing processed images outside the local environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/image-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local image-file operations and optional callback/API-related configuration.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
