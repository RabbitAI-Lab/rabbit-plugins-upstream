## Description:

元察 yotta-logwatch helps agents perform read-only, offline analysis of local auth, Web access, PowerShell, and Windows event logs to identify suspicious activity and produce timelines with Chinese teaching-style explanations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security engineers, and incident responders use this skill to triage authorized local security logs for brute force attempts, scanning, suspicious scripts, account activity, process anomalies, and log clearing. It supports read-only audit workflows for owned assets, authorized tests, CTFs, and teaching environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write analysis reports to user-selected paths.

Mitigation: Use --output or report paths only where creating or overwriting a file is intended.

Risk: Broad installer targets can copy the skill into many agent environments.

Mitigation: Prefer --agent or --dir unless global installation is intentional.

Risk: Overly broad scans may review more local log data than intended.

Mitigation: Pass only the specific log files or directories that are in scope for the authorized review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-logwatch)
- [元察 analysis specification](references/analysis-spec.md)
- [auth log rules](references/auth-log-rules.md)
- [Web log rules](references/web-log-rules.md)
- [PowerShell log rules](references/powershell-log-rules.md)
- [Windows event log rules](references/windows-event-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Text, JSON, or Markdown reports with timelines, severity labels, evidence lines, and Chinese review guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write reports to a user-selected output path; exit codes distinguish no findings, findings, and usage or read errors.]

## Skill Version(s):

0.2.6 (source: SKILL.md frontmatter, CHANGELOG.md, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
