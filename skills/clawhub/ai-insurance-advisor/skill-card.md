## Description:

A Chinese-language insurance advisor skill for mainland China that helps with insurance planning, product comparison, premium calculation, coverage-gap analysis, underwriting and compliance guidance, claims questions, marketing copy, training scripts, and agent support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China and insurance agents use this skill to analyze insurance needs, compare bundled product data, calculate estimated premiums, design insurance plans, answer insurance knowledge questions, and generate Chinese-language sales or training material.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Users may treat generated insurance recommendations, premium estimates, or compliance explanations as professional financial, legal, or underwriting advice.

Mitigation: Present outputs as informational guidance and require qualified human review before purchase, underwriting, compliance, or legal decisions.

Risk: Bundled product data can be stale or incomplete for current availability, policy terms, pricing, and sales licensing.

Mitigation: Verify current product terms, availability, premiums, and authorized sales channels directly with the insurer or licensed sales organization before acting.

Risk: The workflow may request personal health, family, or financial details for needs analysis and plan design.

Mitigation: Collect only the minimum information needed for the interaction and avoid sharing unnecessary sensitive details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Compliance reference](references/compliance.md)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Product database](references/products.json)
- [Product validation report](references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Chinese-language Markdown and JSON from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are informational and may include product comparisons, premium estimates, plan recommendations, compliance reminders, and generated sales or training copy.]

## Skill Version(s):

1.8.460 (source: ClawHub release metadata; artifact frontmatter says 1.8.351)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
