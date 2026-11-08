## Description:

用 Cue 深度分析 A 股赛道与 ETF，包括赛道全景、产品对比、持仓穿透、估值水位和风险扫描。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

个人 ETF 投资者、资产配置者和投顾可用此技能研究有 A 股 ETF 覆盖的赛道，比较相关产品、检查持仓暴露并了解估值与风险；它不提供具体买卖时点建议。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill's security guidance identifies a risk of exposing a reusable Cue API key by pasting it into chat.

Mitigation: Keep the key outside chat in CUE_API_KEY or a tightly permissioned configuration file, and rotate any key already pasted into a conversation.

Risk: The external Cue runner is not included in the supplied artifact.

Mitigation: Review and pin the external runner before execution.

## Reference(s):

- [Cue research service](https://cuecue.cn/)
- [Eastmoney Fund Data](https://fund.eastmoney.com/)
- [China Securities Index](https://www.csindex.com.cn/)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown research report with comparison tables and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers A-share listed ETFs; includes sector analysis, ETF comparisons, holdings review, valuation context, and risk notes.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
