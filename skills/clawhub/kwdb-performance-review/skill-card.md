## Description:

Optimizes SQL query performance for KaiwuDB time-series and relational engines by analyzing EXPLAIN output, anti-patterns, pagination, cross-model queries, and selected configuration tuning cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kwdb](https://clawhub.ai/user/kwdb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to review slow KWDB SQL and EXPLAIN output, distinguish time-series, relational, or mixed workloads, and produce query rewrites with validation steps. It can also frame limited configuration tuning proposals after resource preconditions are confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may produce administrator-level configuration or DDL proposals such as SET CLUSTER SETTING, CREATE INDEX, or DROP INDEX.

Mitigation: Treat these outputs as review proposals only; a qualified database operator should assess and test them outside production before execution.

Risk: Applying query, schema, or configuration advice to the wrong KWDB engine or workload can degrade performance or use unsupported operations.

Mitigation: Confirm whether the target is time-series, relational, or mixed before acting, and validate changes with EXPLAIN or EXPLAIN ANALYZE.

## Reference(s):

- [KWDB Performance Review skill page](https://clawhub.ai/kwdb/skills/kwdb-performance-review)
- [KWDB Performance Optimization: Core Rules](references/key-rules.md)
- [EXPLAIN Output Analysis](references/query-analysis.md)
- [Time-Series Query Optimization](references/timeseries-optimization.md)
- [Pagination Optimization for Time-Series](references/pagination-optimization.md)
- [Relational Query Optimization](references/relational-optimization.md)
- [Cross-Model Query Optimization](references/cross-model-optimization.md)
- [Storage Configuration Optimization](references/config-optimization.md)
- [Configuration Tuning Examples](assets/example-configs.md)
- [Example Queries for kwdb-performance-review](assets/example-queries.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown with SQL code blocks and configuration review tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory proposals and validation steps; database operators should review and test changes before execution.]

## Skill Version(s):

1.2.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
