## Description:

Provides offline Huawei Cloud DWS SQL syntax and specification checks, including DWS-specific syntax validation, object design rules, data operation rules, and naming guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data engineers use this skill to statically review Huawei Cloud DWS SQL before execution, checking syntax compatibility and specification issues without connecting to a cluster.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A clean report may be mistaken for proof of complete SQL safety, compliance, performance, or production readiness.

Mitigation: Treat findings as advisory, review important SQL manually, and use cluster-specific validation for performance or production decisions.

Risk: Some documented checks require cluster metadata or execution-plan analysis and are skipped during local static analysis.

Mitigation: Run appropriate DWS cluster checks for index counts, non-pushdown behavior, view dependency depth, and performance-sensitive changes.

## Reference(s):

- [AST Schema](references/ast_schema.md)
- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-dws-sql-check)
- [Publisher Profile](https://clawhub.ai/user/huaweicloudskill)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, guidance]

**Output Format:** [JSON or Markdown SQL check reports with rule findings and fix suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local static analysis only; some cluster-dependent checks are skipped in static mode.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
