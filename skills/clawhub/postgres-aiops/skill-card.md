## Description: <br>
Postgres AIops helps agents operate and troubleshoot PostgreSQL clusters with health checks, catalog and pg_stat reads, slow-query, bloat, vacuum, replication, and blocking-lock analysis, plus governed maintenance actions such as canceling sessions, vacuuming, index changes, reindexing, ALTER SYSTEM updates, and query-stat resets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, database administrators, and operations engineers use this skill to inspect PostgreSQL health, investigate performance and locking issues, and carry out controlled maintenance through CLI or MCP workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform powerful PostgreSQL maintenance actions, including terminating sessions, changing indexes, running vacuum or reindex operations, altering settings, and resetting statistics. <br>
Mitigation: Install it only for PostgreSQL environments where DBA-style inspection is intended, start with a read-only or monitoring role, and switch to write privileges only for controlled maintenance. <br>
Risk: Database credentials and local operation records are sensitive. <br>
Mitigation: Protect POSTGRES_AIOPS_MASTER_PASSWORD and review the local audit and undo stores under ~/.postgres-aiops. <br>
Risk: Some maintenance actions are irreversible or operationally disruptive even when audited. <br>
Mitigation: Use dry-run previews, confirm high-risk writes deliberately, and prefer reversible workflows such as recorded index or setting undo where available. <br>


## Reference(s): <br>
- [Postgres AIops project homepage](https://github.com/AIops-tools/Postgres-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, and DBA analysis summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include PostgreSQL observations, cited measurements, dry-run maintenance previews, and guidance to use higher limits when results are truncated.] <br>

## Skill Version(s): <br>
0.8.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
