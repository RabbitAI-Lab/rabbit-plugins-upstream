## Description:

根据商品图片和品牌参数提取统一的品牌视觉语言，并输出结构化 brandGeneJson 供下游商品套图生成流程复用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and ecommerce content teams use this skill to derive brand color, typography, localized background strategy, lighting, and brand-injection guidance from product images and brand inputs. The resulting brandGeneJson is intended for downstream image-generation orchestration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide users through LinkFox authentication and API-key issuance.

Mitigation: Prefer obtaining and storing API keys through LinkFox's first-party site, and avoid sharing credentials in prompts or logs.

Risk: The skill includes billing and payment-order helper flows.

Mitigation: Require explicit user confirmation before any purchase step and verify plan, amount, and payment method before proceeding.

Risk: Environment URL overrides can redirect account, billing, or gateway traffic.

Mitigation: Use default LinkFox endpoints unless the alternate endpoint is trusted and intentionally configured.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-imagegen-brand-gene-extract)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Onboarding guidance](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON with supporting Markdown and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a length-one brandGeneJson list and saves it to the session data directory for downstream reuse.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
