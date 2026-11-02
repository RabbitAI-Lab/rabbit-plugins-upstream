## Description:

用 Cue 一键深度拆解热门赛道与ETF，包括赛道全景分析、同类ETF横向对比、底层持仓穿透和估值水位研判。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

个人ETF投资者、定投用户和理财顾问可用它研究有A股上市ETF覆盖的赛道，比较产品、检查持仓暴露并查看历史估值水位。它提供研究材料以支持选择，不提供具体买卖时点建议。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: API credentials could be exposed if the user shares a key in chat.

Mitigation: Configure CUE_API_KEY locally or use an owner-only configuration file, and rotate any key already shared.

Risk: The downloaded research runner may be unsafe or may change before execution.

Mitigation: Review and pin the runner before executing it.

Risk: Research queries consume account credits.

Mitigation: Check available credits and account usage before running research.

## Reference(s):

- [Cue](https://cuecue.cn/)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-sector-etf)
- [Cue runner repository (listed by the skill)](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror (listed by the skill)](https://gitee.com/sensedeal/cue-skills)
- [Eastmoney Fund](https://fund.eastmoney.com)
- [China Securities Index](https://www.csindex.com.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Chinese research report in Markdown with comparison tables, valuation analysis, risk notes, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers A-share listed ETFs; excludes intraday valuation and specific buy/sell timing recommendations.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
