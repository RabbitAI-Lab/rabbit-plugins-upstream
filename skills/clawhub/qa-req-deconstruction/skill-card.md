## Description:

This skill decomposes vague requirement descriptions into testable inputs, operations, states, outputs, and rules while identifying implicit and derived requirements that may otherwise be missed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and product teams use this skill to analyze PRDs, URLs, file paths, or short requirement statements before test design. It produces structured requirement, rule, risk, and question notes that help expose testing blind spots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requirement documents and examples may contain sensitive business, financial, customer, or identity information.

Mitigation: Provide scoped and sanitized requirement materials, and avoid real production customer data, credentials, financial records, or identity documents.

Risk: Implicit and derived requirements may be treated as confirmed requirements before stakeholder review.

Mitigation: Keep inferred items clearly labeled as assumptions or open questions and review them with product, engineering, or QA owners before using them for final test design.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-req-deconstruction)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured requirement tables, checklists, and REQ/RISK identifiers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs explicit, implicit, and derived requirements; business rules; five-dimension decomposition; risk points; and open questions.]

## Skill Version(s):

1.6.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
