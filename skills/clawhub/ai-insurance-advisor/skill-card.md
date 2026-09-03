## Description:

AI Insurance Advisor is a mainland China insurance assistant for coverage planning, product comparison, critical illness, medical, life, accident, and savings insurance recommendations, premium estimates, coverage gap analysis, underwriting, claims, marketing copy, and agent training support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to evaluate insurance needs, compare products, estimate premiums, design coverage plans, understand insurance and compliance concepts, and generate Chinese sales or training copy.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may handle sensitive insurance-planning details, including income, family obligations, existing coverage, budget, and health-disclosure context.

Mitigation: Collect only the information needed for the request, avoid sharing it outside the conversation, and follow the skill's customer information protection guidance.

Risk: Product data and premium estimates are static and may be outdated or approximate.

Mitigation: Treat outputs as planning guidance and verify current product terms, premiums, eligibility, and availability with licensed professionals or insurers before purchase.

Risk: Insurance recommendations, compliance notes, and claims guidance can be mistaken for professional financial or legal advice.

Mitigation: Present results as decision support, disclose limits clearly, and direct users to licensed insurance or legal professionals for binding advice.

Risk: The skill may offer a named sales-company contact when a user asks for a referral.

Mitigation: Make any referral optional, respect refusal, and encourage users to compare licensed multi-company brokers or agents before acting.

## Reference(s):

- [Compliance Reference](references/compliance.md)
- [Insurance Knowledge Reference](references/insurance-knowledge.md)
- [Insurance Product Data](references/products.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese Markdown with structured JSON outputs from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-facing outputs are in Chinese; product recommendations include freshness notices and advice to verify product details with insurers or licensed professionals.]

## Skill Version(s):

2.0.73 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
