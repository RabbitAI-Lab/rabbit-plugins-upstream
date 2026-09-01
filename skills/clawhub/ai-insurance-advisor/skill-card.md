## Description:

Provides Chinese-language insurance guidance for mainland China, including coverage planning, product comparison, premium estimation, needs analysis, underwriting and compliance prompts, claims support, marketing copy, and agent training scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External consumers, families, and insurance agents in mainland China use this skill to evaluate coverage needs, compare insurance products, estimate premiums, design insurance plans, and produce compliant Chinese-language insurance explanations or sales support materials.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may ask for age, family, income, budget, existing coverage, and health-related insurance details.

Mitigation: Collect only information needed for the user's request, obtain consent, avoid unnecessary retention or sharing, and follow applicable personal information protection requirements.

Risk: Insurance product availability, premiums, and terms may change after the static product data was published.

Mitigation: Verify product availability, premium calculations, coverage terms, and suitability with the insurer or a licensed insurance professional before a purchase decision.

Risk: Insurance recommendations and compliance explanations may be incomplete or unsuitable for a specific customer's facts.

Mitigation: Treat outputs as planning support and require review by a licensed professional; do not rely on the skill as a substitute for legal, regulatory, underwriting, or financial advice.

Risk: The skill can offer a specific insurance sales contact after recommendations.

Mitigation: Disclose that the contact is sales-related, ask whether the user wants contact information, respect declines, and encourage comparison across multi-company insurance agencies or brokers.

## Reference(s):

- [Insurance Knowledge Reference](references/insurance-knowledge.md)
- [Regulatory Compliance Reference](references/compliance.md)
- [Insurance Product Dataset](references/products.json)
- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands]

**Output Format:** [Chinese Markdown guidance with optional JSON output from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static reference data; product availability, premiums, and compliance details require current professional verification.]

## Skill Version(s):

2.0.69 (source: server release metadata; artifact frontmatter says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
