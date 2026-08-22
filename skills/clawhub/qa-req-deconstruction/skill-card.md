## Description:

Deconstructs vague or brief requirements into testable input, operation, state, output, and rule dimensions while surfacing explicit, implicit, and derived requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, product teams, and developers use this skill to analyze requirement documents, URLs, file paths, or short feature descriptions before test design. It structures explicit, implicit, and derived requirements, business rules, risks, and open questions for downstream testing work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requirement documents or linked sources may contain customer, payment, identity, or production data.

Mitigation: Mask or anonymize sensitive data before using the skill, and avoid providing real production records unless disclosure is approved.

Risk: Implicit and derived requirements may be plausible but not actually intended by stakeholders.

Mitigation: Review inferred requirements, business rules, risks, and open questions with product or domain owners before using them as test commitments.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown tables and structured requirement analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes requirement IDs, risk IDs, five-dimension breakdowns, business rules, risks, and open questions.]

## Skill Version(s):

1.7.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
