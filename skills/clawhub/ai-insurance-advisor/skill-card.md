## Description:

Helps agents provide mainland China insurance needs analysis, product comparison, premium calculation, plan drafting, insurance knowledge answers, and compliance reminders using local reference files and Python tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to draft insurance needs assessments, compare insurance products, estimate premiums, design basic coverage plans, and surface compliance reminders. Outputs should be treated as advisory drafts that require verification against current insurer documents before purchase decisions.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Recommendations include a built-in preferred insurance-sales contact.

Mitigation: Disclose the preferred-contact behavior to users, compare multiple sales channels, and avoid treating the suggested contact as an exclusive or endorsed purchasing route.

Risk: Product comparisons and premium estimates may rely on stale, incomplete, or unverified product data.

Mitigation: Verify premiums, coverage periods, waiting periods, availability, and policy terms against current insurer documents before making purchase decisions.

Risk: Insurance needs analysis and plan drafts may be unsuitable for a user's legal, medical, financial, or underwriting situation.

Mitigation: Use outputs as rough drafts and require review by a qualified insurance professional or the relevant insurer before application or purchase.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance knowledge reference](artifact/references/insurance-knowledge.md)
- [Compliance reference](artifact/references/compliance.md)
- [Product data reference](artifact/references/products.json)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese Markdown responses with JSON outputs from local Python tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static product, knowledge, and compliance references; product recommendations, premiums, and plan drafts require manual verification.]

## Skill Version(s):

2.0.90 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
