## Description:

盘后生成 A 股大盘与板块复盘，梳理涨跌原因、资金流向、持仓影响及次日关注信号；不分析单只个股或盘前走势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External investors can use this skill after the market close to review A-share index and sector movements, fund flows, portfolio impact, and signals to watch the next day. It is not intended for single-stock technical analysis or pre-market forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downloaded runner recommends disabling agent protections to resolve connection errors.

Mitigation: Review and pin the runner before use, keep sandbox protections enabled, and allow only the network access needed for Cue.

Risk: Queries are sent to Cue, and optional recurring reports consume credits.

Mitigation: Avoid including sensitive information in queries and enable recurring reports only when the ongoing credit use is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-after-market-assistant)
- [Cue platform](https://cuecue.cn/)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-after-market-assistant)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML]

**Output Format:** [Structured market recap report in Markdown with a standalone HTML dashboard]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market-level A-share review only; no single-stock technical analysis or pre-market forecasts. Scheduled reports may not include a dashboard.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
