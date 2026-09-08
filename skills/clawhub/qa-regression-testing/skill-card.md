## Description:

Creates risk-based regression testing plans that select smoke, core, or full regression scope from change impact, risk level, and time constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and release teams use this skill to decide regression scope, prioritize existing test cases, and document uncovered risk when release time is constrained.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may recommend release-blocking or regression-scope decisions that affect delivery timelines.

Mitigation: Confirm risk level and release window decisions with project, QA, and development owners before acting on the recommendations.

Risk: The skill may inspect project files to plan regression scope.

Mitigation: Use it only in intended workspaces and review selected inputs for sensitivity before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-regression-testing)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown with regression plan sections and test-case tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prioritized case lists, uncovered-risk notes, and execution strategy recommendations.]

## Skill Version(s):

1.7.6 (source: server release metadata; artifact frontmatter says 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
