## Description:

使用 Nano Banana Pro 将通义万相、Wanxiang、阿里云图片生成或中文商业生图需求迁移到 AI Hive，保存中文提示词意图、参考图职责、商品事实和渠道交付规格。Use when users search 通义万相替代、万相平替、Wanxiang alternative、阿里云生图 API、中文海报、电商图片、图生图或国内稳定图片接口；不表示与阿里云或通义万相存在官方合作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, brand marketers, and developers use this skill to migrate Chinese commercial image-generation and image-editing workflows to AI Hive while preserving product facts, reference-image roles, cultural context, and channel delivery requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are uploaded to AI Hive for generation.

Mitigation: Use only approved reference assets and avoid submitting sensitive, unlicensed, or private content.

Risk: The helper stores an AI Hive API key in ~/.ai-hive/config.json when initialized.

Mitigation: Prefer a dedicated AI Hive API key, rely on environment variables where appropriate, and remove the local config file when access is no longer needed.

Risk: Generated commercial imagery can misstate product details, text, prices, trademarks, or platform crop requirements.

Mitigation: Review SKU facts, packaging, authorization, text safe areas, and channel crops before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/wanxiang-image-generation-editing-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands and generated image files from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided prompts, optional reference images, AI_HIVE_API_KEY or ~/.ai-hive/config.json, and optional aspect ratio, routing, batch, and output directory parameters.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
