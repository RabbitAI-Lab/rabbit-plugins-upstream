## Description:

Provides governed MySQL and MariaDB DBA operations for health checks, slow-query analysis, lock-wait and deadlock RCA, replication-lag diagnosis, fragmentation analysis, and guarded maintenance actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database administrators, and operations engineers use this skill to inspect and troubleshoot MySQL 8.x or MariaDB 10.6+ servers, produce RCA guidance, and run governed maintenance commands when intentionally authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes disruptive database write operations through MCP and does not enforce its own approval gate.

Mitigation: Use a least-privilege, preferably read-only MySQL or MariaDB account unless maintenance writes are intentionally authorized through external controls.

Risk: Production use with broad database privileges can allow destructive actions such as killing sessions, dropping indexes, resetting query stats, or changing global variables.

Mitigation: Require explicit external approval, prefer dry-run previews, review audit records, and limit elevated grants to the target schemas and operations needed.

Risk: Local state and non-interactive deployments depend on protected secrets and configuration under the mysql-aiops home directory.

Mitigation: Secure the local state directory, avoid weak placeholder passwords or wildcard host access, and protect MYSQL_AIOPS_MASTER_PASSWORD in CI or MCP deployments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/mysql-aiops)
- [Project Homepage](https://github.com/AIops-tools/MySQL-AIops)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup and Security Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured tool-call guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cited RCA findings, SQL maintenance previews, dry-run instructions, and security guidance for database access.]

## Skill Version(s):

0.10.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
