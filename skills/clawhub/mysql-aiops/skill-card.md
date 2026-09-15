## Description:

mysql-aiops helps agents operate and troubleshoot MySQL 8.x and MariaDB 10.6+ servers through governed DBA reads, root-cause analysis workflows, and guarded maintenance writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Database engineers, SREs, and agent operators use this skill to inspect MySQL or MariaDB server health, diagnose slow queries, lock waits, replication lag, fragmentation, and index health, and prepare guarded remediation commands. It is intended for MySQL/MariaDB DBA operations and explicitly excludes PostgreSQL and unrelated infrastructure domains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs an external executable that can connect to live MySQL or MariaDB databases.

Mitigation: Use a pinned and verified package version, review the release before installation, and start with a least-privilege database account.

Risk: Maintenance actions such as killing sessions, changing global variables, index changes, and table optimization can have high operational impact.

Mitigation: Run dry-run previews first, require an operator decision before writes, and rely on database privileges to prevent unauthorized changes.

Risk: Database credentials and operational history may be present under ~/.mysql-aiops/.

Mitigation: Protect the directory with appropriate local access controls, avoid broad environment-variable password exposure, and define retention handling for audit and history data.

Risk: Connections to non-local databases may expose credentials or sensitive query metadata if TLS is not verified.

Mitigation: Use verified TLS modes such as verify_ca or verify_identity with the appropriate CA configuration for untrusted networks.

Risk: The artifact says the query models are mock-validated and not yet exercised against a live server.

Mitigation: Run mysql-aiops doctor and a live verification checklist in a controlled environment before depending on results for production decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/mysql-aiops)
- [Publisher profile](https://clawhub.ai/user/zw008)
- [Project homepage](https://github.com/AIops-tools/MySQL-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and DBA analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include measured database observations, dry-run remediation commands, risk-tier notes, and follow-up verification steps.]

## Skill Version(s):

0.10.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
