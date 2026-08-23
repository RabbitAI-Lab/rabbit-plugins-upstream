## Description:

用 AI Hive Nano Banana 2 为真实商品逐张制作电商详情页、PDP、Amazon A+ 与 Listing 卖点图；每张图只表达一个已核准主张，并记录商品事实、主张来源、视觉证据、文案安全区和不可虚构项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers, brand teams, and designers use this skill to create fact-controlled product detail page panels, PDP modules, Amazon A+ assets, listing images, feature panels, material close-ups, how-it-works visuals, verified specification panels, and comparison graphics. It is intended for workflows where each generated image must tie a single approved product claim to supplied reference images and documented evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product reference images, prompts, and claims are sent to AI Hive during generation.

Mitigation: Install and run only when those assets are approved for AI Hive processing; avoid confidential or unapproved product assets.

Risk: The auth command can store an AI Hive API key in a local configuration file.

Mitigation: Use AI_HIVE_API_KEY or --api-key when a persistent local key file is not desired.

Risk: Generated visuals or required text can be inconsistent with approved product facts.

Mitigation: Review each panel against the original product references, approved claim source, visual evidence, and any required text before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-product-detail-page)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and generated task/status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper can save generated image files locally after submitting user-selected reference images to AI Hive.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
