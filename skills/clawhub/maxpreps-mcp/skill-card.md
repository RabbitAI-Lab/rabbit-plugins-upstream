## Description:

Read MaxPreps.com high school sports data to find schools and retrieve team schedules, scores, records, rosters, stat leaders, rankings, and athlete careers across the United States.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users look up public US high school sports information, including school teams, game results, rosters, rankings, and athlete careers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public roster and athlete results may contain information about students.

Mitigation: Limit lookups and shared outputs to relevant public sports information; avoid treating results as private records.

Risk: Sports results may be incomplete or mistaken for official records.

Mitigation: Check the relevant season and verify important results against the original source before relying on them.

Risk: Broad lookups can generate unnecessary requests to MaxPreps.

Mitigation: Use scoped school and team queries rather than broad scraping.

## Reference(s):

- [MaxPreps MCP on ClawHub](https://clawhub.ai/chrischall/skills/maxpreps-mcp)
- [MaxPreps](https://www.maxpreps.com)
- [MaxPreps recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Guidance]

**Output Format:** [Structured JSON results and text or Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on publicly available MaxPreps data and the selected school, team, and season.]

## Skill Version(s):

1.1.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
