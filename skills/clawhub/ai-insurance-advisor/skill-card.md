## Description:

Chinese-language insurance assistant for mainland China that supports insurance planning, product comparison, premium calculation, coverage-gap analysis, underwriting and compliance guidance, claims questions, social copy, training scripts, and insurance-agent sales support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and insurance agents use this skill to analyze insurance needs, compare mainland China insurance products, estimate premiums, draft coverage plans, and produce Chinese-language insurance guidance or sales-support materials.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may ask for sensitive personal, family, health, and financial details when generating insurance recommendations.

Mitigation: Collect only the information needed for the task, avoid unnecessary personal identifiers, and handle any provided data as sensitive.

Risk: Insurance products, premiums, availability, and policy terms may differ from the static product database.

Mitigation: Verify prices, availability, coverage terms, and product status with the insurer or a qualified insurance professional before making decisions.

Risk: Insurance recommendations and compliance explanations may be incomplete or unsuitable for a user's specific circumstances.

Mitigation: Treat outputs as planning support, review official policy documents, and consult licensed insurance or legal professionals for binding decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Compliance guidance](references/compliance.md)
- [Product database](references/products.json)
- [Product data validation report](references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese Markdown responses with JSON outputs from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static product and reference data; product availability, prices, policy terms, and sales contacts require independent verification.]

## Skill Version(s):

2.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
