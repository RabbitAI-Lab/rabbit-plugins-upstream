## Description:

用 Cue 对个股做短线走势与技术面分析，从量价关系、资金流向和趋势结构入手，计算波动率与最大回撤，并产出可复核的走势分析底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向关注个股短线走势的用户，用于复盘量价关系、资金流向、趋势、波动与关键支撑压力位，形成便于核对的分析底稿。报告用于研究参考，交易决策由用户自行判断。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to send a Cue API key in chat.

Mitigation: Configure the key through protected local secret entry instead, and replace any key already shared in chat.

Risk: The skill runs an external runner that may update, and the downloaded runtime was not fully verified by this review.

Mitigation: Pin and review the runner and its dependencies before execution and before accepting updates.

Risk: Stock queries consume Cue credits, and recurring reports can continue using credits.

Mitigation: Check the available credit balance and require the user's explicit opt-in before setting up recurring reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-technical-analysis)
- [Cue platform](https://cuecue.cn)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-technical-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured Markdown technical-analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes market overview, price-volume analysis, fund flows, trend structure, volatility and drawdown, support and resistance levels, risk notes, and source links.]

## Skill Version(s):

1.1.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
