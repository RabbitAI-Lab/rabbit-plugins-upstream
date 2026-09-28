## Description:

Generates traceable test cases from requirements through a structured QA workflow covering functional, boundary, combination, and regression testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA teams and developers use this skill to turn requirement documents or URLs into reviewed, traceable test cases and coverage reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may read linked files or directories and fetch URLs without a separate confirmation or defined path and network limits.

Mitigation: Use a scoped workspace with only intended requirements; avoid broad directories, absolute paths, secret-bearing project roots, and sensitive or internal URLs unless their contents are intended for analysis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/kokxi/skills/qa-test-skills)
- [Output formats and checks](artifact/references/format.md)
- [Input routing and document formats](artifact/references/routing.md)
- [Workflow details](artifact/references/workflow-detail.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV files, Guidance]

**Output Format:** [Markdown reports and UTF-8 CSV test cases]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Test cases include identifiers, steps, expected results, and risk levels; reports describe coverage and requirement gaps.]

## Skill Version(s):

1.7.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
