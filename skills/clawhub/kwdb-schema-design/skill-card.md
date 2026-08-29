## Description:

Design KWDB schemas and generate DDL for relational, time-series, and mixed workloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kwdb](https://clawhub.ai/user/kwdb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design KWDB table structures, indexes, constraints, views, partitioning, retention policies, and other DDL for relational, time-series, and mixed workloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated DROP, CASCADE, retention, or privilege commands could cause data loss, authorization changes, or compliance issues if run without review.

Mitigation: Confirm the target database, backups, retention requirements, and authorization before executing generated destructive DDL or privilege commands.

Risk: Generic SQL requests may be mistaken for KWDB-specific schema design tasks.

Mitigation: Clarify whether KWDB is intended before applying KWDB-specific DDL syntax or schema guidance.

## Reference(s):

- [KWDB Schema Design on ClawHub](https://clawhub.ai/kwdb/skills/kwdb-schema-design)
- [Core Rules and Decision Tree](references/key-rules.md)
- [Requirement Disambiguation Questions](references/disambiguation.md)
- [Skill Scope and Boundaries](references/_scope.md)
- [Table DDL Reference](references/table-ddl-ref.md)
- [Index DDL Reference](references/index-ddl-ref.md)
- [Constraint Reference](references/constraint-ref.md)
- [Data Type Reference](references/type-ref.md)
- [Time-Series Retention Reference](references/retention-ref.md)
- [Output Templates](assets/output-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with SQL code blocks and validation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include workload classification, assumptions, schema design rationale, executable KWDB DDL, and validation steps.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
