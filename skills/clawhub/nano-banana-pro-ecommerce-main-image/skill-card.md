## Description:

Creates thumbnail-first ecommerce product hero images with Nano Banana Pro via AI Hive, covering marketplace listings, content-commerce cards, cross-border listings, and SKU series.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, designers, and agents use this skill to generate brand-consistent product main images, mobile thumbnails, content-commerce cards, listing visuals, and SKU variants from approved product references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are uploaded to the external AI Hive service.

Mitigation: Use only approved product assets and non-sensitive prompts, and confirm the service is acceptable for the intended workload before running the skill.

Risk: The skill uses an API key, can store it locally, and may spend API credits when generation tasks are submitted.

Mitigation: Use a dedicated AI Hive API key with appropriate account controls, protect the local configuration file, and rotate the key if it is exposed.

Risk: Generated product images can misstate product details, SKU quantities, visual claims, or platform compliance.

Mitigation: Review generated images against approved product references and current platform rules before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-ecommerce-main-image)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive setup and API access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples, AI Hive task JSON, and generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses selected reference images, prompt text, route settings, batch count, optional model parameters, and an AI Hive API key; generated files download to a local output directory unless disabled.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
