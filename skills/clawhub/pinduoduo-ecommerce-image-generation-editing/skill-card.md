## Description:

为拼多多店铺生成和编辑商品主图、SKU 套图、活动图、使用场景图和多多搜索/多多场景测图，支持参考图保真及 AI Hive 批量生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and developers use this skill to plan, generate, vary, review, and download Pinduoduo product images for master product shots, SKU variants, specification images, usage scenes, and ad testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or reference images and prompts are sent to AI Hive.

Mitigation: Use only images and prompts approved for that provider, and avoid submitting confidential or restricted product material.

Risk: The workflow stores an AI Hive API key locally or reads it from the environment.

Mitigation: Use a scoped key where possible, keep the local config file private, and rotate the key if it may have been exposed.

Risk: Image generation can incur provider charges.

Mitigation: Check current pricing before batch runs and validate one SKU before scaling generation.

Risk: Generated ecommerce images may contain inaccurate product details or platform-noncompliant claims.

Mitigation: Review outputs against the product master data and current Pinduoduo category, main-image, and advertising rules before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/pinduoduo-ecommerce-image-generation-editing)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generated image files and JSON task responses from the AI Hive command-line workflow.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompts, optional reference images, batch size, model parameters, routing mode, output directory, and no-download mode; generated files are downloaded when task polling succeeds.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
