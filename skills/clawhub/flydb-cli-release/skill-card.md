## Description:

Guides agents through Flydb CLI release-package use for database migrations, including Java and CLI checks, package verification, configuration, dry-run migration review, write-gated migration commands, JDBC driver setup, and error handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to install and validate Flydb CLI, inspect migration state, run dry-run previews, execute approved database migrations, and troubleshoot configuration, driver, and error-code issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through real database-changing operations such as migrate, baseline, repair, undo, and clean.

Mitigation: Use least-privilege database credentials, run validation and dry-run checks, review the target summary, and require explicit approval before write operations.

Risk: Credentials or sensitive JDBC connection details may be exposed in commands, logs, or reports.

Mitigation: Keep passwords in environment variables or secret files and redact JDBC URLs and secrets from user-facing output.

## Reference(s):

- [Release package, installation, and Java runtime](references/release-package.md)
- [CLI command reference](references/commands.md)
- [Configuration reference](references/configuration.md)
- [JDBC driver setup and FLYDB-1003 troubleshooting](references/drivers.md)
- [Error code reference](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline bash commands and concise execution summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Database URLs and credentials should be redacted in user-facing output.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
