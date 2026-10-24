## Description:

每天开盘前 3 分钟，看懂今天 A 股的机会与风险——自动扫隔夜美股、政策、产业新闻，大白话讲清利好利空，排出今日最值得关注的方向清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users interested in China's A-share market use this skill to review overnight news, understand possible sector impacts, and prepare a pre-market watchlist. Its reports are informational and do not provide real-time prices or trading advice.

### Deployment Geography for Use:

Global; focused on China's A-share market.

## Known Risks and Mitigations:

Risk: Credential handling and the downloaded runner warrant review.

Mitigation: Keep the API key out of chat and shell history, restrict the key configuration file to the user's account, review and pin the runner, and preserve sandbox protections.

Risk: Cue receives research queries and hosts the resulting reports.

Mitigation: Consider this data flow before use and avoid including sensitive information in research queries.

Risk: Scheduled reports consume Cue credits and may fail if service or external data sources are unavailable.

Mitigation: Approve recurring credit spending only when desired and review each report's source availability and timeliness.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/panting09266-ai/skills/cue-pre-market-strategy)
- [Cue service](https://cuecue.cn/)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown pre-market report with source links and setup guidance, plus shell commands when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a link to the original Cue report; reports are not automatically pushed to the user. Does not provide real-time prices, capital flows, or buy/sell points.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
