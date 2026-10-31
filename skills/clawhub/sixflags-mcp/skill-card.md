## Description:

Plan a day at a Six Flags theme park with live ride wait times, park hours, show schedules, and next-ride suggestions. Use when the user asks about Carowinds or any Six Flags / Cedar Fair park (Cedar Point, Canada's Wonderland, Magic Mountain, the Hurricane Harbor water parks, etc.) — current waits, what to ride next, what time the park opens/closes, or what shows are on. Backed by the sixflags-mcp server over the public themeparks.wiki API (no login).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Visitors planning a day at a Six Flags or Cedar Fair park can check operating hours, ride waits, attraction details, and showtimes, then use next-ride suggestions to plan what to do next.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separately configured sixflags-mcp server implementation is outside this package.

Mitigation: Review that server before enabling it.

Risk: Off-hours ride data may show CLOSED even when the park is not unexpectedly closed.

Mitigation: Check parkOpen and the park schedule before assuming the park is dark.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/sixflags-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language trip-planning guidance and park information]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live wait times and showtimes populate during park operating hours.]

## Skill Version(s):

2.1.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
