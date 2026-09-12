## Description:

MySQL AIops helps agents operate and troubleshoot MySQL 8.x and MariaDB 10.6+ servers with health checks, query and lock analysis, replication and fragmentation RCA, and governed DBA write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers, database administrators, and operations engineers use this skill to inspect MySQL or MariaDB server health, diagnose slow queries, lock waits, replication lag, and fragmentation, and run selected DBA remediation commands with audit and dry-run support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and invokes external executable code for database administration.

Mitigation: Pin or verify the mysql-aiops package version before production use.

Risk: The skill stores database secrets and operational state locally.

Mitigation: Protect ~/.mysql-aiops as sensitive data, avoid long-lived master passwords in shell profiles or CI logs, and use the encrypted secret store.

Risk: The skill can perform live MySQL or MariaDB changes without a skill-level approval gate.

Mitigation: Start with a dedicated least-privilege database account, withhold write and admin grants until needed, and use dry-run previews and human approval for state-changing operations.

Risk: Database connections on untrusted networks can expose credentials or traffic if TLS is weakly configured.

Mitigation: Require TLS verification with verify_ca or verify_identity and a trusted CA for untrusted networks.

## Reference(s):

- [mysql-aiops capabilities](references/capabilities.md)
- [mysql-aiops CLI reference](references/cli-reference.md)
- [mysql-aiops setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [MySQL-AIops homepage](https://github.com/AIops-tools/MySQL-AIops)
- [ClawHub mysql-aiops page](https://clawhub.ai/zw008/skills/mysql-aiops)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured database findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include database observations, RCA findings, dry-run remediation commands, and operational guidance.]

## Skill Version(s):

0.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
