## Description:

元察分析 auth/secure、Web、PowerShell 和 Windows 事件日志中的可疑活动，并生成时间线与中文说明。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security practitioners and system administrators use the skill to review supplied local authentication, Web, PowerShell, and Windows event logs for suspicious activity and prepare a triage report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer confirmation controls may be bypassed, and directory scans may exceed the selected scope.

Mitigation: Prefer a corrected release. If using this version, select one agent or installation directory and preview with --dry-run.

Risk: Writing a report may overwrite a source log.

Mitigation: Analyze copied logs with explicit filenames; print reports to stdout or choose a new, separate output file.

Risk: Detection alerts may be mistaken for confirmed incidents.

Mitigation: Manually verify each alert before taking action.

## Reference(s):

- [Analysis specification](artifact/references/analysis-spec.md)
- [Authentication log rules](artifact/references/auth-log-rules.md)
- [Web log rules](artifact/references/web-log-rules.md)
- [PowerShell log rules](artifact/references/powershell-log-rules.md)
- [Windows event log rules](artifact/references/windows-event-rules.md)
- [Project homepage](https://github.com/YottaMeta/yotta-logwatch)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-logwatch)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Text, JSON, or Markdown reports with a chronological timeline and Chinese explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include severity, evidence lines, explanations, and review suggestions.]

## Skill Version(s):

0.3.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
