## Description:

Yuancha yotta-logwatch helps agents analyze local auth, web access, PowerShell, and Windows event logs offline, flag suspicious activity, and produce timelines with Chinese teaching-style reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security engineers, incident responders, auditors, and developers use this skill to triage authorized local log files for brute-force activity, abnormal logins, web attack traces, suspicious PowerShell behavior, Windows account events, and log-clearing indicators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing into a broad or unintended agent directory could overwrite or disturb an existing yotta-logwatch folder.

Mitigation: Install with a specific --agent or --dir target and avoid directories where an existing yotta-logwatch folder contains work that must be preserved.

Risk: Log analysis can expose sensitive operational or personal data if run on logs outside the user's authorization.

Mitigation: Run the skill only on logs the user is authorized to analyze, and prefer stdout unless a report file is intentionally needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-logwatch)
- [analysis-spec.md](references/analysis-spec.md)
- [auth-log-rules.md](references/auth-log-rules.md)
- [web-log-rules.md](references/web-log-rules.md)
- [powershell-log-rules.md](references/powershell-log-rules.md)
- [windows-event-rules.md](references/windows-event-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples; the underlying tool can emit text, JSON, or Markdown reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local log files or stdin and writes to stdout by default, with optional report-file output when explicitly requested.]

## Skill Version(s):

0.2.7 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
