## Description:

Use when comparing where to live based on commute, evaluating a hybrid work schedule, deciding if a new job's longer commute is worth it, calculating the true annual cost of driving to work, or planning which weekdays to go into the office; computes rush-hour travel times by weekday, prices commute modes in hours and dollars, optimizes hybrid office-day schedules, and shows lifespan and multi-year costs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to compare housing, job, commute-mode, and hybrid-office choices by annualizing route time, direct costs, and multi-year tradeoffs. It is best suited for planning decisions based on known route facts, not live traffic routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commute estimates can mislead if treated as live routing or precise traffic prediction.

Mitigation: Use observed route facts, review the editable assumptions for local traffic and costs, and treat the outputs as planning estimates.

Risk: Default cost and traffic assumptions may not match a specific city, employer schedule, or commute mode.

Mitigation: Adjust the local script parameters before relying on comparisons for housing, job, or return-to-office decisions.

## Reference(s):

- [Commute Cost Model](references/commute-model.md)
- [Server-resolved GitHub provenance](https://github.com/voronindenis5/commute-time-optimizer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local planning estimates from user-provided commute assumptions; no network access or credential use was found in the security evidence.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
