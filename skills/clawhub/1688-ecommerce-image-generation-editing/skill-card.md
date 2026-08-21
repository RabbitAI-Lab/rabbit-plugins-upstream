## Description:

为1688工厂与批发商生成和编辑产品主图、规格图、工厂能力图、定制说明、包装运输和批量SKU图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External 1688 sellers, factories, wholesalers, and their operators use this skill to generate or edit procurement-oriented product images, SKU visuals, customization diagrams, packaging views, and factory-process visuals from verified supplier materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an AI Hive API key locally for repeated use.

Mitigation: Use a dedicated API key, keep the local config file private, and rotate or revoke the key if the environment is shared or compromised.

Risk: Selected product or reference images are uploaded to AI Hive for generation or editing.

Mitigation: Upload only materials approved for that service and avoid including confidential supplier, customer, or unreleased product information unless authorized.

Risk: Generated 1688 product visuals could imply unsupported specifications, certifications, production capacity, pricing, or delivery claims.

Mitigation: Keep supplier facts from verified source materials and review images before listing so business claims are manually confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/1688-ecommerce-image-generation-editing)
- [AI Hive API access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated image files downloaded by the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive API credentials, accepts optional reference images, and writes generated outputs to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
