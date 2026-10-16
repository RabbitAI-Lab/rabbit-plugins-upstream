## Description:

Provides schedules, teams, rosters, coaches, scores, news, and broadcast links for Myers Park High School athletics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Fans and community members use this skill to ask about Myers Park teams, upcoming games, coaches, scores, and athletics news.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Missing or partial scores could be mistaken for a loss, a zero score, or an unplayed game.

Mitigation: Treat null scores as unknown and state when the school has not recorded a result.

Risk: Incomplete past-season coverage or stale team IDs could make a team appear absent.

Mitigation: Resolve team IDs for the requested year and explain coverage limits rather than claiming a team did not exist.

Risk: A listed fixture may be cancelled, postponed, or still awaiting confirmation.

Mitigation: Check the event status before stating that a game will take place.

## Reference(s):

- [Myers Park Athletic Zone skill on ClawHub](https://clawhub.ai/chrischall/skills/myersparkathleticzone-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers may include schedules, team details, scores, or links; availability depends on public source data.]

## Skill Version(s):

1.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
