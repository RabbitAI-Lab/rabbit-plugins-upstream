## Description:

用 Cue 一键深度拆解热门赛道与ETF——赛道全景分析、同类ETF横向对比、底层持仓穿透、估值水位研判，告诉你"这条赛道值不值得投、哪只ETF更匹配"。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Investors use this skill to research A-share ETF-linked sectors, compare relevant ETFs, inspect holdings exposure, and understand historical valuation levels. It provides research context rather than real-time trading or buy/sell timing advice.

### Deployment Geography for Use:

China (A-share ETFs and related sectors)

## Known Risks and Mitigations:

Risk: The downloaded runner may recommend disabling agent security protections during network troubleshooting.

Mitigation: Keep sandbox protections enabled, limit network and report-directory access to what is needed, and review and pin the external runner before execution.

Risk: Research queries are sent to Cue and consume account credits; results may be limited by service status or incomplete public ETF data.

Mitigation: Configure the Cue key locally, confirm the user understands query charges, and check source coverage and report freshness before relying on results.

## Reference(s):

- [Cue research service](https://cuecue.cn/)
- [Eastmoney Fund data](https://fund.eastmoney.com)
- [China Securities Index](https://www.csindex.com.cn)
- [Lixinger valuation data](https://www.lixinger.com)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Structured Chinese-language Markdown research report with comparative tables and cited report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research scope is A-share-listed ETFs; valuation and holdings analysis depends on source-data coverage and Cue service availability.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
