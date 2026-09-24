## Description:

Read MaxPreps.com high school sports data -- find a school, then get team schedules, scores, records, rosters, stat leaders, rankings, and athlete careers for any US high school.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query public MaxPreps high school sports data and guide agents through school lookup, team path resolution, schedules, scores, rosters, rankings, standings, stat leaders, and athlete career checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes live read-only requests to MaxPreps and, for troubleshooting recipes, MaxPreps asset hosts.

Mitigation: Use it only where those outbound public web requests are acceptable.

Risk: Public sports data can be stale, out of season, or absent for a specific team path.

Mitigation: Resolve canonical school and team paths first, check prior seasons when current season data is empty, and cross-check decoded schedules or rosters before reporting conclusions.

## Reference(s):

- [MaxPreps recipes](references/recipes.md)
- [MaxPreps](https://www.maxpreps.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/maxpreps-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-producing CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled CLI reads public MaxPreps pages, decodes Next.js JSON payloads, and writes only a temporary buildId cache.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
