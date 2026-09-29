## Description:

Read public MaxPreps high-school sports data to find schools and retrieve team schedules, scores, records, rosters, stat leaders, rankings, and athlete careers across the United States.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to look up public U.S. high-school sports results, team details, rankings, and athlete profiles on MaxPreps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Roster and athlete results can contain information about school-age athletes.

Mitigation: Use only public information and handle athlete details with appropriate privacy care.

Risk: Broad or repeated requests to MaxPreps can impose unnecessary load.

Mitigation: Use targeted school and team lookups rather than broad scraping.

## Reference(s):

- [MaxPreps skill recipes](references/recipes.md)
- [MaxPreps](https://www.maxpreps.com)
- [ClawHub release](https://clawhub.ai/chrischall/skills/maxpreps-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses with public sports data and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Data is retrieved from public MaxPreps pages; no account or API key is required.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
