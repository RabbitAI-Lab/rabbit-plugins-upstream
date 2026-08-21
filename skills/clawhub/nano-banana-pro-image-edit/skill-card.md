## Description:

使用 Nano Banana Pro 按自然语言编辑现有图片，帮助用户明确保留区、修改区和禁止变化项，并通过 AI Hive 上传、生成与下载结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, designers, and developers use this skill to edit existing images with explicit preservation, change, and validation requirements. It is suited for object removal, product color changes, localized clothing edits, ad-layout revision, batch image variants, and reference-image editing through AI Hive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected image files and prompts are uploaded to AI Hive for processing.

Mitigation: Use only image inputs intended for AI Hive, and avoid uploading sensitive or unauthorized content.

Risk: The AI Hive API key may be stored in ~/.ai-hive/config.json or supplied through the environment or command line.

Mitigation: Keep the API key private, review the local config file after initialization, and rotate credentials if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-image-edit)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload selected image inputs to AI Hive and download generated results to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
