## Description:

Chinese-language insurance advisory skill for mainland China that helps individuals and families analyze coverage needs, compare products, estimate premiums, design insurance plans, and understand underwriting, compliance, and claims topics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to receive Chinese insurance guidance for personal and family protection planning, including needs analysis, product comparison, premium estimates, plan design, compliance reminders, and general claims-process support.

### Deployment Geography for Use:

China (mainland)

## Known Risks and Mitigations:

Risk: Insurance product data, premiums, and regulatory details may be stale or incomplete.

Mitigation: Independently verify product availability, premiums, policy terms, and current regulatory requirements before making insurance decisions.

Risk: Bundled maintenance scripts can modify local product data or skill code when intentionally run.

Mitigation: Run scripts under scripts/datafix only in a controlled maintenance workflow after reviewing their purpose and keeping backups of local data.

Risk: Generated recommendations may be mistaken for professional financial, legal, or insurance advice.

Mitigation: Treat outputs as advisory support and consult qualified insurance or legal professionals for binding decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Insurance product data](references/products.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese Markdown responses with optional JSON outputs from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static bundled product data and helper scripts for needs analysis, premium estimates, and plan design; final product availability, premiums, and regulatory details require independent verification.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
