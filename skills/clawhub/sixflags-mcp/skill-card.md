## Description:

Helps plan a Six Flags or Cedar Fair park visit using public ride wait times, park hours, show schedules, and next-ride suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Park visitors and trip planners use this skill to check current ride waits, operating hours, and shows, then choose what to ride next at Six Flags and former Cedar Fair parks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad park questions may trigger live operations guidance when the user wants unrelated travel or ticketing advice.

Mitigation: Confirm whether the user wants current park operations data before using live results.

Risk: Off-hours ride status may show CLOSED with no wait, which can be mistaken for an operating-day closure.

Mitigation: Check park operating hours and parkOpen before interpreting closed ride statuses.

## Reference(s):

- [sixflags-mcp on ClawHub](https://clawhub.ai/chrischall/skills/sixflags-mcp)
- [ThemeParks.wiki](https://themeparks.wiki)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live park data may be unavailable outside operating hours.]

## Skill Version(s):

2.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
