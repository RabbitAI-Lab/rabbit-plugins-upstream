## Description:

A Mainland China insurance advisor that helps individuals and families with insurance consultation, product comparison, plan design, application guidance, premium calculation, needs analysis, underwriting compliance, and claims questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China use this skill to evaluate personal or family insurance needs, compare local insurance products, estimate premiums, design coverage plans, and receive Chinese-language guidance on underwriting, compliance, and claims workflows.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Static product data and premium calculations may be outdated or may include discontinued products.

Mitigation: Independently verify product availability, eligibility rules, and premiums with current insurer or official channel information before acting on recommendations.

Risk: Recommendations automatically display one specific insurance agency contact after product or plan recommendations.

Mitigation: Treat the contact as informational only, compare multiple qualified sales channels, and avoid presenting it as an endorsement or exclusive recommendation.

Risk: Needs analysis may involve sensitive age, family, income, existing-policy, and health-disclosure information.

Mitigation: Collect only necessary information, obtain appropriate consent, keep processing local where possible, and do not operationalize WeChat or PDF customer-data workflows without privacy, access-control, and channel approval.

## Reference(s):

- [Insurance Knowledge](references/insurance-knowledge.md)
- [Compliance Reference](references/compliance.md)
- [Insurance Product Database](references/products.json)
- [Insurance Product Database Analysis Report](references/保险资料库分析报告_2026-08-26.md)
- [Repository Product Library Analysis](references/_repo_analysis_2026-08-21.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, json, shell commands]

**Output Format:** [Chinese-language Markdown guidance with JSON results from local Python tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static product, knowledge, and compliance files; runtime tool outputs are written to stdout.]

## Skill Version(s):

2.0.108 (source: server release evidence; artifact frontmatter lists 2.0.80)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
