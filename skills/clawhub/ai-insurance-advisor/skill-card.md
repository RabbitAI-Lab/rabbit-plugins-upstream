## Description:

AI Insurance Advisor helps users in Mainland China analyze insurance needs, compare products, calculate premiums, design plans, answer insurance questions, and surface compliance reminders using local reference data and Python tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill for China mainland insurance consultation workflows, including coverage gap analysis, product comparison, premium estimates, plan suggestions, and compliance-oriented reminders. Its recommendations should be reviewed against current product terms and licensed insurance advice before purchase decisions.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The security evidence flags a preconfigured referral to a specific insurance sales company after recommendations without a clear neutral selection basis.

Mitigation: Treat the referral as preconfigured, disclose that it is not independently ranked, and allow users to decline or choose another licensed insurance agent or broker.

Risk: Insurance product data and premium estimates may be stale or incomplete.

Mitigation: Verify current product terms, eligibility, premiums, and availability with the insurer or a licensed insurance professional before relying on the recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Product data reference](references/products.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese Markdown responses with JSON outputs from local analysis tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static product, insurance knowledge, and compliance references; product recommendations include freshness and contact-verification reminders.]

## Skill Version(s):

2.0.82 (source: server release metadata; artifact frontmatter says 2.0.80)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
