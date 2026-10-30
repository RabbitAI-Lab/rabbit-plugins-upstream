## Description:

Schedules, teams, rosters, coaches, news and game broadcast links for Myers Park High School (Mustangs) athletics. Use when the user asks about Myers Park games, when a team plays, who a team's coach is, opponents, home/away fixtures, or school sports news.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent for Myers Park athletics schedules, team rosters and coaches, scores, school sports news, and broadcast links. The guidance helps the agent explain schedule status and distinguish missing or partial records from confirmed results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incomplete scores or partial past-season coverage could be mistaken for a final result or for evidence that a sport or game did not exist.

Mitigation: Treat null scores as unknown, report coverage limits, and do not infer a result or absence from an empty partial search.

Risk: A team ID can become stale between school years, causing team-specific lookups to fail or use the wrong season context.

Mitigation: Resolve the team and sport slug for the requested school year before making team-specific lookups.

## Reference(s):

- [Myersparkathleticzone-mcp on ClawHub](https://clawhub.ai/chrischall/skills/myersparkathleticzone-mcp)
- [Publisher profile: chrischall](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Text, Guidance, Links]

**Output Format:** [Natural-language responses with schedule, team, score, news, and broadcast-link details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe incomplete score records and season coverage; broadcast entries are links, not video clips.]

## Skill Version(s):

1.1.11 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
