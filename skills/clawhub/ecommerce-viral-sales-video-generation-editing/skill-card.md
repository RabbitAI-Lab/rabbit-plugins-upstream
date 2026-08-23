## Description:

为淘宝、天猫、京东、抖音电商、小红书、快手、Amazon、TikTok Shop、Instagram 与 Shopify 制作高留存、高转化的电商带货视频，并在不改商品事实的前提下修复已有素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, content teams, merchants, brands, and agencies use this skill to plan, generate, and repair short sales videos for product listings, social commerce, UGC ads, Reels, Shorts, and storefront placements while preserving approved product facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation commands can upload product images, videos, and prompt content to AI Hive.

Mitigation: Use --preview to inspect prompts before upload, and provide only assets approved for that service.

Risk: The workflow uses an AI Hive API key that may be supplied on the command line, in AI_HIVE_API_KEY, or in ~/.ai-hive/config.json.

Mitigation: Prefer environment or config-based secrets, keep the config file private, and rotate exposed keys.

Risk: Generated sales videos may imply unsupported product claims, offers, prices, ratings, or platform UI if inputs are not controlled.

Mitigation: Provide approved claim, offer, continuity, and rejection constraints, then review outputs against channel policy and product fact sources before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ecommerce-viral-sales-video-generation-editing)
- [AI Hive OpenAPI endpoint](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with bash command examples and JSON preview output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload user-provided product images or videos to AI Hive for Seedance 2.5 generation unless run with --preview.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
