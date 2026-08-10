## Description: <br>
Schedules, teams, rosters, coaches, news and game broadcast links for Myers Park High School (Mustangs) athletics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer public Myers Park High School athletics questions about schedules, teams, rosters, coaches, news, results, and broadcast links. It is useful when responses need to resolve the correct team and explain missing or incomplete school athletics data clearly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public school athletics data can be incomplete or stale, especially scores and past-season coverage. <br>
Mitigation: State missing-score and partial-coverage caveats explicitly, and do not infer wins, losses, zeros, or team existence from null or empty results. <br>
Risk: Event timing or status may be misreported if timezone, cancellation, postponement, or TBA fields are ignored. <br>
Mitigation: Convert UTC start times to America/New_York for user-facing answers and check cancellation, postponement, and TBA fields before saying a game is scheduled. <br>
Risk: Team-scoped lookups can fail when a stale team id from another school year is reused. <br>
Mitigation: Resolve the team for the requested school year before team schedule, roster, or score lookups, and re-resolve when a team is not found. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myersparkathleticzone-mcp) <br>
- [Publisher profile](https://clawhub.ai/user/chrischall) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain text guidance for public athletics lookups] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include schedule details, roster or coach summaries, news and broadcast links, and caveats for missing scores, stale team ids, timezone conversion, cancellations, postponements, and partial past-season coverage.] <br>

## Skill Version(s): <br>
0.2.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
