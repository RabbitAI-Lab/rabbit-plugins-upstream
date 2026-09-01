## Description:

Automates end-to-end anomaly detection for time-series data stored in KaiwuDB / KWDB.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kwdb](https://clawhub.ai/user/kwdb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect KWDB or KaiwuDB time-series tables for outliers, spikes, dips, drift, and data-quality issues in numeric telemetry columns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles database credentials and can execute SQL against KWDB or KaiwuDB.

Mitigation: Use a least-privileged read-only KWDB account and avoid production or administrator credentials.

Risk: The SQL runner can execute and commit database-changing statements.

Mitigation: Inspect every SQL statement before execution and reject any statement that would create, modify, or delete database objects or data.

Risk: Intermediate database results and reports may be written to /tmp.

Mitigation: Avoid querying sensitive data unless temporary-file handling is acceptable, and remove intermediate files after use.

## Reference(s):

- [KWDB Time-Series Anomaly Detection on ClawHub](https://clawhub.ai/kwdb/skills/kwdb-ts-anomaly-detection)
- [Workflow](references/workflow.md)
- [Constraints](references/constraints.md)
- [Metadata Query](references/metadata-query.md)
- [SELECT](references/ts-select.md)
- [Column Comment](references/column-comment.md)
- [Error Handling](references/error-handling.md)
- [Report Template](references/report-template.md)
- [HTML Report Template](references/report-template-html.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with SQL, shell commands, anomaly summaries, and optional HTML or Markdown report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create temporary SQL result, detection result, report JSON, HTML, or Markdown files under /tmp while preserving the final report.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
