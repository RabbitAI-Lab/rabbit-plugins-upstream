## Description:

Huawei Cloud MRS Spark SQL specification checking skill that performs comprehensive SQL statement checking for MRS Spark, including syntax validation, specification compliance, and performance risk detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data engineers use this skill to review MRS Spark SQL before execution, validate Spark-specific syntax, check specification compliance, and identify performance anti-patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user-supplied file path can be read by the local checker and the analyzed SQL can appear in output.

Mitigation: Provide only SQL text or files intended for analysis, and review generated reports before sharing them.

Risk: Rule findings can be incomplete or overly strict for environment-specific Spark SQL behavior.

Mitigation: Treat findings as review guidance and validate important changes against the target MRS Spark environment before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-mrs-spark-sql-check)
- [AST Schema](references/ast-schema.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Report Template](assets/report_template.md)
- [Syntax Rules](rules/syntax_rules.yaml)
- [Specification Rules](rules/spec_rules.yaml)
- [Performance Rules](rules/perf_rules.yaml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with summary tables, rule violations, source positions, descriptions, and fix suggestions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The checker runs locally and may include the analyzed SQL text in its report output.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
