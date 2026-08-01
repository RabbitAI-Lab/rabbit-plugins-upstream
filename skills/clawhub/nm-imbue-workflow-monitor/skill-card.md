## Description: <br>
Detects workflow failures and inefficient patterns then files GitHub issues <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to monitor workflow executions, detect failures and inefficient patterns, and prepare GitHub or GitLab issues with evidence and suggested fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workflow evidence can include commands, output excerpts, session IDs, and working directories that may expose sensitive repository or environment details. <br>
Mitigation: Review and redact evidence before filing issues; keep auto_create_issues disabled unless a redaction and approval process is in place. <br>
Risk: Automatic issue creation can publish findings to GitHub or GitLab before duplicate checks or human review are complete. <br>
Mitigation: Require approval before creating issues, check for duplicates, and enforce the documented rate limit of five issues per session. <br>


## Reference(s): <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>
- [Detection Patterns](modules/detection-patterns.md) <br>
- [Efficiency Metrics](modules/efficiency-metrics.md) <br>
- [Issue Templates](modules/issue-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports and issue bodies with inline shell commands and YAML configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create GitHub or GitLab issue content; automatic issue creation should stay approval-gated.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
