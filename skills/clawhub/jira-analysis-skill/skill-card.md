## Description: <br>
Fetches bug data from Jira Server/Data Center, analyzes bug trends and operational metrics, and produces an interactive self-contained HTML report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cntesters](https://clawhub.ai/user/cntesters) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and engineering managers use this skill to collect Jira bug data, review trends and backlog health, and generate a local HTML report for project-level bug analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Jira credentials may be exposed or over-privileged during data collection. <br>
Mitigation: Use a least-privileged Jira personal access token instead of a password, and scope it only to the project data needed for the report. <br>
Risk: TLS verification bypass can expose Jira credentials and issue data to interception. <br>
Mitigation: Avoid --no-verify and curl -k except in isolated testing; configure trusted certificates for normal use. <br>
Risk: Generated HTML and Excel-compatible reports can contain raw issue details and identities. <br>
Mitigation: Store generated reports in approved locations, restrict access, and handle them as sensitive enterprise data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cntesters/skills/jira-analysis-skill) <br>
- [Publisher profile](https://clawhub.ai/user/cntesters) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON-producing script execution, and generated self-contained HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow may generate local HTML and Excel-compatible report artifacts containing raw Jira issue details.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
