## Description:

SQL大师工具(专业版) provides agent-facing guidance, examples, and configuration patterns for database migration management, incremental compressed backups, schema comparison and synchronization, high availability, disaster recovery, and operational monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, DBAs, data engineers, and operations teams use this skill to ask an agent for database operations guidance, example scripts, migration and backup workflows, schema comparison steps, high-availability setup patterns, and recovery procedures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence marks the release suspicious because it requests broad command and file access while guiding production-affecting database actions.

Mitigation: Use the skill only with test or explicitly selected database environments unless backups, credentials, target hosts, and rollback plans have been verified.

Risk: Agent-generated migrations, schema synchronization scripts, restores, scheduled jobs, or failover actions could change or interrupt production systems.

Mitigation: Require the agent to show exact commands, scripts, and target connections first, then obtain explicit approval before any execution.

Risk: Database credentials, backup encryption keys, S3 credentials, and webhook URLs may be exposed or misused during automation.

Mitigation: Provide secrets through environment variables or approved secret stores, avoid hardcoding credentials, and limit credentials to the minimum required scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/sql-master-tool-pro)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with tables, JSON examples, Python code snippets, and command-oriented setup notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe database-affecting operations such as migrations, backups, schema synchronization, restores, scheduled jobs, and failover; review generated actions before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
