## Description:

根据商品图片和品牌参数提取统一的品牌视觉语言，并输出结构化 brandGeneJson 供下游图像生成技能复用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and agent workflows use this skill to analyze product imagery with brand parameters such as color, font, language, platform, and sales region, then produce a reusable visual identity JSON for downstream image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes authentication and API-key helper flows in addition to brand-style extraction.

Mitigation: Use the official LinkFox account UI or a secure secret store for API keys when possible, and only share SMS codes with an agent when account login is explicitly intended.

Risk: The skill includes billing and order helper flows.

Mitigation: Review and confirm any plan, payment method, order, QR code, or payment URL before proceeding.

Risk: Generated brand data is saved locally for downstream reuse.

Mitigation: Review local session data before sharing or retaining it, especially when product imagery or brand parameters are sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-imagegen-brand-gene-extract)
- [Skill instructions](artifact/SKILL.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Structured JSON brandGeneJson plus local session data files and concise setup guidance when authentication or billing errors occur.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The primary agent output is a length-1 brandGeneJson list saved to the session data directory for downstream image-generation skills.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact _meta.json reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
