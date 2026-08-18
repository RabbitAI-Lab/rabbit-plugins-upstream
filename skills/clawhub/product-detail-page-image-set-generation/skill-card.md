## Description:

使用 Nano Banana Pro 把商品资料转换成完整详情页套图镜头清单，并逐模块生成首屏、利益、结构、步骤、尺寸、场景和装箱图片。Use this skill for 商品详情页套图一键生成、PDP image set、淘宝天猫京东抖店详情页、Amazon A+、Shopify 商品页、卖点图、结构图、步骤图、规格图和电商长图；通过 AI Hive 生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and developers use this skill to turn approved product facts and reference images into a module-by-module product detail page image plan and AI Hive image-generation commands for marketplaces such as Taobao, JD, Amazon A+, and Shopify.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and approved reference images are sent to an external AI Hive image service.

Mitigation: Use only approved assets, avoid proprietary or sensitive product images unless external sharing is acceptable, and review the provider's retention terms before use.

Risk: Generated product detail images may introduce unsupported product claims, dimensions, certifications, accessories, or visual inconsistencies.

Mitigation: Trace every claim to approved evidence, keep one product master across modules, and perform human layout and accuracy review before publishing.

Risk: API keys may be provided through an environment variable, command-line flag, or local config file.

Mitigation: Prefer environment variables or the initialized config with restricted file permissions, and rotate keys if they are exposed.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wubin1836/skills/product-detail-page-image-set-generation)
- [ClawHub publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples; generated image files are downloaded as PNG by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed Nano Banana Pro image model through AI Hive, with optional reference images, prompt parameters, routing mode, batch size, task lookup, and output directory settings.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
