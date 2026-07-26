## Description: <br>
Mysql Aiops helps agents operate and troubleshoot MySQL 8.x and MariaDB 10.6+ servers with governed DBA workflows for health checks, slow-query analysis, lock waits, replication lag, fragmentation, index health, and audited maintenance actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, database administrators, and operations teams use this skill to inspect MySQL or MariaDB server state, diagnose performance and replication issues, and prepare governed maintenance actions with audit records and dry-run previews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes powerful MySQL/MariaDB write operations such as killing sessions, changing global variables, optimizing tables, and creating or dropping indexes. <br>
Mitigation: Start with a least-privilege read-only account for monitoring, grant write privileges only when needed, use dry-run previews, and rely on the skill's audit records and reversible-operation undo descriptors where available. <br>
Risk: Database credentials and the master password protect access to production systems. <br>
Mitigation: Protect MYSQL_AIOPS_MASTER_PASSWORD and the ~/.mysql-aiops directory carefully, and use the encrypted secrets store rather than legacy plaintext password environment variables. <br>
Risk: Some diagnostic behavior depends on database configuration and live validation, including performance_schema availability and MySQL versus MariaDB feature differences. <br>
Mitigation: Run mysql-aiops doctor before relying on live diagnostics, confirm performance_schema is enabled for query-stat workflows, and review flavor-specific results before applying remediation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/mysql-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/MySQL-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured diagnostic summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run maintenance previews, measured database findings, audit-oriented context, and configuration guidance.] <br>

## Skill Version(s): <br>
0.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
