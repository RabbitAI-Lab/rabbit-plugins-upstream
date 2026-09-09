## Description:

China-mainland insurance advisor skill for needs analysis, product comparison, premium calculation, plan design, insurance knowledge Q&A, and compliance reminders using local reference files and Python calculation scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to analyze insurance needs, compare products, estimate premiums, design basic insurance plans, and receive insurance knowledge or compliance reminders. It is not a substitute for insurer underwriting, legal advice, claims handling, or licensed financial advice.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Specific sales-channel recommendations may make product or plan advice promotional rather than neutral.

Mitigation: Tell users when company mentions are promotional, compare multiple providers, and avoid presenting any sales channel as the only appropriate option.

Risk: Product data and verification basis may be incomplete or stale for financial decisions.

Mitigation: Ask users to verify current product terms, premiums, eligibility, and licensing directly with insurers or licensed professionals before acting.

Risk: Insurance, legal, underwriting, and claims outcomes depend on individual facts and official insurer review.

Mitigation: Keep outputs framed as informational guidance and route underwriting, claims, legal, or final purchase decisions to qualified human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [insurance-knowledge.md](references/insurance-knowledge.md)
- [compliance.md](references/compliance.md)
- [products.json](references/products.json)
- [National Financial Regulatory Administration insurance intermediary information disclosure platform](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with optional JSON output from local Python scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured needs analysis, product comparison tables, premium estimates, plan recommendations, disclaimers, and compliance reminders.]

## Skill Version(s):

2.0.88 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
