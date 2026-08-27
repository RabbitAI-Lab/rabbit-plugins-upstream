## Description:

Monthly content performance and output-analysis skill that aggregates published content, the content calendar, channel-effect data, product-line coverage, and knowledge-base health, then outputs a monthly report and next-cycle optimization suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Content marketing and operations teams use this skill to review monthly content output, compare planned versus actual publication, assess product-line coverage and available channel-effect data, and prepare advisory recommendations for the next cycle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may receive broader project files than needed for the monthly report.

Mitigation: Provide only the intended calendar, published-content, channel-data, product-map, and knowledge-base files before running the skill.

Risk: A report for the same month could overwrite an existing report.

Mitigation: Confirm before overwriting an existing monthly report or write a uniquely named copy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-performance-analyst)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown monthly report saved to reports/YYYY-MM-monthly-report.md]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Marks missing performance data as DATA_MISSING and produces advisory recommendations without modifying calendars or triggering downstream writing.]

## Skill Version(s):

1.1.3 (source: server evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
