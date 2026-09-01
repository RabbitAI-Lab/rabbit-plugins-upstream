## Description:

This skill helps QA practitioners turn completed requirement, scenario, boundary, and combination analysis into prioritized, traceable test cases with coverage guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and test leads use this skill after upstream analysis is complete to design or review structured test cases for feature requirements, coverage gaps, and priority planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate too broadly during general QA discussions.

Mitigation: Clarify whether the user wants formal test-case generation before producing a structured test-case report.

Risk: Incomplete requirements or missing upstream analysis can lead to generic or misleading test cases.

Mitigation: Provide requirement details, scenario analysis, boundary conditions, and business context; label assumptions and coverage gaps when inputs are incomplete.

Risk: Generated execution steps may not match the target system implementation.

Mitigation: Keep test steps blank for the user to complete against the actual system, while generating preconditions and objective expected results.

Risk: Coverage claims can be overstated when based on partial input.

Mitigation: State the coverage basis, avoid absolute full-coverage claims, and mark missing modules with the reason they are not covered.

## Reference(s):

- [Design Methods](references/design-methods.md)
- [Coverage and Quality](references/coverage-and-quality.md)
- [Output Template Full](references/output-template-full.md)
- [Review Standards](references/review-standards.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown test-case reports, tables, coverage notes, and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces P0-P3 priorities, traceability IDs, objective expected results, coverage notes, and blank test steps for user completion.]

## Skill Version(s):

1.7.5 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
