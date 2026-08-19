## Description:

使用 Nano Banana Pro 精修商品照片，清理灰尘与划痕、校正颜色和白平衡、控制反光、修复背景与阴影，同时锁定商品几何和包装事实。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, designers, and developers use this skill to generate Nano Banana Pro product-photo retouching prompts and commands for dust cleanup, color correction, reflection control, background repair, SKU consistency, and commercial image optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are sent to AI Hive, and an AI Hive API key may be stored locally.

Mitigation: Use the skill only when this data handling is acceptable, protect the local API key, and keep the default AI Hive base URL unless intentionally changing endpoints.

Risk: Product retouching may alter facts that buyers rely on, including geometry, labels, material appearance, or damage visibility.

Mitigation: Compare outputs with originals, preserve product structure and packaging facts, and retain original files for rollback.

## Reference(s):

- [AI Hive API access page](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-product-retouch)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generated image files are downloaded by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive credentials and uploads selected product images to the configured AI Hive API endpoint.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact changelog top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
