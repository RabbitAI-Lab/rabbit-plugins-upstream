## Description:

Monthly content performance and output-analysis skill that aggregates published content, content calendar, channel-effect data, product-line coverage, and knowledge-base health into a monthly report with next-cycle optimization suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Content, marketing, and product teams use this skill to review monthly content output, compare planned work with actual publication, identify coverage and performance gaps, and prepare advisory recommendations for the next cycle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product-line analysis can be weaker or less reliable when the product map is missing.

Mitigation: Provide product_line_map when accuracy matters and review the generated report before acting on recommendations.

Risk: Missing channel-effect data can limit performance conclusions.

Mitigation: Analyze only observable dimensions when effect data is unavailable and mark unavailable metrics as DATA_MISSING.

Risk: Advisory recommendations may be acted on before business review.

Mitigation: Require human confirmation before the planning team acts on generated recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-performance-analyst)
- [artifact/SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown monthly report saved as reports/YYYY-MM-monthly-report.md]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Marks missing performance data as DATA_MISSING and does not modify schedules or trigger downstream writing.]

## Skill Version(s):

1.1.5 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
