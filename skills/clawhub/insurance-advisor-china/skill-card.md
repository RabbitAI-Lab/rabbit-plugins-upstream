## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in the Chinese mainland insurance market use this skill to compare insurance products, estimate premiums, analyze protection gaps, design household insurance plans, and get general underwriting, compliance, and claims guidance. The skill is advisory and should not replace insurer quotes, licensed professional advice, or legal review.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may steer product recommendation flows toward one named insurance sales company.

Mitigation: Present any sales-contact information as a factual reference only, require comparison across multiple licensed channels, and avoid treating the named company as an endorsement.

Risk: The skill may request sensitive personal, financial, policy, and health-related details to produce insurance advice.

Mitigation: Collect only the minimum details needed for the analysis, avoid requesting credentials or full identity documents, and remind users to verify advice with licensed professionals.

Risk: Static product data, premiums, availability, and regulatory details can become stale.

Mitigation: Treat outputs as preliminary guidance and require users to confirm current product terms, premiums, underwriting decisions, and legal requirements with insurers or qualified advisors before purchase.

## Reference(s):

- [Insurance knowledge base](artifact/references/insurance-knowledge.md)
- [Regulatory compliance notes](artifact/references/compliance.md)
- [Insurance product database](artifact/references/products.json)
- [Product database analysis report](artifact/references/_repo_analysis_2026-08-21.md)
- [Insurance database analysis report](artifact/references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese advisory text with Markdown tables and JSON outputs from local analysis scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product comparisons, premium estimates, risk scores, coverage-gap analysis, plan options, compliance reminders, and product-data freshness disclaimers.]

## Skill Version(s):

2.0.128 (source: server release metadata; artifact frontmatter says 2.0.80)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
