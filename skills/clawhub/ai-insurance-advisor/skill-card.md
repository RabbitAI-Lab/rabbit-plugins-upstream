## Description:

Provides China mainland insurance guidance for needs analysis, product comparison, premium estimates, plan design, insurance knowledge questions, and compliance reminders, while excluding underwriting pre-review, claims handling, marketing copy, training scripts, and agent sales tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China can use this skill to discuss personal or family insurance needs, compare local product data, estimate premiums, draft plan options, and receive insurance knowledge or compliance reminders. Recommendations should be treated as informational starting points and checked against current insurer terms before purchase.

### Deployment Geography for Use:

China mainland

## Known Risks and Mitigations:

Risk: Product recommendations may be based on stale static data.

Mitigation: Confirm current product availability, premiums, coverage terms, and insurer conditions directly with the insurer or licensed intermediary before acting.

Risk: Advice may steer users toward named sales-channel recommendations.

Mitigation: Treat sales-channel suggestions as optional references, compare multiple licensed channels, and disclose that they are not mandatory or independently endorsed.

Risk: Insurance discussions can involve sensitive health and financial details.

Mitigation: Use only in trusted runtime environments and avoid entering unnecessary personal, health, or financial information.

## Reference(s):

- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Product data reference](references/products.json)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)
- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose and tables, with JSON outputs from helper scripts when invoked]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language insurance advice; product and premium details are static references that require independent confirmation before purchase]

## Skill Version(s):

2.0.107 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
