## Description:

使用 GPT Image 2 按购买问题设计商品详情页模块，包括首屏、卖点证据、材质细节、尺寸说明、使用步骤、包装清单和SKU选择。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Commerce designers, marketplace operators, and agents preparing product detail pages use this skill to break buyer questions into PDP modules and generate image-generation commands for product hero, evidence, sizing, usage, package, and SKU visuals. Approved copy, prices, specifications, dimensions, claims, and legal language are expected to be added in a design or layout tool rather than generated into the image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or reference images and prompts are uploaded to AI Hive during generation.

Mitigation: Use approved, non-sensitive assets and avoid uploading private or regulated local files.

Risk: The init flow can store an AI Hive API key in the user's home directory.

Mitigation: Prefer AI_HIVE_API_KEY or the command-line API key option when a persistent config file is not desired, and restrict or remove any saved config.

Risk: Generated visuals can imply unsupported dimensions, claims, certifications, prices, or platform compliance if those details are delegated to the image model.

Mitigation: Keep approved copy, legal claims, prices, dimensions, and platform-specific compliance text in the layout stage and review each module against source product data.

## Reference(s):

- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key and chat page](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-product-detail-page)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline bash commands and generated image files from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive with selected reference images, prompts, model parameters, and an output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
