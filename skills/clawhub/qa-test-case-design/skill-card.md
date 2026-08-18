## Description:

This skill helps QA practitioners turn completed requirements, scenario, boundary, and combination analysis into structured, prioritized, traceable test cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, testers, and product teams use this skill to convert finished requirements analysis into P0-P3 test case sets with coverage notes, traceability, and review guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for many test-case-related requests and could be used before requirements analysis is complete.

Mitigation: Use it after requirements, scenarios, boundaries, and combinations have been analyzed, and provide that prior analysis as input.

Risk: Generated test cases can be incomplete or mismatched to the actual system if the user supplies limited requirements.

Mitigation: Review the generated cases against product requirements, fill in system-specific execution steps, and validate coverage before operational use.

## Reference(s):

- [Design Methods](references/design-methods.md)
- [Coverage and Quality](references/coverage-and-quality.md)
- [Review Standards](references/review-standards.md)
- [Output Template Full](references/output-template-full.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown test case templates and QA review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prioritized P0-P3 test cases with traceability fields, coverage notes, risk reminders, and user-completed execution steps.]

## Skill Version(s):

1.7.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
