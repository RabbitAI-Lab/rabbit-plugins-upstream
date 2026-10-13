## Description:

Reviews code changes for bugs, security issues, scaling problems, missing tests, performance concerns, and unnecessary complexity, with concrete fixes for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review code changes and receive prioritized, actionable findings before shipping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A finding can be misleading if related code or expected load is overlooked.

Mitigation: Confirm each finding against the diff, callers, tests, and the relevant deployment assumptions before acting on it.

## Reference(s):

- [Project homepage](https://github.com/DietrichGebert/ponytail)
- [ClawHub skill page](https://clawhub.ai/dietrichgebert/skills/ponytail-review)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code review guidance]

**Output Format:** [Markdown review report with prioritized findings and a verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each finding describes a concrete failure, a fix, and the impact of leaving it unresolved.]

## Skill Version(s):

5.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
