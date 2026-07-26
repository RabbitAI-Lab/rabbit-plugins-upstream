## Description: <br>
Postgres Aiops helps agents operate and troubleshoot PostgreSQL clusters with health checks, query and lock analysis, bloat and vacuum recommendations, replication checks, and guarded maintenance commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Database administrators, developers, and operations engineers use this skill to inspect PostgreSQL health, diagnose slow queries, analyze bloat and blocking, and prepare guarded maintenance actions with audit and undo support where available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can connect to PostgreSQL databases and expose powerful read and write operations. <br>
Mitigation: Install it only for databases you are authorized to administer, start with a read-only or least-privilege PostgreSQL role, and enable write-capable credentials only for deliberate maintenance. <br>
Risk: Maintenance actions can affect database availability or state. <br>
Mitigation: Use dry-run first, rely on the documented audit trail and undo support where available, and treat irreversible actions such as cancel, terminate, vacuum, reindex, and reset stats as operational changes requiring extra review. <br>
Risk: The master password unlocks stored database credentials. <br>
Mitigation: Treat the master password as a high-value secret and provide it only through secure runtime secret handling. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/postgres-aiops) <br>
- [Project Homepage](https://github.com/AIops-tools/Postgres-AIops) <br>
- [Capabilities Reference](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Setup and Security Guide](references/setup-guide.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include PostgreSQL observations, cited analysis findings, dry-run previews, and operational recommendations.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
