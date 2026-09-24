## Description:

Designs MongoDB schemas, indexes, and aggregation pipelines, and helps diagnose slow queries, connection errors, replica set failures, sharding, backups, Atlas, search, and operational incidents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to design and review MongoDB data models, indexes, aggregation pipelines, and operational workflows. It also supports troubleshooting query performance, connection failures, replication lag, sharding hotspots, backups, Atlas deployments, and production incidents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may keep MongoDB deployment details, collection names, query patterns, incident history, and performance baselines in local plaintext memory.

Mitigation: Avoid storing secrets, connection strings, tenant or customer identifiers, or raw production data; tighten file permissions and clear local memory after sensitive work.

Risk: The skill may propose destructive database commands or profiler changes during operational troubleshooting.

Mitigation: Review destructive commands and profiling changes explicitly, and apply them through production change controls before execution.

## Reference(s):

- [ClawHub MongoDB Skill](https://clawhub.ai/ivangdavila/skills/mongodb)
- [Clawic MongoDB Skill Homepage](https://clawic.com/skills/mongodb)
- [Publisher Profile](https://clawhub.ai/user/ivangdavila)
- [Skill Definition](artifact/SKILL.md)
- [Setup and Local Memory](artifact/setup.md)
- [Security Guidance](artifact/security.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May adapt examples to configured MongoDB version, deployment target, driver, ODM, naming conventions, and risk posture.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
