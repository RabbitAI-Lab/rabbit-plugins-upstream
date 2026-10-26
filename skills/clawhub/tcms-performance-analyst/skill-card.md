## Description:

Analyzes monthly content output, schedule variance, channel performance, product-line coverage, and knowledge-base health to produce a report with next-month recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Content marketing teams use this skill to review the previous month's published content against their calendar, assess available channel metrics and product coverage, and plan improvements for the next cycle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monthly reports may expose internal channel metrics and product-line mapping.

Mitigation: Use only for authorized reporting; provide only the needed files and handle the report as internal data.

Risk: Broad trigger phrases may invoke the skill outside the intended reporting workflow.

Mitigation: Narrow trigger phrases before broad publication and confirm the reporting scope.

Risk: Missing or vendor-reported metrics may lead to misleading conclusions.

Mitigation: Mark gaps as DATA_MISSING, identify observed data boundaries, and label vendor metrics as reported rather than independently verified.

## Reference(s):

- [Content Performance Analyst on ClawHub](https://clawhub.ai/haiyangchenbj/skills/tcms-performance-analyst)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown monthly report saved as reports/YYYY-MM-monthly-report.md]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes plan-versus-actual tables, product and channel findings, knowledge-base health, and next-month recommendations; labels missing data and qualifies vendor-reported metrics.]

## Skill Version(s):

1.1.7 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
