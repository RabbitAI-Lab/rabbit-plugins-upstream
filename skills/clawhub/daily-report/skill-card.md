## Description: <br>
Generate daily, weekly, and alert reports tracking leads, outreach, cost, priorities, and issues, saving structured summaries for progress monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[visualdeptcreative](https://clawhub.ai/user/visualdeptcreative) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Operators and growth teams use this skill to generate morning, end-of-day, weekly, and immediate alert reports for lead pipeline, outreach, costs, priorities, and blockers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Daily memory logs may capture sensitive lead, budget, issue, or business details. <br>
Mitigation: Avoid secrets, full lead records, personal message contents, and unnecessary confidential details; periodically review or delete old logs. <br>
Risk: Immediate Telegram alerts may expose operational events or reply status outside the local workspace. <br>
Mitigation: Send only minimal alert content, verify the destination, and avoid including secrets or full message contents. <br>
Risk: Generated reports can contain incomplete or stale metrics if the underlying pipeline data is not current. <br>
Mitigation: Review key counts, costs, blockers, and priorities before using the report for operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/visualdeptcreative/skills/daily-report) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report templates and alert guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes scheduled morning, end-of-day, weekly, and immediate alert report structures; local memory summaries may be written by the consuming agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
