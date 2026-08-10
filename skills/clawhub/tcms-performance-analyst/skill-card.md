## Description:

Aggregates published content, content calendars, channel-effect data, product-line coverage, and knowledge-base health into a monthly report with next-cycle optimization suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and content leads use this skill to review monthly content output, compare planned work with published work, analyze available channel metrics, and plan next-cycle improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured paths could point outside the intended project content and expose unrelated files to analysis.

Mitigation: Confirm calendar_path, published_dir, channel_data, and product_line_map before running the skill.

Risk: A report for the same month could overwrite an existing reports/YYYY-MM-monthly-report.md file.

Mitigation: Check whether the monthly report already exists and preserve or rename prior output before saving a new report.

Risk: Missing channel-effect data can make performance conclusions incomplete.

Mitigation: Analyze only observable dimensions and mark unavailable metrics as DATA_MISSING.

Risk: If the product-line map is missing, product attribution may rely on title-based inference.

Mitigation: Provide a product_line_map when possible, or include a clear boundary note when title-based inference is used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-performance-analyst)
- [README](artifact/README.md)
- [README (Chinese)](artifact/README_zh.md)

## Skill Output:

**Output Type(s):** [markdown, guidance]

**Output Format:** [Markdown monthly report saved as reports/YYYY-MM-monthly-report.md]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Marks missing performance data as DATA_MISSING and requires findings to reference an observable date, file, or data point.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
