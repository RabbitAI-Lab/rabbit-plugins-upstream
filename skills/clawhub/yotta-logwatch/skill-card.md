## Description:

Analyzes local authentication, web access, PowerShell, and Windows event logs for suspicious activity and produces a reviewable timeline and report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security analysts and developers use this skill to review authorized local logs for signs of brute-force attempts, web attacks, suspicious scripts, and unusual account or system activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can modify agent skill directories more broadly than the analyzer's read-only behavior suggests.

Mitigation: Review the installer, select a reviewed target with --agent or --dir, and avoid global installation unless updates to all listed agents are intended.

Risk: An unpinned installation or a symbolic-link target may cause unintended changes.

Mitigation: Pin the npm package version and confirm that the target yotta-logwatch directory is not a symbolic link.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-logwatch)
- [Analysis specification](references/analysis-spec.md)
- [Authentication log rules](references/auth-log-rules.md)
- [Web access log rules](references/web-log-rules.md)
- [PowerShell log rules](references/powershell-log-rules.md)
- [Windows event log rules](references/windows-event-rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Plain text, JSON, or Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Time-ordered findings with severity, evidence, and Chinese explanations and review suggestions.]

## Skill Version(s):

0.3.1 (source: frontmatter, CHANGELOG, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
