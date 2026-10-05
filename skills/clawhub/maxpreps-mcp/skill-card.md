## Description:

Find US high school sports teams and retrieve public MaxPreps schedules, scores, rosters, rankings, statistics, and athlete careers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can look up US high school sports teams and summarize public game results, team records, rosters, rankings, statistics, and athlete careers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the included helper sends outbound requests to public MaxPreps/CBS-hosted pages.

Mitigation: Run it only when those outbound requests are acceptable and review the returned data before using it.

Risk: An out-of-season team or a stale site build can make results appear missing.

Mitigation: Check an appropriate season and refresh or retry before concluding that records are unavailable.

## Reference(s):

- [MaxPreps skill on ClawHub](https://clawhub.ai/chrischall/skills/maxpreps-mcp)
- [MaxPreps](https://www.maxpreps.com)
- [Skill usage recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance and structured JSON sports data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public data; current-season records may be empty before games begin.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
