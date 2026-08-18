## Description:

使用 GPT Image 2 将人物、商品、服装、姿势、场景、光线、构图和品牌风格等多张参考图按指定职责组合成新图片。Use this skill for GPT Image 2 multi-reference image generation、多图融合、参考图合成、人物与商品同框、换装、品牌视觉、室内搭配、角色连续内容和电商广告合成；通过 AI Hive 自动上传多张素材并生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, ecommerce teams, and developers use this skill to combine multiple authorized reference images into a new GPT Image 2 image while keeping each reference image's role explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and reference images are uploaded to AI Hive.

Mitigation: Use only authorized, intended reference materials and avoid private or unrelated files in upload and generate commands.

Risk: The AI Hive API key may be stored in ~/.ai-hive/config.json.

Mitigation: Protect the local config file and remove it when the saved key is no longer needed.

Risk: Generated images can mix identity, product, brand, or scene details incorrectly across references.

Mitigation: Keep an explicit reference-role contract and review generated outputs before approval or release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-multi-reference-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown guidance with inline bash commands and generated image files downloaded by the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uploads user-selected reference images and prompts to AI Hive, then polls task status and downloads completed image outputs unless no-download mode is selected.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
