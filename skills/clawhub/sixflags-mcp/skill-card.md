## Description:

Helps agents plan visits to Six Flags and Cedar Fair parks with live wait times, park hours, show schedules, attraction lookup, and next-ride suggestions using public themeparks.wiki data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan a day at a Six Flags or Cedar Fair park, including deciding when to arrive, what rides to prioritize, and where show schedules fit into the day.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live wait times, hours, and show schedules may be stale or unavailable outside park operating hours.

Mitigation: Check the park schedule and parkOpen status before using wait-time or show data for time-sensitive plans.

Risk: The skill depends on an external MCP server and public park data.

Mitigation: Confirm the configured MCP server is the expected one before installing or using the skill.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance, API calls]

**Output Format:** [Markdown or plain text responses with tool-derived park data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public live park data that may be stale or unavailable outside operating hours.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
