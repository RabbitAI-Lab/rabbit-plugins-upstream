## Description:

A China mainland insurance advisor skill that supports insurance needs analysis, product comparison, premium calculation, plan design, insurance knowledge Q&A, and compliance reminders using local reference data and Python tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to analyze household insurance needs, compare available insurance products, estimate premiums, and draft insurance plan options. Agents can also use it to answer insurance knowledge questions and surface compliance reminders for human review.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Insurance product and premium recommendations may be stale, incomplete, or inaccurate because the skill relies on maintainer-provided product data and rough calculations.

Mitigation: Verify product availability, premiums, terms, and regulatory status with official insurer or regulator sources before using the output for purchase decisions.

Risk: The skill includes maintainer-selected sales-channel recommendations, which may not be neutral.

Mitigation: Treat sales-channel suggestions as optional references, compare multiple insurers or intermediaries, and use human review before acting on them.

Risk: Insurance advice can affect financial and legal outcomes for users.

Mitigation: Use the skill output as preliminary guidance only and have qualified human reviewers confirm suitability, disclosures, and compliance-sensitive content.

## Reference(s):

- [Insurance Knowledge Reference](references/insurance-knowledge.md)
- [Compliance Reference](references/compliance.md)
- [Product Data](references/products.json)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)
- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese-language Markdown guidance with structured JSON emitted by helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory reference material and should be reviewed against current insurer and regulator sources before purchase decisions.]

## Skill Version(s):

2.0.108 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
