## Description:

使用 Nano Banana Pro 迁移 PhotoRoom、Photo Room 或 Photoroom API 常见的电商商品处理需求，完成背景清理、白底图、自然阴影、生活方式场景和批量 SKU 统一。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and developers use this skill to generate or edit ecommerce product images for white backgrounds, transparent edges, natural shadows, lifestyle scenes, and consistent batch SKU presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images, prompts, and the AI Hive API key are sent to the disclosed AI Hive endpoint.

Mitigation: Use the skill only when AI Hive is acceptable for the workflow, and avoid sensitive product photos unless that provider is approved.

Risk: Generated product edits may alter colors, logos, edges, counts, shadows, or included accessories in ways that could misrepresent a SKU.

Mitigation: Compare outputs against the original product photos and perform the documented edge and authenticity QA before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/photoroom-image-generation-editing-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generated image files are saved locally by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompts, optional reference images, batch size, routing mode, and model parameters such as aspect_ratio.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
