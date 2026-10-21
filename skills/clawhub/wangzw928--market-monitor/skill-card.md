## Description:

Provides source-checked market snapshots and optional deeper analysis across Chinese, US, and Hong Kong equities, rates, currencies, commodities, and macroeconomic events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangzw928](https://clawhub.ai/user/wangzw928)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and analysts use this skill to review current market conditions, compare cross-market risks, and examine earnings, valuations, or an existing investment plan with dated source evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delayed, stale, or unavailable quotes can make a market summary misleading.

Mitigation: Use live, source-checked data; identify observation times and quote status, and disclose missing or unverified values.

Risk: Readers may mistake market analysis for an automatic trading recommendation.

Mitigation: Treat outputs as source-checked context, not automatic trading advice; weigh investment choices against the user's own constraints.

Risk: Shanghai-default display times can obscure the US trading date.

Mitigation: Label time zones and retain the New York trading date for US markets.

## Reference(s):

- [Market Monitor release](https://clawhub.ai/wangzw928/skills/market-monitor)
- [Data sources and indicator definitions](references/data-sources.md)
- [Deep analysis framework](references/analysis.md)
- [Shanghai Stock Exchange](https://www.sse.com.cn/)
- [NYSE trading information](https://www.nyse.com/trade/trading-information)
- [FRED 10-year Treasury yield](https://fred.stlouisfed.org/series/DGS10)

## Skill Output:

**Output Type(s):** [Text, Market analysis, Guidance]

**Output Format:** [Markdown market snapshot or detailed analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primarily Chinese-language; dates, time zones, source links, quote status, and unverified or missing data are identified when applicable.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
