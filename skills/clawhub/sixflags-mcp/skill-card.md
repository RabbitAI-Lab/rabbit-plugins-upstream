## Description:

Plan theme park visits across Six Flags and Cedar Fair parks using live waits, operating hours, show schedules, park lookup, and next-ride suggestions backed by public themeparks.wiki data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External park visitors and agents assisting them use this skill to plan a day at Six Flags and Cedar Fair parks, including what to ride next, when the park is open, and which shows fit the day.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live waits and show schedules can be unavailable or misleading outside operating hours.

Mitigation: Check the park schedule and open-status fields before treating closed rides or missing wait times as current operating conditions.

Risk: Trip plans depend on the availability and freshness of public theme park data.

Mitigation: Use the health check and verify time-sensitive recommendations against current park information before relying on them.

Risk: The skill should not require credentials or local file access for the described use case.

Mitigation: Do not provide account credentials or local access; confirm the installation only queries public park data through the referenced service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/sixflags-mcp)
- [themeparks.wiki](https://themeparks.wiki/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or plain text responses with park data summaries and ride-planning recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depends on live public park data; waits and shows may be unavailable outside operating hours.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
