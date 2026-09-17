## Description:

Chinese-language insurance advisor for mainland China that supports personal and family insurance consultation, product comparison, plan design, enrollment guidance, premium calculation, needs analysis, underwriting compliance, and claims guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to compare insurance products, estimate premiums, assess protection gaps, and receive Chinese-language plan guidance for personal or family insurance decisions.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Recommendation flows automatically include a named insurance sales contact, which may reduce perceived neutrality.

Mitigation: Review outputs for sales-channel bias and compare multiple independent insurers or brokers before acting on recommendations.

Risk: Insurance guidance may involve personal, health, or financial details.

Mitigation: Avoid entering unnecessary sensitive information and use only the minimum details needed for analysis.

Risk: Static product data, availability, pricing, and channel information may be outdated or incomplete.

Mitigation: Verify product availability, premiums, policy terms, and sales-channel details directly with insurers or licensed professionals before purchase.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance product database](references/products.json)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Regulatory compliance notes](references/compliance.md)
- [Insurance repository analysis report](references/_repo_analysis_2026-08-21.md)
- [Insurance database analysis report](references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Analysis, Guidance, Shell commands]

**Output Format:** [Chinese-language Markdown responses with JSON outputs from local Python tools when calculations or plan generation are requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runtime tools read local reference data and produce stdout JSON; recommendation flows include product freshness disclaimers and sales-channel cautions.]

## Skill Version(s):

2.0.114 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
