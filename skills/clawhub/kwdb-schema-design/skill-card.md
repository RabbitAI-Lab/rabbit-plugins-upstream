## Description: <br>
Design KWDB schemas and generate DDL for relational, time-series, and mixed workloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kwdb](https://clawhub.ai/user/kwdb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and database engineers use this skill to classify KWDB workloads, gather schema requirements, design relational, time-series, or mixed schemas, and generate reviewable KWDB DDL with validation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated DROP, CASCADE, retention, and privilege SQL can affect data, dependencies, or access if applied without review. <br>
Mitigation: Treat generated SQL as review-only until the target database, environment, backups, dependency impact, and least-privilege requirements are verified. <br>
Risk: Broad schema and DDL triggers may activate the skill for adjacent database tasks outside its intended scope. <br>
Mitigation: Confirm the request is KWDB schema design or DDL before relying on the generated guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kwdb/skills/kwdb-schema-design) <br>
- [Core Rules and Decision Tree](references/key-rules.md) <br>
- [Requirement Disambiguation Questions](references/disambiguation.md) <br>
- [Skill Scope and Boundaries](references/_scope.md) <br>
- [Table DDL Reference](references/table-ddl-ref.md) <br>
- [Index DDL Reference](references/index-ddl-ref.md) <br>
- [Constraint Reference](references/constraint-ref.md) <br>
- [Data Type Reference](references/type-ref.md) <br>
- [Partitioning Reference](references/partitioning-ref.md) <br>
- [Time-Series Retention Reference](references/retention-ref.md) <br>
- [Output Templates](assets/output-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown with SQL and validation command code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces reviewable KWDB DDL, schema rationale, assumptions, and validation steps.] <br>

## Skill Version(s): <br>
1.2.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
