## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China use this skill to obtain Chinese-language insurance needs analysis, product comparisons, premium estimates, plan design, compliance prompts, and claims guidance. Outputs are informational and should be verified with licensed insurance professionals or insurers before purchase.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Bundled maintenance scripts can modify local product data and source files if run.

Mitigation: Keep datafix scripts out of the user-facing workflow; run them only in a reviewed maintenance context with backups.

Risk: Insurance product availability, terms, and premiums can change quickly.

Mitigation: Treat recommendations and calculations as informational; verify active status, policy terms, and premiums with insurers or licensed insurance professionals before purchase.

## Reference(s):

- [Insurance-Advisor-China product library analysis](references/_repo_analysis_2026-08-21.md)
- [Regulatory compliance points](references/compliance.md)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Insurance products dataset](references/products.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese-language Markdown responses with optional JSON reports from local scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product freshness disclaimers, premium estimates, comparison tables, and risk or compliance guidance.]

## Skill Version(s):

2.0.5 (source: server release evidence; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
