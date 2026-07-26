## Description: <br>
Analyzes a specified Zentao user's stories, tasks, bugs, and effort logs over a chosen time range through read-only database queries and produces a Markdown work report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[endcy](https://clawhub.ai/user/endcy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, project administrators, and authorized managers use this skill to generate a structured work-activity report for a named Zentao user and time period. It supports authorized work analysis by combining current Zentao records with action history and effort logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated reports may contain sensitive employee work activity and performance-related data. <br>
Mitigation: Generate reports only with authorization, keep report files private, avoid insecure sharing channels, and remove reports that are no longer needed. <br>
Risk: Database credentials or over-privileged access could expose Zentao data. <br>
Mitigation: Use a read-only database account, keep config.json private, and prefer environment variables or managed configuration for secrets. <br>
Risk: Queries that are not limited to read-only operations could change Zentao data. <br>
Mitigation: Review database actions before execution and run only SQL SELECT statements. <br>


## Reference(s): <br>
- [Zentao Work Stats ClawHub Page](https://clawhub.ai/endcy/skills/zentao-work-stats) <br>
- [Report Template](references/report-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report with SQL and Python code blocks plus configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires authorized read-only Zentao database access; generated reports can contain sensitive employee work data.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
