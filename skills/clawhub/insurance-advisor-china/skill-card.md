## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in mainland China use this skill to explore insurance needs, compare products, estimate premiums, design coverage plans, and understand underwriting, compliance, and claims considerations. It supports Chinese-language advisory workflows using bundled reference materials and local calculation scripts.

### Deployment Geography for Use:

China (mainland)

## Known Risks and Mitigations:

Risk: The skill may process personal, family, income, budget, mortgage, health, and underwriting-related details.

Mitigation: Collect only details needed for the advisory task and avoid exposing sensitive user information outside the intended session.

Risk: Bundled product data, premium estimates, insurer terms, and sales contact details may be stale or differ from official insurer materials.

Mitigation: Verify product availability, premiums, policy terms, and sales contacts independently before making purchase decisions.

Risk: Insurance suggestions may be mistaken for final financial, legal, or underwriting advice.

Mitigation: Present outputs as informational guidance and have users confirm final decisions with qualified insurance or legal professionals.

## Reference(s):

- [Compliance guidance](artifact/references/compliance.md)
- [Insurance knowledge base](artifact/references/insurance-knowledge.md)
- [Product reference data](artifact/references/products.json)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, JSON]

**Output Format:** [Chinese Markdown responses with structured JSON from local calculation scripts when invoked]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled static product data; product availability, premiums, terms, and sales contacts should be independently verified.]

## Skill Version(s):

1.8.463 (source: server release evidence; artifact frontmatter lists 1.8.347)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
