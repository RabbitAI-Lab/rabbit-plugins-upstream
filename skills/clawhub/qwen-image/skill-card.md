## Description: <br>
Generate images using Qwen Image API (Alibaba Cloud DashScope) for Chinese or English text prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robin797860](https://clawhub.ai/user/robin797860) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to generate images from Chinese or English text prompts with Alibaba Cloud DashScope. It returns a Markdown-rendered image URL by default and can save a local image file when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and generation settings are sent to Alibaba Cloud DashScope. <br>
Mitigation: Avoid sensitive prompts and use the skill only when external API processing is acceptable. <br>
Risk: DashScope API keys can be exposed if passed directly on the command line. <br>
Mitigation: Use a dedicated DashScope API key through an environment variable or secret store. <br>
Risk: The optional TLS bypass flag can weaken transport security. <br>
Mitigation: Do not use --no-verify-ssl except in a controlled proxy setup. <br>
Risk: Optional local image saving writes files to the requested path. <br>
Mitigation: Save files only to paths chosen intentionally and review generated files before relying on them. <br>


## Reference(s): <br>
- [Qwen Image on ClawHub](https://clawhub.ai/robin797860/skills/qwen-image) <br>
- [Alibaba Cloud DashScope](https://dashscope.aliyuncs.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with generated image URLs and optional local file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a DashScope API key and can optionally save generated images to a user-selected path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
