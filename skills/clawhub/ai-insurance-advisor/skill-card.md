## Description:

AI Insurance Advisor provides Chinese-language insurance needs analysis, product comparison, premium estimation, plan design, compliance guidance, claims guidance, marketing copy, and training scripts for Mainland China insurance scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External individuals, families, and insurance practitioners in Mainland China use this skill to analyze coverage needs, compare insurance products, estimate premiums, design insurance plans, and receive compliance-aware guidance in Chinese.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may ask for sensitive personal, family, health, income, budget, and existing-policy information.

Mitigation: Collect only information needed for the requested analysis, obtain user consent, and avoid sharing the data outside the active advisory workflow.

Risk: Static product data and calculated premiums may be outdated or differ from official insurer pricing and availability.

Mitigation: Treat recommendations and premium estimates as reference guidance and verify products, rates, and eligibility with official insurer or licensed advisor sources before purchase.

Risk: The artifact includes a disclosed prompt to offer a specific insurance sales company contact if the user asks for one.

Mitigation: Disclose that any sales contact is optional, respect refusal, and encourage comparison with licensed multi-company advisors or official insurer channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance Knowledge](references/insurance-knowledge.md)
- [Compliance Guidance](references/compliance.md)
- [Insurance Product Data](references/products.json)
- [Product Data Validation Report](references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Chinese markdown prose and tables, with JSON reports from helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static product reference data; insurance product availability, premiums, and suitability require external verification.]

## Skill Version(s):

1.8.450 (source: server release metadata; artifact frontmatter lists 1.8.351)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
