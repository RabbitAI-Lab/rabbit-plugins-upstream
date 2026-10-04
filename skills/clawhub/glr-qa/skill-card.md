## Description:

Run goal-driven GameLearningRuntime QA against an authorized game, training adapter, replay, or live probe and produce dated JSON and HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and game QA teams use this skill to run bounded checks on authorized GameLearningRuntime projects and review evidence of bugs, regressions, training behavior, and live-test gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: QA commands may run against projects or games outside the user's authorization.

Mitigation: Confirm the project and permission first; use only explicitly bounded checks on controlled environments.

Risk: QA reports and logs may disclose proprietary project details or secrets when shared.

Mitigation: Review and redact generated reports before sharing; publish only owner-authorized evidence.

Risk: Passing smoke tests or synthetic checks could be mistaken for full game quality or live acceptance.

Mitigation: Report each evidence scope separately and label untested live behavior as an evidence gap.

## Reference(s):

- [GLR QA on ClawHub](https://clawhub.ai/loonghao/skills/glr-qa)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and dated JSON and self-contained HTML QA reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish deterministic checks, training evidence, and missing live acceptance.]

## Skill Version(s):

0.25.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
