## Description:

Macro Monitor gathers public macroeconomic data, policy updates, and financial news from free sources, summarizes the prior 24 hours, explains key indicators in plain language, and sends a daily report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmzo](https://clawhub.ai/user/hmzo)

### License/Terms of Use:


## Use Case:

External users and analysts use this skill to receive a scheduled Chinese-language digest of macroeconomic releases, central-bank and regulator updates, and major financial news with beginner-friendly explanations of economic indicators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is configured for daily scheduled browsing and report delivery.

Mitigation: Review the cron schedule, browser profile, and message delivery settings before enabling automatic execution.

Risk: Macroeconomic summaries can be incomplete, stale, or affected by temporary source availability.

Mitigation: Verify material figures against the cited public sources before using the report for business or investment decisions.

## Reference(s):

- [Macro indicator explanations](references/indicators.md)
- [Trading Economics economic calendar](https://tradingeconomics.com/calendar)
- [FRED economic data releases](https://fred.stlouisfed.org/releases)
- [National Bureau of Statistics of China](http://www.stats.gov.cn/)
- [People's Bank of China](http://www.pbc.gov.cn/)
- [China Securities Regulatory Commission](http://www.csrc.gov.cn/)
- [CLS financial news](https://www.cls.cn/)
- [Wallstreetcn market news](https://wallstreetcn.com/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style Chinese-language report with categorized bullet points and indicator explanations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scheduled daily at 22:00 Asia/Singapore time; manual triggering is also documented.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
