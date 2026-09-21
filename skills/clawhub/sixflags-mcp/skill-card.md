## Description:

Plans visits to Six Flags and Cedar Fair parks with live ride waits, park hours, show schedules, attraction lists, and next-ride suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to plan visits to Six Flags and Cedar Fair parks with current waits, schedules, attraction lists, and next-ride suggestions. It is useful for day-of park planning when public live park data is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad park-name questions where the user did not intend live Six Flags or Cedar Fair planning.

Mitigation: Review whether the trigger scope matches the deployment environment and ask a clarifying question when the park intent is ambiguous.

Risk: Wait times and show schedules can be unavailable or misleading outside operating hours.

Mitigation: Check park operating status and schedule before treating closed or missing wait data as a real-time park condition.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/sixflags-mcp)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
