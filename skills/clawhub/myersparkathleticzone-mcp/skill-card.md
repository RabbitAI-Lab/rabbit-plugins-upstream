## Description:

Provides public Myers Park High School athletics schedules, team and coach details, news, and broadcast links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students, families, and other users can ask an agent about Myers Park High School games, teams, coaches, school sports news, and broadcast links using public athletics information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Team IDs can become stale between school years.

Mitigation: Resolve the team for the requested year before querying its schedule, roster, or scores.

Risk: Missing scores and partial historical coverage can produce misleading results.

Mitigation: Treat null scores as unknown and describe coverage gaps rather than assuming a game was not played.

Risk: Broadcast links may be mistaken for playable clips.

Mitigation: Identify NFHS Network links as broadcasts, not clips or zero-second videos.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown responses with schedules, team information, news, and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public information; game results and historical coverage may be incomplete.]

## Skill Version(s):

1.1.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
