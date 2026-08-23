## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to analyze personal or family insurance needs, compare products, estimate premiums, design coverage plans, and get general underwriting, compliance, and claims guidance. It is intended as advisory support and should be checked against official insurer sources before purchase decisions.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The packaged maintenance scripts can modify the product database or local skill files.

Mitigation: Avoid running scripts under artifact/scripts/datafix unless you intentionally want to maintain or alter the packaged database; review changes before using updated outputs.

Risk: Insurance product recommendations and premium estimates may rely on static or stale product data.

Mitigation: Verify product availability, pricing, terms, and insurer disclosures against official sources before making purchase decisions.

Risk: The skill provides advisory insurance guidance that may not account for every user-specific legal, health, underwriting, or financial circumstance.

Mitigation: Use outputs as decision support and consult qualified insurance, legal, or financial professionals for binding advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge base](artifact/references/insurance-knowledge.md)
- [Regulatory compliance notes](artifact/references/compliance.md)
- [Insurance product database](artifact/references/products.json)
- [Product database analysis report](artifact/references/_repo_analysis_2026-08-21.md)
- [Insurance database analysis report DOCX](artifact/references/保险资料库分析报告_2026-08-21.docx)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Chinese-language Markdown guidance with JSON returned by helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static packaged insurance reference data and local Python helper scripts for needs analysis, premium calculation, and plan design.]

## Skill Version(s):

2.0.8 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
