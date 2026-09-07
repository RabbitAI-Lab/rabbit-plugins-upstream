## Description:

元察 yotta-logwatch analyzes local auth, web access, PowerShell, and Windows event logs to flag brute-force attempts, webshell activity, scanning, abnormal logins, suspicious scripts, account operations, suspicious processes, and log clearing, then returns timelines and Chinese teaching-style reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security engineers, incident responders, red/blue team operators, and authorized auditors use this skill to perform read-only offline triage of local security logs, identify suspicious activity, and generate timeline reports with review guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled installers can copy the skill into multiple agent skill directories.

Mitigation: Install with an explicit --agent or --dir target, avoid no-argument and global installer modes unless intended, and pin or verify the package version before running npx.

Risk: Security logs may contain sensitive operational data.

Mitigation: Analyze the narrowest required log file or directory and treat generated reports as sensitive.

## Reference(s):

- [元察分析规范（五块规范）](references/analysis-spec.md)
- [auth 日志检测规则（元察 · 元）](references/auth-log-rules.md)
- [PowerShell 脚本块日志检测规则（元察 · 元）](references/powershell-log-rules.md)
- [Web 访问日志检测规则（元察 · 元）](references/web-log-rules.md)
- [Windows 事件日志检测规则（元察 · 元）](references/windows-event-rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text, Markdown, or JSON reports with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include log-derived evidence and should be handled as sensitive operational data.]

## Skill Version(s):

0.2.8 (source: server release metadata; artifact files report 0.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
