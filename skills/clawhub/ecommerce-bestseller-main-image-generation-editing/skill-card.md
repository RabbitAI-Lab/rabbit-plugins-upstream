## Description:

使用 Nano Banana Pro 为电商商品生成和编辑白底、场景、SKU 与单变量测试主图候选，并强调商品事实、可视证据和平台规范核查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and marketers use this skill to generate and edit product main-image candidates for marketplaces and social commerce while keeping product evidence, channel rules, and test variables explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or reference images and prompts are sent to AI Hive for generation.

Mitigation: Use approved product assets and avoid confidential images unless the AI Hive account and data terms permit that use.

Risk: The helper stores or reads an AI Hive API key locally or from the environment.

Mitigation: Keep API keys out of shared logs and repositories, and rely on the script's restricted local config permissions or environment variables.

Risk: Generated ecommerce images can imply inaccurate product claims, accessories, quantities, prices, or platform-disallowed messaging.

Mitigation: Review generated images against real SKU facts, channel rules, and approved product assets before publishing.

Risk: Main-image changes alone do not guarantee bestseller status, clicks, or conversion.

Mitigation: Run controlled single-variable tests and evaluate real click, add-to-cart, and conversion data before scaling a candidate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ecommerce-bestseller-main-image-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands, JSON task output, and downloaded image files from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the fixed public_model_nano_banana_pro image model and supports user-selected reference images, batch generation, task lookup, and local result downloads.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
