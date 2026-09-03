## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in mainland China use this skill to assess insurance needs, compare products, estimate premiums, design coverage plans, and understand underwriting, compliance, and claims topics. Agents can use its local scripts and reference files to produce Chinese-language insurance guidance and structured JSON analyses.

### Deployment Geography for Use:

China (Mainland)

## Known Risks and Mitigations:

Risk: The skill may ask for sensitive personal, health, family, and financial details when preparing insurance guidance.

Mitigation: Collect only the information needed for the task, avoid storing it outside the current session, and handle it according to applicable privacy requirements.

Risk: Product data and premium calculations are static reference material and may not match current insurer terms or formal underwriting results.

Mitigation: Verify policy availability, terms, premiums, and eligibility with insurers or licensed insurance professionals before purchase decisions.

Risk: Local maintenance utilities can alter the product dataset if run deliberately.

Mitigation: Run maintenance scripts only in a controlled workspace after reviewing their purpose and keeping a backup of the source data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Regulatory compliance notes](references/compliance.md)
- [Product database](references/products.json)
- [Product database analysis report, 2026-08-21](references/_repo_analysis_2026-08-21.md)
- [Insurance database analysis report, 2026-08-26](references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese-language Markdown responses with optional JSON outputs from local analysis scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include insurance disclaimers, product recency warnings, premium estimates, product comparison tables, and plan recommendations.]

## Skill Version(s):

2.0.73 (source: server release evidence; artifact SKILL.md frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
