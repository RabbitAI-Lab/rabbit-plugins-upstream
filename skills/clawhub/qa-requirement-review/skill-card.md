## Description:

Reviews PRDs and requirement documents across completeness, clarity, consistency, testability, and feasibility, then produces a structured quality report with scores, issues, and improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and product teams use this skill to assess requirement quality before test design or implementation. It helps identify ambiguous, conflicting, incomplete, untestable, or infeasible requirements and suggests concrete improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be selected for a testing task when the immediate need is test design rather than requirement quality review.

Mitigation: Confirm the user's scope before applying the review checklist, especially when the request mentions requirements as context for testing.

Risk: A structured requirement review can produce misleading recommendations if the supplied PRD or business context is incomplete.

Mitigation: Ask for missing requirement details, business goals, acceptance criteria, or constraints before finalizing high-priority findings.

## Reference(s):

- [Report template](references/report-template.md)
- [Five-dimensional review standards](references/review-standards.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured Markdown requirement review report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes five-dimensional scores, prioritized P0-P2 issue lists, traceability IDs, and improvement suggestions.]

## Skill Version(s):

1.6.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
