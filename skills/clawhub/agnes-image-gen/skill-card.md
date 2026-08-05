## Description: <br>
使用 Agnes AI 的图像生成 API 生成和编辑图片，支持文生图和图生图工作流。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiuwu2495](https://clawhub.ai/user/jiuwu2495) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to call Agnes AI for text-to-image generation and image-to-image editing, then save generated image files locally. It is intended for creative design, marketing content, product visualization, social media assets, and image transformation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill bundles and may automatically use a hardcoded Agnes API key. <br>
Mitigation: Configure a user-owned Agnes API key through secure configuration and treat the bundled key as exposed and unsuitable for shared distribution. <br>
Risk: Prompts and optional input images are sent to external Agnes endpoints for generation or editing. <br>
Mitigation: Avoid sending sensitive images, proprietary prompts, or confidential visual material through this skill unless the external service is approved for that data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiuwu2495/skills/agnes-image-gen) <br>
- [Agnes AI](https://agnes-ai.com) <br>
- [Agnes image generation endpoint](https://apihub.agnes-ai.com/v1/images/generations) <br>
- [Agnes image generation fallback endpoint](https://apihub.agnes-ai.cn/v1/images/generations) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Files, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON API responses, generated image files, and local file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated image URLs may expire; the script downloads images to local PNG files when URL output is returned.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
