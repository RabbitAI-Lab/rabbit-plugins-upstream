## Description: <br>
Content topic-planning agent that generates structured topic briefs from knowledge-base updates, competitor signals, content calendars, and performance data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Brand-side content marketing teams use this skill to turn product knowledge-base updates, competitor signals, and editorial schedules into prioritized topic briefs. It supports topic judgment and brief handoff only, with human confirmation before downstream content writing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local content calendars, product knowledge bases, and marketing inventories, which may contain sensitive planning or customer material. <br>
Mitigation: Install it only in workspaces where those local marketing inputs are appropriate for agent access. <br>
Risk: Broad activation phrases such as "content plan" or "本周内容" may trigger the skill during unrelated workspace conversations. <br>
Mitigation: Narrow activation phrases if the workspace frequently uses similar terms outside topic-planning tasks. <br>
Risk: Topic briefs could move into downstream content production before review. <br>
Mitigation: Keep the documented human confirmation step before invoking content-writing workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-planner) <br>
- [Publisher profile](https://clawhub.ai/user/haiyangchenbj) <br>
- [README](artifact/README.md) <br>
- [README Chinese](artifact/README_zh.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Guidance] <br>
**Output Format:** [Markdown topic brief plus execution summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes briefs to content-calendar/briefs/YYYY-MM-DD-brief.md and requires human confirmation before downstream content writing.] <br>

## Skill Version(s): <br>
1.1.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
