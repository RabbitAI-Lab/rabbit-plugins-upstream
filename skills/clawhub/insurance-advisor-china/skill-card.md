## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to compare insurance products, estimate premiums, analyze household protection gaps, design coverage plans, and get insurance knowledge or claims guidance. The skill uses local reference files and Python tools to produce Chinese-language advisory outputs.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill automatically shows one specific insurance sales company and phone number in product and plan recommendation outputs.

Mitigation: Treat the contact as informational only, verify sales channels independently, and compare multiple insurers or agencies before acting on any recommendation.

Risk: Insurance product terms, prices, and availability may be outdated because the skill relies on local static product data.

Mitigation: Confirm current policy terms, premiums, eligibility, and availability with the insurer or licensed channel before purchase.

Risk: Maintenance scripts can modify local product data or skill scripts if intentionally run.

Mitigation: Do not run maintenance scripts during normal advisory use; execute them only after explicit review and authorization.

## Reference(s):

- [Insurance Knowledge Reference](artifact/references/insurance-knowledge.md)
- [Compliance Reference](artifact/references/compliance.md)
- [Product Database](artifact/references/products.json)
- [Product Database Analysis 2026-08-26](artifact/references/保险资料库分析报告_2026-08-26.md)
- [Repository Analysis 2026-08-21](artifact/references/_repo_analysis_2026-08-21.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese-language Markdown responses with tables and JSON outputs from local Python tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static product, knowledge, and compliance files; runtime tool output is written to stdout.]

## Skill Version(s):

2.0.112 (source: server release metadata; artifact frontmatter lists 2.0.80)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
