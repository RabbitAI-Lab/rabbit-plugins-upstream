## Description:

Checks ClickHouse SQL statements for syntax compatibility and MRS development specification rules across kernel versions 24.8, 23.3, and 22.3.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review ClickHouse SQL before execution, including syntax validation, version-specific compatibility checks, and advisory MRS development specification findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SQL check results may be incomplete or misleading for complex grammar or production approval decisions.

Mitigation: Treat reports as advisory static analysis and require human review before relying on findings for production changes.

Risk: Unsafe shell quoting of user-provided SQL can change command behavior when an agent runs the local checker.

Mitigation: Pass SQL as a safely quoted argument or use the Python API instead of interpolating raw SQL into shell commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-mrs-clickhouse-sql-check)
- [DDL Grammar Reference](artifact/references/ddl_grammar.md)
- [DML and Misc Grammar Reference](artifact/references/dml_misc_grammar.md)
- [SELECT Grammar Reference](artifact/references/select_grammar.md)
- [Token Types Reference](artifact/references/token_types.md)
- [Report Template](artifact/templates/report_template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown or JSON SQL check reports with summary metrics, violation details, and fix suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Checks are advisory static analysis results for user-provided SQL and selected ClickHouse version or mode.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
