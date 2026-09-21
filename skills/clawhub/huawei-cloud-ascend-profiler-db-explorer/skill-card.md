## Description:

Converts natural language questions into safe executable SQL for querying Ascend PyTorch Profiler and msprof databases about operator time, communication, dispatch, and schema details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and performance engineers use this skill to analyze Ascend PyTorch Profiler and msprof SQLite databases, generate bounded SQL for operator, communication, and dispatch bottlenecks, and inspect documented profiler table schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated SQL may query more profiler data than intended or perform large scans.

Mitigation: Review generated SQL before execution, require aggregation or an ORDER BY with LIMIT for main queries, and prefer read-only SQLite access.

Risk: CSV export can persist profiler metadata such as operator names, timings, hardware topology, and model-performance details.

Mitigation: Use CSV export only when explicitly requested and acceptable for the data environment.

Risk: Schema mismatches between profiler documentation and a specific database version can produce incorrect queries or misleading analysis.

Mitigation: Compare documented tables with the target database and use the bundled schema helper before relying on table or column semantics.

## Reference(s):

- [Profiler DB Data Format](references/profiler_db_data_format.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Verification Method](references/verification-method.md)
- [Troubleshooting](references/troubleshooting.md)
- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-ascend-profiler-db-explorer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with SQL snippets, shell commands, and concise analysis tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated SQL, table schema excerpts, query result summaries, and performance optimization recommendations.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
