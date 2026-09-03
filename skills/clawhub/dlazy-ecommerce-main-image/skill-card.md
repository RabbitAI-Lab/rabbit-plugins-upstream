## Description:

Helps ecommerce teams turn approved product photos into channel-ready main-image candidates for white-background baselines, visual-difference images, lifestyle scenes, color SKU sets, and single-variable A/B tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and marketing teams use this skill to prepare main-image candidates from approved product photos while preserving product facts, platform constraints, and A/B test isolation. It is aimed at marketplace and social commerce channels including Taobao, Tmall, JD, Pinduoduo, Douyin, Xiaohongshu, Amazon, TikTok Shop, and Shopify.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are sent to dLazy hosted services for processing.

Mitigation: Use only approved commercial product photos and install the skill only when sending those inputs to dLazy is acceptable.

Risk: A dLazy API key may be stored in the local CLI config or supplied through the environment.

Mitigation: Use organization-approved credentials and rotate or revoke keys when access changes.

Risk: Short requests such as 白底图 or 测图 may be ambiguous outside ecommerce main-image work.

Mitigation: Confirm the user wants ecommerce main-image generation or testing before invoking the skill.

Risk: Batch generation can spend credits quickly if prompt or image parameters are wrong.

Mitigation: Run a dry run before batch submissions and review the payload and estimated cost.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline bash commands and JSON CLI response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call dLazy banana-pro to generate hosted image URLs; supports dry-run, async submission, and 1K, 2K, or 4K image sizes.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
