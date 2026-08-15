## Description:

Helps QA teams create risk-based regression testing plans by selecting smoke, core, or full regression scope from change impact, risk, and time constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and release teams use this skill to choose an efficient regression scope, prioritize historical test cases, and expose uncovered release risk when time is constrained.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate during broad regression-testing discussions and inspect workspace files provided for planning.

Mitigation: Provide only the files or change descriptions needed for regression planning, and avoid unnecessary sensitive workspace inputs.

Risk: Regression plans may misclassify release risk or be used as an unsupported release blocker.

Mitigation: Have project managers and developers confirm risk ratings, release windows, and any blocking decisions before acting on the plan.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/kokxi/skills/qa-regression-testing)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown regression plan with selected test cases, risk-based priorities, execution strategy, time estimates, and uncovered-risk notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses original test case IDs where available and labels regression levels as smoke, core, or full.]

## Skill Version(s):

1.6.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
