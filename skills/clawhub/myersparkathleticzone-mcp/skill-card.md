## Description:

Helps agents answer questions about Myers Park High School athletics schedules, teams, rosters, coaches, news, and broadcast links using public information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find Myers Park High School sports fixtures, team and coach information, and related school athletics updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stale team IDs or partial past-season coverage can lead to incorrect claims about available teams or fixtures.

Mitigation: Resolve teams for the requested school year and state coverage limits when no results are found.

Risk: Missing or partially entered scores can be mistaken for zero scores or completed results.

Mitigation: Treat null scores as unknown and avoid inferring a result unless both sides have recorded scores.

Risk: Schedule changes can make a listed fixture misleading.

Mitigation: Check cancellation, postponement, and time-to-be-announced flags before confirming a game.

## Reference(s):

- [Myers Park Athletic Zone skill release](https://clawhub.ai/chrischall/skills/myersparkathleticzone-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language responses with schedules, team details, and source links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public athletics data may have missing scores and incomplete past-season coverage.]

## Skill Version(s):

1.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
