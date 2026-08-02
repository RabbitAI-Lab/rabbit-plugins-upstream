## Description: <br>
TCMS Planner generates structured topic briefs from knowledge-base updates, competitor signals, content calendars, and performance data without writing article bodies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams and content operators use this skill to convert product knowledge-base updates, competitor signals, and calendar needs into 1-3 prioritized topic briefs for human review before drafting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic content-planning language could activate the skill when the user did not intend to run the planner. <br>
Mitigation: Use explicit requests such as running tcms-planner or generating a topic brief. <br>
Risk: Topic suggestions can be incomplete or misleading when source material is thin or outdated. <br>
Mitigation: Require human confirmation before entering the writer workflow and mark insufficient material instead of recommending a topic. <br>
Risk: Briefs involving internal customer cases may expose sensitive details. <br>
Mitigation: Mark internal-source customer cases with a redaction requirement before any downstream use. <br>


## Reference(s): <br>
- [TCMS Planner ClawHub page](https://clawhub.ai/haiyangchenbj/skills/tcms-planner) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown topic brief plus execution summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes brief files under content-calendar/briefs when configured; requires human confirmation before downstream writing.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
