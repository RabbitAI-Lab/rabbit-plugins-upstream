## Description:

Advises mainland China individuals and families on insurance needs analysis, product comparison, premium calculation, plan design, insurance knowledge, and compliance reminders using local references and Python calculators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use the skill to analyze household insurance needs, compare insurance products, estimate premiums, design coverage plans, and receive insurance knowledge or compliance reminders.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Regulated insurance recommendations may be mistaken for licensed legal, medical, or financial advice.

Mitigation: Present outputs as informational and require review by a qualified insurance or compliance professional before purchase, sales, or underwriting decisions.

Risk: The skill can steer users toward a specific sales company after recommendations, and server security evidence reports missing product referral verification metadata.

Mitigation: Treat referral and product claims as unverified until the products.json metadata is corrected, disclose the referral basis, and encourage users to compare providers.

Risk: Static product data and calculated premiums may be outdated or incomplete.

Mitigation: Confirm current product availability, policy terms, and premiums with the insurer or a licensed broker before decisions are made.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Product database](references/products.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with JSON output from local Python scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static product, knowledge, and compliance references; no network access or runtime persistence is declared.]

## Skill Version(s):

2.0.110 (source: ClawHub release evidence; artifact frontmatter is 2.0.90)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
