## Description:

每日收集全球股市资讯（A股/港股/美股/欧股/亚太），覆盖各行业板块，生成标题为「每日动荡+日期」的 Markdown 报告，突出影响当日市场变动的关键消息，并包含「昨日总结」和「今日预期」分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[susie-ss](https://clawhub.ai/user/susie-ss)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market analysts use this skill to collect current public financial news across Chinese, Hong Kong, U.S., European, and Asia-Pacific markets and produce a concise Simplified Chinese Markdown report. The report summarizes market drivers, prior-day conditions, and same-day expectations as commentary rather than financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market commentary may be mistaken for investment or financial advice.

Mitigation: Treat the report as informational commentary and verify material claims against primary financial sources before making decisions.

Risk: Current-market reports can become stale or include outdated search results.

Mitigation: Use date-specific searches, check the year on retrieved sources, and review the generated report for timeliness before relying on it.

Risk: The skill saves reports outside the active project workspace.

Mitigation: Review the output path before use if reports should remain inside a project-controlled directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/susie-ss/skills/daily-market-turmoil)
- [Publisher profile](https://clawhub.ai/user/susie-ss)
- [Search guide](artifact/references/search_guide.md)
- [Report template](artifact/assets/report_template.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown report saved as a dated file, with a brief text summary to the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report is written to ~/Documents/Daily news/每日动荡/每日动荡_YYYY-MM-DD.md when generated.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
