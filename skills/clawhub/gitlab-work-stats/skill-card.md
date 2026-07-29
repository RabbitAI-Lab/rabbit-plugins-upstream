## Description: <br>
Generates read-only GitLab work statistics reports for a specified user and date range, covering merge requests, commits, and code review activity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[endcy](https://clawhub.ai/user/endcy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering managers, and authorized team leads use this skill to create Markdown activity reports for a GitLab user over a defined time range. It is intended for authorized work-statistics analysis, not covert monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GitLab activity reports can expose sensitive work data if run without authorization. <br>
Mitigation: Use the skill only for authorized inspections, confirm the target user and time range before analysis, and protect generated reports. <br>
Risk: Server connection configuration can contain credentials or access tokens. <br>
Mitigation: Keep server-config.json private, prefer environment variables or managed configuration, and use a dedicated least-privilege account. <br>
Risk: Broad database or repository access could collect more information than the report requires. <br>
Mitigation: Use read-only SELECT queries with tight user and date filters, prefer API or parameterized database access where possible, and avoid the optional git-log step unless repository metadata access is explicitly permitted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/endcy/skills/gitlab-work-stats) <br>
- [GitLab PostgreSQL database guide](references/database-guide.md) <br>
- [Report template](references/report-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, SQL queries, Configuration guidance] <br>
**Output Format:** [Markdown report with supporting read-only SQL and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a GitLab username, date range, authorized read-only GitLab access, and optional project filtering.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
