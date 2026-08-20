## Description:

通过 AI Hive 使用 Nano Banana Pro 生成和编辑商业图片，支持文生图、图生图、多参考融合、商品与人物一致性、广告海报、电商详情页和社媒素材生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and developers use this skill to plan and run Nano Banana Pro image generation and editing workflows for product photography, campaign visuals, ecommerce assets, social media materials, and localized creative variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to AI Hive for image generation or editing.

Mitigation: Use only prompts and assets approved for third-party processing, and avoid sensitive, confidential, or unauthorized reference images.

Risk: The initialization flow can open an AI Hive page and store an AI Hive API key locally in ~/.ai-hive/config.json.

Mitigation: Review the init flow before use, prefer environment variables where appropriate, and keep the local config file restricted to the current user.

Risk: Generated visuals can contain inaccurate text, prices, legal claims, brand details, or inconsistent reference-asset reproduction.

Mitigation: Review generated text, claims, packaging, logos, product geometry, and campaign assets against approved source files before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API key page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with bash command examples and generated image files downloaded by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload selected reference images to AI Hive and save generated results under ~/Downloads/AiHive unless overridden.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
