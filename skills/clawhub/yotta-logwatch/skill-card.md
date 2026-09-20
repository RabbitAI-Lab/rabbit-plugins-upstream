## Description:

Yuancha is a read-only, offline security log analysis skill that parses auth, Web access, PowerShell script-block, and Windows event logs to flag suspicious activity and produce timelines and Chinese teaching-style reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security engineers, incident responders, and authorized auditors use this skill to review local log files for brute-force activity, abnormal logins, Web attack traces, suspicious PowerShell behavior, account operations, process anomalies, and log clearing. Findings are prompts for human verification, not final incident determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer modes may copy the skill into multiple agent skill directories without interactive confirmation.

Mitigation: Install into an explicit target with --agent or --dir, avoid broad or global modes unless intentional, and review the destination before use.

Risk: Security findings from log heuristics can be incomplete or misleading if treated as conclusive.

Mitigation: Use results as triage prompts, verify evidence lines manually, and correlate with other authorized incident-response data before taking action.

Risk: Running an unpinned npm install can retrieve a newer package version than the reviewed release.

Mitigation: Pin the package version when using npx or npm-based installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-logwatch)
- [Project homepage](https://github.com/YottaMeta/yotta-logwatch)
- [Auth log rules](references/auth-log-rules.md)
- [Web log rules](references/web-log-rules.md)
- [PowerShell log rules](references/powershell-log-rules.md)
- [Windows event rules](references/windows-event-rules.md)
- [Analysis specification](references/analysis-spec.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Text, JSON, or Markdown reports with timelines, evidence lines, severity labels, explanations, and review suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local log files or standard input; supports severity filtering, recursive directory scans, and explicit log-type selection.]

## Skill Version(s):

0.2.9 (source: SKILL.md frontmatter, package.json, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
