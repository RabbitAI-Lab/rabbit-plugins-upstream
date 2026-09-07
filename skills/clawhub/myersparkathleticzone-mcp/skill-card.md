## Description:

Provides schedules, teams, rosters, coaches, news, game broadcast links, and result caveats for Myers Park High School Mustangs athletics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer Myers Park High School athletics questions about schedules, teams, rosters, coaches, opponents, venues, home or away status, news, broadcasts, and available scores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public upstream athletics data may be incomplete, especially scores and past-season coverage.

Mitigation: State unknown or null data as unknown, re-resolve current team IDs before team lookups, and avoid inferring wins, losses, or team existence from missing fields.

Risk: Event times and game status can be misstated if raw fields are repeated without interpretation.

Mitigation: Convert ISO UTC starts to America/New_York for user-facing answers and check cancellation, postponement, and TBA fields before saying a game is scheduled.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Markdown or plain text answers based on public athletics data and tool-result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include timezone conversion from ISO UTC to America/New_York and caveats for missing scores, stale team IDs, cancellations, postponements, TBA games, or partial past-season coverage.]

## Skill Version(s):

0.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
