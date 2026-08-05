## Description:

A China-mainland insurance assistant that helps users analyze coverage needs, compare products, calculate premiums, design insurance plans, answer insurance questions, provide compliance reminders, and draft sales or training copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to explore personal or family insurance needs, compare insurance products, estimate premiums, and generate Chinese-language planning, compliance, sales, and training guidance.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Insurance recommendations may be incomplete, unsuitable, or mistaken if treated as final financial or legal advice.

Mitigation: Use outputs as a starting point and verify plans with an insurer, licensed broker, or qualified professional before purchase.

Risk: Bundled product data is static and may be outdated, unavailable, or different from current insurer terms.

Mitigation: Verify prices, availability, policy terms, and licensing directly with the insurer or a licensed broker before relying on recommendations.

Risk: Needs analysis may involve sensitive health, family, income, mortgage, and existing-policy details.

Mitigation: Share only the personal information needed for the specific analysis and avoid unnecessary identifiers.

Risk: The skill may provide a specific insurance sales-company contact when asked for contact information.

Mitigation: Independently confirm the contact, licensing, and suitability of any sales channel, and compare multi-company options.

## Reference(s):

- [Insurance product data](references/products.json)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Regulatory compliance notes](references/compliance.md)
- [Product data validation report](references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese Markdown responses and JSON from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local scripts read bundled product data for needs analysis, premium calculation, and plan design.]

## Skill Version(s):

1.8.434 (source: server release metadata; artifact frontmatter reports 1.8.351)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
