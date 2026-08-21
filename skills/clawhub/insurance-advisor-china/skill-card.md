## Description:

A Mainland China AI insurance advisor for individuals and families that supports insurance consultation, product comparison, plan design, application guidance, premium calculation, needs analysis, underwriting compliance, and claims guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External consumers and families in Mainland China use this skill to assess insurance coverage needs, compare products, estimate premiums, design insurance plans, and receive general compliance and claims guidance in Chinese.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Generated insurance advice and premium estimates may be outdated or inaccurate because the skill uses bundled static product data.

Mitigation: Treat recommendations and premiums as informational and verify current product terms, prices, eligibility, and availability with insurers before making decisions.

Risk: Bundled maintenance scripts under scripts/datafix can modify local product data or skill source files if run intentionally.

Mitigation: Use the normal advisor calculators for runtime work and run datafix scripts only in a controlled maintenance workflow with backups.

Risk: Needs analysis can involve personal, financial, family, and health-related information.

Mitigation: Collect only the minimum information required for the user request and handle it under applicable privacy and data-protection requirements.

Risk: Compliance and claims guidance may be mistaken for professional legal, insurance, or financial advice.

Mitigation: Present the guidance as general information and direct users to licensed professionals or insurers for binding advice, underwriting decisions, claims handling, and legal interpretation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Product data reference](references/products.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese advisory responses with Markdown structure and JSON outputs from bundled local calculators]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled static product and reference data; generated premiums and recommendations are informational and require verification against current insurer terms.]

## Skill Version(s):

2.0.3 (source: ClawHub release metadata; artifact frontmatter: 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
