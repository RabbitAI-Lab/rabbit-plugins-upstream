## Description: <br>
Generates read-only GitLab user work statistics reports for a specified user and time range, covering merge requests, commits, push activity, and code review activity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[endcy](https://clawhub.ai/user/endcy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering managers, and authorized GitLab administrators use this skill to produce a Markdown work-activity report for a named GitLab user over an explicit time range. It is intended for authorized read-only analysis of GitLab Omnibus PostgreSQL data and optional repository commit metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks agents to use SSH and database access against a GitLab server. <br>
Mitigation: Use it only for GitLab servers you administer or are authorized to audit, and prefer a dedicated read-only database or API account. <br>
Risk: Generated SQL or git commands could expose sensitive work activity or run with broader permissions than intended. <br>
Mitigation: Review every generated SQL and git command before execution, keep queries read-only, and avoid collecting data beyond the requested user and time range. <br>
Risk: Credential handling in the skill depends on user-provided server configuration. <br>
Mitigation: Do not store real credentials in the skill folder; use environment variables or managed configuration and verify SSH host keys instead of auto-accepting them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/endcy/skills/gitlab-work-stats) <br>
- [GitLab PostgreSQL database guide](references/database-guide.md) <br>
- [Report template](references/report-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown report with SQL, Python, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a target GitLab username and time range; generated analysis should remain read-only and should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
