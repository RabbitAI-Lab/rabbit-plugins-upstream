## Description:

Create and edit Shopify product photography, PDP image galleries, collection banners, DTC lifestyle images and campaign creatives for Shopify商品图、独立站PDP、Hero Image、产品套图、DTC品牌视觉、Meta Ads素材、邮件营销、换背景、多市场本地化和批量SKU with reference-guided generation through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopify merchants, ecommerce teams, and developers use this skill to plan and run AI Hive image-generation workflows for PDP galleries, collection cards, homepage heroes, paid social creatives, localized lifestyle images, and batch SKU assets while preserving product and brand consistency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or reference media can be uploaded to AI Hive.

Mitigation: Do not pass private files with --image or --file unless the user intends to send them to the service.

Risk: The skill stores or reads an AI Hive API key locally.

Mitigation: Use a scoped API key, keep local configuration permissions restricted, and rotate the key if it may have been exposed.

Risk: Generated ecommerce assets can introduce unsupported claims, offers, reviews, certifications, or legal text.

Mitigation: Review outputs against approved product facts, brand requirements, Shopify theme constraints, and current ad-channel policies before publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wubin1836/skills/shopify-ecommerce-image-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; the helper script can return JSON task data and download generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive API credentials, optional reference image uploads, configurable routing and model parameters, batch generation, and an output directory for downloaded assets.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact changelog top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
