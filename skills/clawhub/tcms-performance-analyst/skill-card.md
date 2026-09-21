## Description:

Monthly content performance and output-analysis skill that aggregates published content, calendar variance, channel-effect data, product-line coverage, and knowledge-base health into a monthly report with next-cycle optimization suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Brand-side tech-product marketing teams use this skill to produce monthly content performance reports that compare planned and published output, summarize channel metrics when available, evaluate product-line coverage, and recommend next-month adjustments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads business content, calendars, channel metrics, and product maps that may include sensitive internal planning data.

Mitigation: Provide only narrow, authorized paths for the monthly analysis inputs and limit use to teams that need TCMS-style content performance reports.

Risk: Missing channel-effect data could lead to unsupported performance conclusions.

Mitigation: Mark missing metrics as DATA_MISSING and limit findings to observable dimensions when effect data is unavailable.

Risk: Recommendations could be mistaken for automatic planning changes.

Mitigation: Keep the report advisory and require human confirmation before plan teams act on recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-performance-analyst)
- [Publisher profile](https://clawhub.ai/user/haiyangchenbj)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown report saved as reports/YYYY-MM-monthly-report.md]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Missing metrics are marked DATA_MISSING; every finding should reference an observable date, file, or data point.]

## Skill Version(s):

1.1.6 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
