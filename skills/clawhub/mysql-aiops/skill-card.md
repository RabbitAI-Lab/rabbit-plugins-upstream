## Description:

MySQL AIops helps agents operate and troubleshoot MySQL 8.x and MariaDB 10.6+ servers with DBA health checks, RCA workflows, governed write operations, audit logging, undo support for reversible changes, and setup guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database administrators, and operations engineers use this skill to inspect MySQL or MariaDB health, diagnose slow queries, lock waits, replication lag, and fragmentation, and perform guarded maintenance actions. It is intended for environments where the configured database account has only the privileges appropriate for the requested task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate with sensitive MySQL or MariaDB authority if the configured account has broad privileges.

Mitigation: Start with a least-privilege read-only account and enable write privileges only for maintenance tasks that require them.

Risk: State-changing operations such as killing sessions, changing globals, rebuilding tables, or modifying indexes can affect production availability or behavior.

Mitigation: Review dry-run output before execution, use the built-in confirmation flow, and schedule disruptive maintenance actions appropriately.

Risk: Database credentials and master passwords are sensitive operational secrets.

Mitigation: Prefer interactive secret entry or a secret manager, avoid long-lived environment variables where possible, and keep the encrypted secret store access-controlled.

Risk: Database observations and RCA results depend on the live server configuration, including performance_schema availability and account permissions.

Mitigation: Run connectivity and capability checks before relying on RCA output, and report missing measurements as unavailable rather than inferring them.

## Reference(s):

- [mysql-aiops capabilities](artifact/references/capabilities.md)
- [mysql-aiops CLI reference](artifact/references/cli-reference.md)
- [mysql-aiops setup and security guide](artifact/references/setup-guide.md)
- [Agent guardrails for mysql-aiops](artifact/references/agent-guardrails.md)
- [MySQL AIops homepage](https://github.com/AIops-tools/MySQL-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/mysql-aiops)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured tool guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include database observations, RCA findings, dry-run previews, audit-oriented guidance, and recommended follow-up checks.]

## Skill Version(s):

0.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
