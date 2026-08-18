## Description:

Plans risk-based regression testing scope, case selection, priority, and execution strategy from change scope, risk level, and time constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and release teams use this skill to decide whether to run smoke, core, incremental, or full regression testing and to identify selected cases, priorities, execution timing, and uncovered risk areas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Regression plans may be treated as release-blocking decisions without enough business or engineering context.

Mitigation: Confirm risk level, release window, and blocking decisions with the project owner and development team before acting.

Risk: The skill may read workspace files relevant to changes, diffs, or test cases while preparing advisory guidance.

Mitigation: Use it in an appropriate workspace and review which project materials are available to the agent.

Risk: Time-boxed or differential regression can leave important areas untested.

Mitigation: Document uncovered risk areas explicitly and escalate to broader core or full regression when risk is high.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-regression-testing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown regression plan with selected cases, priorities, execution strategy, time estimates, and uncovered risk notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses original test case IDs when available and labels cases by smoke, core, or full regression level.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
