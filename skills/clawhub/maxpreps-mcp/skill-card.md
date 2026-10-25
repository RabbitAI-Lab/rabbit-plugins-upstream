## Description:

Helps agents find US high school sports data on MaxPreps, including teams, schedules, scores, rosters, rankings, statistics, and athlete careers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and sports researchers use this skill to look up public US high school team results, rosters, statistics, rankings, and athlete histories without account access.

### Deployment Geography for Use:

Global (covers US high school sports)

## Known Risks and Mitigations:

Risk: Running the included helper makes public web requests and stores a temporary build identifier.

Mitigation: Run it only for public MaxPreps lookups; do not provide credentials, browser sessions, or private files.

## Reference(s):

- [MaxPreps recipes](references/recipes.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/maxpreps-mcp)
- [MaxPreps](https://www.maxpreps.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Markdown summaries, JSON data, and optional shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public, read-only data; results depend on available seasons and site updates.]

## Skill Version(s):

1.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
