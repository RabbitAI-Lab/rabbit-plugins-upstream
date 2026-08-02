## Description: <br>
Huawei Cloud MRS Spark SQL specification checking skill that performs SQL syntax validation, specification compliance checks, and performance risk detection for MRS Spark. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data engineers use this skill to statically review Huawei Cloud MRS Spark SQL before execution, checking syntax, Spark-specific constructs, specification rules, and common performance anti-patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SQL supplied for checking may be included in generated local reports. <br>
Mitigation: Avoid submitting secrets, credentials, tokens, or sensitive data values in SQL text before running the checker or sharing its report. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-mrs-spark-sql-check) <br>
- [AST Schema](references/ast-schema.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Syntax Rules](rules/syntax_rules.yaml) <br>
- [Specification Rules](rules/spec_rules.yaml) <br>
- [Performance Rules](rules/perf_rules.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with summary tables, rule violations, positions, snippets, and fix suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs offline with Python 3.8+ standard library scripts and can echo the checked SQL text in local reports.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
