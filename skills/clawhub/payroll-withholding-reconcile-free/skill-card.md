## Description:

Reconciles payroll withholding against individual income tax and social insurance filing table data with row-level recalculation, totals checks, duplicate and blank-field detection, and source-cited findings for the free check set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Payroll, finance, and HR users can use this skill during monthly closing or filing reconciliation to compare payroll withholding with tax and social insurance filing values. It reports calculable mismatches, missing required fields, duplicate people, and totals issues without making tax or social insurance calculation judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes payroll data, which may include sensitive employee compensation and filing information.

Mitigation: Run it only on payroll data the user is authorized to process, and prefer local execution as described by the inspected release.

Risk: The free version explicitly withholds some advanced checks, so a clean result is not a full payroll compliance review.

Mitigation: Treat output as reconciliation assistance for the listed free checks and review the omitted checks before relying on the result.

Risk: Most user-facing messages are in Chinese, which can lead to misunderstanding for reviewers who do not read Chinese.

Mitigation: Have a Chinese-reading reviewer confirm findings and limitations before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-withholding-reconcile-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable console text or structured JSON findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing-field guidance instead of a reconciliation conclusion.]

## Skill Version(s):

1.0.49 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
