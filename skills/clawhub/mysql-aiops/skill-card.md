## Description:

mysql-aiops helps agents operate and troubleshoot MySQL 8.x and MariaDB 10.6+ servers with health checks, root-cause analyses for slow queries, locks, replication lag, fragmentation, and guarded maintenance actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, DBAs, and operations engineers use this skill to inspect MySQL/MariaDB health, diagnose query, lock, replication, and fragmentation issues, and prepare or execute governed maintenance actions when the connected account has privileges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change live MySQL/MariaDB databases when connected with write privileges, including killing sessions, changing indexes, running OPTIMIZE or ANALYZE, resetting query statistics, and setting global variables.

Mitigation: Start with a least-privilege read-only monitoring account and grant write privileges only for planned maintenance; use dry-run previews, CLI confirmations, and maintenance windows for potentially blocking operations.

Risk: Database credentials or the mysql-aiops master password could be exposed through shell history, CI logs, or unprotected runtime environments.

Mitigation: Use the encrypted secrets store and protected secret injection, and avoid placing passwords directly in commands, shell history, or logs.

Risk: Some behavior is mock-validated and may vary against a live MySQL or MariaDB server configuration.

Mitigation: Run mysql-aiops doctor and validate access, server flavor, performance_schema availability, and replica status on the intended target before relying on analysis or remediation.

## Reference(s):

- [mysql-aiops capabilities](references/capabilities.md)
- [mysql-aiops CLI reference](references/cli-reference.md)
- [mysql-aiops setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Project homepage from ClawHub metadata](https://github.com/AIops-tools/MySQL-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/mysql-aiops)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or text guidance with shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include measured database observations, risk labels, dry-run statements, and configuration paths.]

## Skill Version(s):

0.8.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
