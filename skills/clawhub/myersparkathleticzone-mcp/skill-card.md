## Description:

Schedules, teams, rosters, coaches, news and game broadcast links for Myers Park High School (Mustangs) athletics. Use when the user asks about Myers Park games, when a team plays, who a team's coach is, opponents, home/away fixtures, or school sports news.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer questions about Myers Park High School athletics schedules, teams, coaches, rosters, scores, news, and broadcast links from public athletics information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on public Myers Park athletics information and an external MCP server or tool set, so answers can reflect missing or incomplete upstream data.

Mitigation: Tell users when data is unavailable or partial, and avoid implying that missing schedules, rosters, or scores prove an event or team does not exist.

Risk: Team identifiers differ by school year, and stale identifiers can produce not-found results.

Mitigation: Resolve the team for the requested year before using team-scoped schedule, roster, or score tools.

Risk: Null scores and partially entered results can be mistaken for zero or a completed win/loss.

Mitigation: Treat null scores as unknown, require both sides before reporting a result, and explain when the school did not record usable scores.

Risk: Game times are returned in ISO UTC and can be misreported for the school's local audience.

Mitigation: Convert kickoff and event times to America/New_York before presenting them to users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myersparkathleticzone-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Markdown guidance with MCP tool names, result interpretation rules, and caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented guidance for querying public athletics data; no credentials or local system access are requested by the inspected artifact.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
