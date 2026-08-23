## Description:

Generates and edits Douyin ecommerce product-card images, SKU images, product-detail proof images, livestream product overlays, and Qianchuan ad test images using AI Hive image generation with optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agents use this skill to produce image prompts and run AI Hive image-generation commands for Douyin storefronts, product detail pages, livestream assets, SKU variants, and ad creative tests. It emphasizes preserving product facts and leaving prices, discounts, inventory, sales claims, and platform UI for approved operational systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or reference images and prompts are uploaded to AI Hive during generation.

Mitigation: Install and run only when uploading those images and prompts to AI Hive is acceptable for the user's business, privacy, and data-handling requirements.

Risk: The skill stores an AI Hive API key locally for reuse.

Mitigation: Prefer environment-variable or command-line key handling in stricter environments, restrict local config-file permissions, and rotate the key if it may have been exposed.

Risk: Generated ecommerce images may include inaccurate product facts or unsupported promotional claims if prompts or outputs are not reviewed.

Mitigation: Review generated images against approved product facts, brand assets, Douyin ecommerce rules, and advertising-account requirements before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/douyin-ecommerce-image-generation-editing)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key and account page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands; generated assets are downloaded image files or JSON task status when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompts, optional reference images, batch generation, routing mode selection, model parameters, output directory selection, task lookup, upload, and no-download task submission.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
