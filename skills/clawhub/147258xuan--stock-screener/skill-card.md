## Description:

Filters A-share stocks by valuation, trading activity, and technical indicators, with presets, watchlists, and text, JSON, Markdown, or CSV output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[147258xuan](https://clawhub.ai/user/147258xuan)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and analysts use it to filter A-share market data by selected valuation, trading, and technical criteria, then review the results in a preferred format.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports that requested technical filters may be skipped if technical analysis fails.

Mitigation: If a technical-filtered run reports analysis failure, treat its results as unverified for those filters and retry or check the indicator data before relying on them.

Risk: The security scan was partial, and static analysis of scripts/screen.js was limited.

Mitigation: Review the source, tool access, and dependency installation process before installing; obtain a complete scan when available.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/147258xuan/skills/stock-screener)
- [Tencent Finance quote feed](https://qt.gtimg.cn/q=)
- [Sina Finance K-line data API](https://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown, CSV, Files]

**Output Format:** [Text, JSON, Markdown table, or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be filtered, sorted, limited, saved to a file, and organized in named watchlists.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata; package.json reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
