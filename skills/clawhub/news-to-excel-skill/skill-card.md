## Description:

自动提取网页新闻列表中的时间和事件简介，并整理为可用 Excel 打开的 CSV 表格。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lilimoss-china](https://clawhub.ai/user/lilimoss-china)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, analysts, and content operations teams use this skill to turn public news roundup pages, activity lists, and monthly reports into timeline tables with date and event-summary columns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent fetches and processes a webpage URL supplied by the user.

Mitigation: Use public, non-sensitive pages unless the user has approval to process the page content.

Risk: The packaged Excel helper appears malformed in the security guidance and may need cleanup before execution.

Mitigation: Treat the helper as optional, inspect or repair it before running, and use CSV text output when direct file generation is not needed.

Risk: Extraction can miss or misread dates and summaries on image-only, PDF, or poorly structured pages.

Mitigation: Review the generated CSV or table before using it in reports or records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lilimoss-china/skills/news-to-excel-skill)
- [usage.md](artifact/usage.md)
- [faq.md](artifact/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Files, Guidance]

**Output Format:** [CSV text or Markdown table, with optional XLSX file generation through a helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs use two main columns: time and event summary.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
