## Description:

Systematically reviews requirement documents across completeness, clarity, consistency, testability, and feasibility, producing scored findings and improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, product teams, and developers use this skill to review PRDs or requirement descriptions before test design. It identifies gaps, ambiguity, contradictions, weak acceptance criteria, and feasibility concerns, then reports prioritized fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt requirement-quality review whenever a testing task involves requirement documents, even when the user did not explicitly ask for a requirement review.

Mitigation: Install it only when that workflow is desired, or narrow the trigger wording so it activates only for explicit requirement-review requests.

## Reference(s):

- [Review report template](references/report-template.md)
- [Five-dimension review standards](references/review-standards.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown review report with scoring tables, prioritized issue lists, and improvement recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes traceable requirement review identifiers, five-dimension scores, P0/P1/P2 issue severity, and coverage caveats.]

## Skill Version(s):

1.7.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
