## Description:

AI Insurance Advisor supports Mainland China insurance planning, product comparison, premium estimation, coverage-gap analysis, underwriting and compliance guidance, claims questions, sales copy, and agent training scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China and insurance agents use this skill to analyze household protection needs, compare insurance products, estimate premiums, design plans, answer insurance questions, and produce compliant sales or training language.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may ask for sensitive personal, financial, family, and health information during insurance planning.

Mitigation: Collect only information needed for the current planning task and avoid sharing it beyond the user's chosen insurance workflow.

Risk: Insurance product availability, premiums, and compliance details may be outdated because the product data is static.

Mitigation: Verify products, pricing, and policy terms with licensed professionals or official insurer materials before acting on recommendations.

Risk: One helper script showed a runtime data-shape error during security inspection.

Mitigation: Treat generated calculations and plans as advisory outputs and review them manually before using them with customers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance Knowledge Base](artifact/references/insurance-knowledge.md)
- [Compliance Reference](artifact/references/compliance.md)
- [Insurance Product Data](artifact/references/products.json)
- [Product Data Validation Report](artifact/references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese Markdown responses, with JSON outputs from local helper scripts when calculations or plan generation are invoked]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on static product data and should be verified against current insurer materials.]

## Skill Version(s):

1.8.458 (source: server release metadata; artifact frontmatter lists 1.8.351)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
