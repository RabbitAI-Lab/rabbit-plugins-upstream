## Description:

三立期货「三立智期」助手可供用户查询期货行情、账户持仓、资讯与龙虎榜，在模拟盘下单，并配置实盘条件单及止盈止损。

This skill is ready for commercial/non-commercial use.

## Publisher:

[13371979982](https://clawhub.ai/user/13371979982)

### License/Terms of Use:

MIT-0

## Use Case:

External users of 三立智期 use the assistant to check futures markets, account positions, news, and rankings; submit simulated orders; and configure broker-hosted live conditional orders and profit/loss controls.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Setup may expose an API key, and live-trading recovery instructions may lead to unsafe order retries.

Mitigation: Use a simulation-only key; do not enter a live key in the setup script, and rotate any key captured in installation logs.

Risk: Live orders and server-hosted conditional orders can remain active independently of the skill session.

Mitigation: Verify the publisher and API with the broker, confirm the active trading environment and exact order details, and separately check or cancel outstanding server-hosted orders.

## Reference(s):

- [Usage notes](references/usage-notes.md)
- [Market API reference](references/api-market.md)
- [Company FAQ](references/company-faq.md)
- [Sanli Futures official website](https://www.sxslqh.com/)

## Skill Output:

**Output Type(s):** [Text, Analysis, API Calls, Guidance]

**Output Format:** [Chinese conversational responses with market and account data, order status, and trading configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit simulated orders and configure broker-hosted live conditional orders when explicitly requested.]

## Skill Version(s):

1.5.8 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
