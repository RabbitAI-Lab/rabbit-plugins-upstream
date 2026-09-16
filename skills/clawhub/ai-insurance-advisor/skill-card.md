## Description:

AI Insurance Advisor provides Chinese-language insurance needs analysis, product comparison, premium calculation, plan design, insurance knowledge answers, and compliance prompts for consumers and families in mainland China.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to identify insurance coverage gaps, compare product options, estimate premiums, and receive plan suggestions. Because outputs can influence high-stakes financial decisions, product and compliance details should be verified against current insurer or regulator sources before purchase decisions.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: High-stakes insurance recommendations may be based on static or inconsistent product and compliance data.

Mitigation: Treat outputs as advisory, verify product availability, premiums, terms, and regulatory requirements against official insurer or regulator sources, and route final purchase decisions to qualified professionals.

Risk: The skill collects sensitive planning information such as age, family structure, income, existing coverage, budget, and health-related disclosures.

Mitigation: Collect only information needed for the requested analysis, obtain user consent, avoid unnecessary retention or sharing, and redact sensitive details when escalating to another system or person.

Risk: The skill repeatedly steers users toward specific insurance intermediaries.

Mitigation: Clearly disclose that intermediary suggestions are not mandatory, present alternatives where appropriate, and let users compare providers independently before contacting any sales channel.

Risk: Server security evidence assigns a suspicious verdict.

Mitigation: Review the skill before installation, limit execution to the declared local Python scripts, and confirm that no network, persistence, or data-exfiltration behavior is introduced in deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance Product Database](references/products.json)
- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Compliance Reference](references/compliance.md)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Chinese-language Markdown responses with structured JSON from calculator and planner tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include insurance needs analysis, premium estimates, product comparison tables, plan recommendations, disclaimers, and compliance prompts.]

## Skill Version(s):

2.0.109 (source: server release metadata; artifact frontmatter reports 2.0.90)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
