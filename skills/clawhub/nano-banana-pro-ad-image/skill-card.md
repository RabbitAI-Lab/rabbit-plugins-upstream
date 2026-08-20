## Description:

使用 Nano Banana Pro 通过 AI Hive 生成或编辑移动端广告图片，面向信息流、社交广告、商品推广、UGC 风格静帧和大促素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to generate and adapt brand-visible ad images for mobile feeds, social ads, product cards, UGC-style stills, promotion layouts, and multi-placement creative variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected reference images or media may be uploaded to AI Hive during generation or upload commands.

Mitigation: Use only approved assets, avoid sensitive unrelated files, and confirm that any uploaded product or brand materials are appropriate for the AI Hive service.

Risk: The skill requires an AI Hive API key that can be passed through an environment variable, CLI flag, or local configuration file.

Mitigation: Keep the API key private, prefer deliberate environment or local config use, restrict local config permissions, and rotate the key if it is exposed.

Risk: Generated advertising images may contain incorrect product details, brand marks, text, prices, offers, or advertising claims.

Mitigation: Review generated images against approved source materials and campaign claims before publication, including the skill's one-second mobile creative checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-ad-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key and chat page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples; generated image files are downloaded to a local output directory unless no-download mode is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompts, optional reference images, batch count, routing mode, model parameters such as aspect ratio, API credentials, and output directory settings.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
