## Description:

Read MaxPreps.com high school sports data to find schools and retrieve team schedules, scores, records, rosters, stat leaders, rankings, and athlete careers across the United States.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can look up public US high-school sports information, including school teams, schedules, results, rosters, rankings, and athlete careers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rosters and athlete pages may contain public information about high-school students.

Mitigation: Avoid unnecessary collection or redistribution, and respect privacy expectations and site terms.

Risk: Using the skill runs a bundled Node script that sends read-only requests to MaxPreps.

Mitigation: Install only if comfortable allowing the agent to run the script and make those requests.

Risk: Out-of-season pages may have empty results, and some statewide scoreboards are not available through this skill.

Mitigation: Check a prior season or individual team schedules before concluding no games or athletes exist.

## Reference(s):

- [MaxPreps MCP on ClawHub](https://clawhub.ai/chrischall/skills/maxpreps-mcp)
- [MaxPreps](https://www.maxpreps.com)
- [Usage recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and shell examples; retrieved sports data is JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only access to public sports data; availability and freshness depend on MaxPreps.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
