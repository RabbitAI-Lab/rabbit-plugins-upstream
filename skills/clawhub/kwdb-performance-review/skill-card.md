## Description: <br>
Optimizes SQL query performance for KaiwuDB time-series and relational engines using EXPLAIN analysis, query rewrites, pagination guidance, cross-model query review, and conditional configuration tuning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kwdb](https://clawhub.ai/user/kwdb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, database administrators, and support engineers use this skill to diagnose slow KaiwuDB queries, identify time-series and relational anti-patterns, propose safer query rewrites, and review narrowly scoped storage configuration changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may propose cluster-wide database setting changes or schema-impacting examples. <br>
Mitigation: Require database administrator review before applying SET CLUSTER SETTING, CREATE INDEX, DROP INDEX, or application-code changes, especially in production. <br>
Risk: Configuration changes can affect memory, disk, CPU, write throughput, or query latency. <br>
Mitigation: Confirm current resource availability and current setting values before suggesting changes, and validate accepted changes with targeted SHOW CLUSTER SETTING and EXPLAIN analysis. <br>
Risk: Query rewrite advice can be incorrect if the table engine is misidentified. <br>
Mitigation: Verify whether the query targets a time-series, relational, or mixed workload before recommending indexes, time filters, pagination changes, or cross-model rewrites. <br>


## Reference(s): <br>
- [KWDB Performance Review on ClawHub](https://clawhub.ai/kwdb/skills/kwdb-performance-review) <br>
- [KWDB Performance Optimization: Core Rules](artifact/references/key-rules.md) <br>
- [EXPLAIN Output Analysis](artifact/references/query-analysis.md) <br>
- [Time-Series Query Optimization](artifact/references/timeseries-optimization.md) <br>
- [Pagination Optimization for Time-Series](artifact/references/pagination-optimization.md) <br>
- [Relational Query Optimization](artifact/references/relational-optimization.md) <br>
- [Cross-Model Query Optimization](artifact/references/cross-model-optimization.md) <br>
- [Storage Configuration Optimization](artifact/references/config-optimization.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with SQL code blocks and review tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include EXPLAIN validation commands and SET CLUSTER SETTING statements for administrator review; it should not execute database changes automatically.] <br>

## Skill Version(s): <br>
1.2.0 (source: ClawHub release metadata; skill frontmatter reports 0.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
