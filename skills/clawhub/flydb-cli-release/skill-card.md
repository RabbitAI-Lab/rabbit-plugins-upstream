## Description:

Guides agents through Flydb CLI database migration workflows, including Java and package checks, configuration, dry runs, migration execution, baselines, repair, undo, clean, JDBC driver setup, and error handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to plan, verify, and run Flydb CLI migrations against supported relational databases. It helps establish execution context, protect credentials, perform dry runs, handle JDBC driver issues, and verify migration results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Database-changing operations such as migrate, baseline, repair, undo, and clean can alter schema state or data.

Mitigation: Confirm the target environment, run validate and dry-run checks first, and require explicit user authorization before executing write operations.

Risk: Production credentials may be exposed through command lines, configuration files, logs, or final reports.

Mitigation: Use environment variables, environment references, or password files for secrets; redact JDBC URLs and do not include passwords in commands or summaries.

Risk: The clean command is destructive and can remove database objects.

Mitigation: Keep clean disabled by default and require target confirmation plus explicit user authorization before using the force and clean-enable switches.

Risk: JDBC driver resolution can involve vendor drivers or remote repositories.

Mitigation: Use approved local drivers or controlled repositories, respect vendor licensing, and avoid downloading or redistributing untrusted driver artifacts.

## Reference(s):

- [Release Package](references/release-package.md)
- [CLI Commands](references/commands.md)
- [Configuration](references/configuration.md)
- [JDBC Drivers](references/drivers.md)
- [Error Codes](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include database target summaries, dry-run findings, validation outcomes, remediation steps, and redacted connection details.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
