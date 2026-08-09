## Description: <br>
Read MaxPreps.com high school sports data to find a school, then retrieve team schedules, scores, records, rosters, stat leaders, rankings, and athlete careers for US high schools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill for specific, user-directed lookups of public high-school sports information from MaxPreps, including team schedules, rosters, rankings, standings, and athlete career summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can fetch and process public roster and athlete-profile information, including information about student athletes. <br>
Mitigation: Use it only for specific, user-directed lookups and avoid republishing or aggregating minor-related data beyond a legitimate need. <br>
Risk: Out-of-season or soft-deleted MaxPreps records can make current rosters, schedules, or leaderboards appear incomplete. <br>
Mitigation: Follow the skill guidance to resolve canonical paths, check prior seasons when appropriate, and rely on the script's default filtering of deleted rows. <br>


## Reference(s): <br>
- [MaxPreps recipes](references/recipes.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/maxpreps-mcp) <br>
- [MaxPreps](https://www.maxpreps.com) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; command results are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only lookups against public MaxPreps pages; no authentication or write path is described.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
