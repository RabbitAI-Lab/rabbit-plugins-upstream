## Description:

A Mainland China insurance assistant for insurance planning, product comparison, premium calculation, coverage-gap analysis, underwriting and compliance prompts, claims questions, sales copy, and agent training scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China use this skill to receive Chinese-language insurance needs analysis, product comparisons, premium estimates, plan options, compliance reminders, social copy, and insurance sales training scripts. It can also support insurance agents preparing customer-facing explanations, subject to verification against current insurer and regulatory sources.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill asks for sensitive personal financial and health-adjacent insurance information.

Mitigation: Collect only information needed for the immediate insurance question, avoid retaining or sharing customer details, and obtain clear user consent before using personal data.

Risk: The skill can influence insurance purchase decisions through product comparisons, plan recommendations, and premium estimates.

Mitigation: Treat outputs as decision support only; verify product terms, underwriting eligibility, and quotes with insurers or licensed professionals before purchase.

Risk: Product data and premium calculations are local reference material and may be stale or approximate.

Mitigation: Use the included product-validity disclaimer and manually check high-value or recommended products against current insurer materials before relying on them.

Risk: The artifact instructs the agent to offer a specific insurance sales-company contact after recommendations.

Mitigation: Disclose that contact suggestions are optional, preserve the user's choice to decline, and compare options across multiple licensed insurance sales channels when appropriate.

## Reference(s):

- [Compliance Reference](references/compliance.md)
- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Insurance Product Dataset](references/products.json)
- [Product Data Validation Report](references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese-language Markdown responses with JSON outputs from local helper scripts when calculations or plan generation are requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes insurance disclaimers, product-comparison tables, premium estimates, coverage-gap reports, plan options, compliance reminders, and sales or training copy.]

## Skill Version(s):

1.8.454 (source: server release evidence; artifact frontmatter reports 1.8.351)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
