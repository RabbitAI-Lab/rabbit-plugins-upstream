## Description:

This skill helps QA and engineering teams create risk-based regression test plans, selected test case lists, priorities, and execution strategies from a change scope, historical test cases, optional risk assessment, and time constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test leads, and developers use this skill to choose smoke, core, or full regression scope after a release, code change, or time-boxed testing request. It is intended to turn change impact, risk level, and historical test cases into a practical regression plan with explicit uncovered-risk notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad regression-testing phrases may activate the skill without enough project context, leading to incomplete or poorly scoped regression recommendations.

Mitigation: Provide a concrete change scope, relevant historical test cases, risk assessment when available, and any time constraints before using the plan for release decisions.

Risk: Regression plans can affect release blocking or prioritization decisions if treated as final authority.

Mitigation: Review the proposed scope and risk levels with QA, development, and project stakeholders before blocking or approving a release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-regression-testing)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Configuration]

**Output Format:** [Markdown with regression plan sections and test case tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include regression scope, selected cases, risk-based priority, execution strategy, time estimates, and uncovered-risk notes.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
