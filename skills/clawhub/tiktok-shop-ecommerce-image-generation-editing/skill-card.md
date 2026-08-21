## Description:

Create and edit TikTok Shop product listing images, shoppable-video covers, affiliate creator packs and livestream product visuals. Use this skill for TikTok Shop商品图、TikTok带货封面、商品卡、UGC素材包、直播间商品图、跨境电商主图、多市场本地化和商品换背景；supports reference-guided image generation and AI Hive delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, creators, and commerce operators use this skill to generate or edit TikTok Shop product listing images, shoppable-video covers, affiliate asset packs, livestream cards, ad-test images, and localized lifestyle visuals while preserving SKU facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected product images and prompts to AI Hive and may store or use an AI Hive API key.

Mitigation: Submit only intended non-sensitive media, use the documented generate/task/init flow, and manage API keys through the documented configuration, environment variable, or command-line paths.

Risk: Generated commerce images may introduce unsupported prices, ratings, certifications, scarcity claims, testimonials, or offer text.

Mitigation: Review generated assets against merchant-provided SKU facts and current TikTok Shop rules before upload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/tiktok-shop-ecommerce-image-generation-editing)
- [AI Hive API Base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API Key Access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with bash commands and generated image files downloaded by the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive API credentials, optional reference images, batch count, routing, params, output directory, and no-download mode.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
