## Description:

AI Insurance Advisor is a Chinese-language mainland China insurance assistant for insurance configuration, plan design, product comparison, critical illness, medical, life, accident and savings insurance recommendations, premium calculation, coverage-gap analysis, underwriting and compliance guidance, claims support, social copy, training scripts, and agent business support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to analyze insurance needs, compare products, calculate indicative premiums, design insurance plans, and generate Chinese-language advisory, compliance, sales, and training content. It provides reference-only insurance guidance that should be checked against official insurer materials and licensed professional review.

### Deployment Geography for Use:

China Mainland

## Known Risks and Mitigations:

Risk: Insurance product availability, premiums, and compliance requirements can change after the static reference data was packaged.

Mitigation: Verify product availability, premiums, and compliance against official insurer materials or licensed professionals before acting.

Risk: Insurance advice workflows may invite users to share sensitive health, family, or financial details.

Mitigation: Collect and provide only the minimum personal information needed for the analysis and avoid sharing unnecessary health or financial details.

Risk: Generated recommendations and compliance notes are reference guidance, not licensed professional advice.

Mitigation: Treat outputs as decision support and have a qualified insurance, legal, or compliance professional review them before purchase or customer-facing use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Compliance reference](artifact/references/compliance.md)
- [Insurance knowledge base](artifact/references/insurance-knowledge.md)
- [Insurance product data](artifact/references/products.json)
- [Product data validation report](artifact/references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese Markdown responses with JSON from local Python calculators]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static local product data and local Python scripts; outputs require product, premium, and compliance verification before use.]

## Skill Version(s):

1.8.444 (source: server release metadata; artifact frontmatter reports 1.8.351)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
