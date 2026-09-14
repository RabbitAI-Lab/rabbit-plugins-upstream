## Description:

mysql-aiops helps agents operate and troubleshoot MySQL 8.x and MariaDB 10.6+ servers with health checks, root-cause analysis for slow queries, lock waits, replication lag and fragmentation, plus guarded maintenance commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers, database administrators, and operations engineers use this skill to investigate MySQL or MariaDB server health, query performance, locking, replication, index health, table fragmentation, and maintenance actions through audited DBA workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes high-impact MySQL and MariaDB maintenance writes to agents without an enforced approval or read-only gate.

Mitigation: Use a dedicated least-privilege read-only database account by default, enable write privileges only for deliberate maintenance sessions, and rely on dry-run previews plus operator confirmation before writes.

Risk: Database credentials and transport settings can create exposure if long-lived secrets or weak TLS modes are used.

Mitigation: Avoid exporting long-lived master passwords, prefer verify_identity TLS with a CA on untrusted networks, and install only from pinned trusted package or plugin releases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/mysql-aiops)
- [Project homepage](https://github.com/AIops-tools/MySQL-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and structured tool-output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include database observations, root-cause findings, dry-run maintenance commands, configuration steps, and safety notes.]

## Skill Version(s):

0.10.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
