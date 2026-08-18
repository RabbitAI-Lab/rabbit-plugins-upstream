## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in Mainland China use this skill to analyze insurance needs, compare products, estimate premiums, design protection plans, and understand underwriting, compliance, and claims guidance. It produces Chinese-language advisory outputs grounded in bundled local reference files and calculator scripts.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill asks for financial, family, and health-related details to generate insurance suggestions.

Mitigation: Share only the personal information needed for the task and avoid entering unnecessary sensitive details.

Risk: Bundled product and premium data may not reflect current insurance terms or availability.

Mitigation: Verify current product terms, premiums, and eligibility with official or licensed insurance channels before making decisions.

Risk: Insurance recommendations, compliance explanations, and claims guidance may be incomplete for a user's specific circumstances.

Mitigation: Treat outputs as informational support and not as a substitute for professional insurance, legal, or medical advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [compliance.md](artifact/references/compliance.md)
- [insurance-knowledge.md](artifact/references/insurance-knowledge.md)
- [products.json](artifact/references/products.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Chinese-language Markdown with optional JSON outputs from bundled calculator scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local bundled references and calculators; product and premium information should be verified with official or licensed channels before decisions.]

## Skill Version(s):

1.8.465 (source: server release metadata; artifact frontmatter reports 1.8.347)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
