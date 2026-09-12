## Description:

Schedules, teams, rosters, coaches, news and game broadcast links for Myers Park High School (Mustangs) athletics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer questions about Myers Park High School athletics schedules, teams, rosters, coaches, news, scores, and broadcast links from public site data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Returned athletics data can have missing scores, null values, UTC kickoff times, or incomplete past-season coverage.

Mitigation: Review returned fields before answering, convert kickoff times to the user's relevant timezone, and state missing or incomplete data as unavailable rather than inferring outcomes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myersparkathleticzone-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or plain text answers based on public athletics MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scores, kickoff times, cancellations, postponements, and past-season coverage should be checked against returned tool fields before being stated to users.]

## Skill Version(s):

0.3.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
