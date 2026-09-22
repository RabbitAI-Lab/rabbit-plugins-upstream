## Description:

Alibaba Cloud Lindorm Agent Skill helps agents answer Lindorm operations and development questions using bundled references for instance management, monitoring, troubleshooting, SQL, search, vector retrieval, AI engine calls, multimodal search, knowledge search, and CLI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database operators, and support engineers use this skill to plan, troubleshoot, and operate Alibaba Cloud Lindorm deployments. It provides guidance, SQL and CLI examples, and configuration steps for Lindorm development, monitoring, storage, migration, permissions, and connectivity tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent through real Alibaba Cloud Lindorm operations using cloud credentials or database passwords.

Mitigation: Configure credentials outside the chat session, avoid pasting AK/SK values, STS tokens, or passwords, and use least-privilege non-root accounts.

Risk: CLI installation or replacement instructions may depend on a latest download that is not independently verified.

Mitigation: Manually verify the CLI source and integrity before installing or replacing a local binary.

Risk: Generated operational commands could affect production Lindorm resources if parameters are wrong.

Mitigation: Confirm region, instance ID, time range, account, and network parameters before execution, and review proposed commands before running them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-lindorm-agent-skill)
- [Skill Homepage Metadata](https://clawhub.ai/sdk-team/alibabacloud-lindorm-agent-skill)
- [Lindorm Agent Skill](artifact/SKILL.md)
- [Connection Information Retrieval Scenario](artifact/references/01-dev/connection-guide.md)
- [Quick Start Scenarios](artifact/references/01-dev/quick-start-guide.md)
- [Lindorm SQL Client Development Guide](artifact/references/01-dev/sql-client-guide.md)
- [Lindorm SQL Syntax Reference](artifact/references/01-dev/sql-operations.md)
- [Lindorm SQL Usage Notes](artifact/references/01-dev/sql-usage-notes.md)
- [Lindorm SQL Table Creation Statement Guide](artifact/references/01-dev/table-design.md)
- [Lindorm Search Engine Guide](artifact/references/01-dev/search-guide.md)
- [Lindorm Vector Engine Guide](artifact/references/01-dev/vector-guide.md)
- [Lindorm AI Engine Guide](artifact/references/01-dev/ai-guide.md)
- [Multimodal Image-Text Search Scene](artifact/references/01-dev/multimodal-search-scene.md)
- [Knowledge Base Search Scene](artifact/references/01-dev/knowledge-search-scene.md)
- [Instance Management Scenarios](artifact/references/02-ops/instance-management.md)
- [Monitoring and Alerting Scenarios](artifact/references/02-ops/monitoring-guide.md)
- [Error Troubleshooting Scenarios](artifact/references/02-ops/error-troubleshoot.md)
- [Storage Analysis Scenarios](artifact/references/02-ops/storage-analysis.md)
- [Connection Troubleshooting Scenarios](artifact/references/02-ops/connection-troubleshoot.md)
- [Backup and Restore Scenarios](artifact/references/02-ops/backup-restore.md)
- [Data Migration Scenarios](artifact/references/02-ops/data-migration.md)
- [Account and Permission Management Scenarios](artifact/references/02-ops/user-permission.md)
- [Slow Query Analysis Scenarios](artifact/references/02-ops/slow-query-analysis.md)
- [Lindorm CLI Agent Skill Guide](artifact/references/03-ref/lindorm-cli-guide.md)
- [HBase Shell (alihbase) Agent Skill Guide](artifact/references/03-ref/hbase-shell-guide.md)
- [Aliyun CLI Command List](artifact/references/03-ref/related-commands.md)
- [RAM Permission Policy List](artifact/references/03-ref/ram-policies.md)
- [Aliyun CLI Installation & Configuration Guide](artifact/references/03-ref/cli-installation-guide.md)
- [Acceptance Criteria](artifact/references/03-ref/acceptance-criteria.md)
- [Verification Methods](artifact/references/03-ref/verification-method.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline SQL, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Aliyun CLI, Lindorm CLI, HBase Shell, SQL, and API examples; user-configurable parameters should be confirmed before execution.]

## Skill Version(s):

0.0.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
