## Description: <br>
MySQL AIops helps agents inspect and troubleshoot MySQL or MariaDB servers, including health checks, slow-query and lock-wait root-cause analysis, replication lag analysis, fragmentation analysis, index health checks, and guarded DBA actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Database administrators, SREs, and developers use this skill to let an agent collect MySQL/MariaDB operational evidence, explain common performance or replication issues, and propose or run governed maintenance actions when privileges allow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect and potentially change a MySQL/MariaDB server, including killing sessions, changing indexes, and running SET GLOBAL operations. <br>
Mitigation: Start with a least-privilege read-only database account and grant write privileges only when those DBA actions are intended and approved. <br>
Risk: Local configuration, encrypted secrets, audit logs, and undo state are stored under ~/.mysql-aiops by default. <br>
Mitigation: Protect the ~/.mysql-aiops directory, avoid the legacy plaintext password environment variable, and use the encrypted secrets workflow documented by the skill. <br>
Risk: Some operational queries are mock-validated and still need live verification against the target MySQL or MariaDB environment. <br>
Mitigation: Run mysql-aiops doctor and perform a live verification pass before relying on findings in production operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/mysql-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/MySQL-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include database observations, RCA findings, dry-run previews, audit-oriented status details, and configuration steps.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
