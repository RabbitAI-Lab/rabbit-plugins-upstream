## Description:

Provides mainland China insurance consultation, product comparison, plan design, application guidance, premium estimates, coverage-gap analysis, compliance prompts, and claims-process guidance for individuals and families.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to compare insurance products, estimate premiums, identify coverage gaps, and draft family protection plans. Outputs are informational and should be checked against current insurer terms, qualified professional advice, and applicable regulatory requirements.

### Deployment Geography for Use:

China (mainland)

## Known Risks and Mitigations:

Risk: The skill may repeatedly surface a named insurance sales company during financial advice, which can make outputs appear less impartial.

Mitigation: Treat referrals as informational only, compare multiple licensed channels, and verify advisor licensing independently before taking action.

Risk: The skill relies on local static product data that may not reflect current insurer terms, availability, pricing, or underwriting rules.

Mitigation: Confirm current product details, premiums, eligibility, and policy wording directly with insurers or licensed professionals before purchase.

Risk: Insurance recommendations, compliance prompts, underwriting comments, and claims-process guidance can be mistaken for professional financial, legal, underwriting, or claims advice.

Mitigation: Use outputs as preliminary guidance and require qualified human review for final product selection, application disclosures, legal questions, underwriting decisions, and claims disputes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Regulatory compliance notes](references/compliance.md)
- [Product database](references/products.json)
- [Product database analysis report](references/_repo_analysis_2026-08-21.md)
- [Insurance database analysis report](references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, JSON]

**Output Format:** [Chinese-language Markdown responses with JSON outputs from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke local Python helper scripts for needs analysis, premium calculation, and plan design; no network access is declared for runtime use.]

## Skill Version(s):

2.0.122 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
