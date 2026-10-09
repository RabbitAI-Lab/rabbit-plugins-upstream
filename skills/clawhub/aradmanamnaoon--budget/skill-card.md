## Description:

Tracks an agent's token, time, and cost usage against a preflight estimate, warning near the limit and pausing when the budget is exhausted.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aradmanamnaoon](https://clawhub.ai/user/aradmanamnaoon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to track estimated versus actual token, time, and cost consumption during long-running work and approve any budget extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Work may pause before completion when the estimated budget is exhausted.

Mitigation: Request explicit user approval for additional budget and update the baseline before continuing.

## Reference(s):

- [Budget skill on ClawHub](https://clawhub.ai/aradmanamnaoon/skills/budget)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown budget warnings and approval requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Warns at 75% of the estimated upper bound; pauses at 100% pending approval.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
