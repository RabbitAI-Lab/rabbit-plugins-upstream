## Description:

聚宽(JoinQuant)策略回测代码生成框架。基于六段式骨架模板，支持截面多因子选股、时序技术指标择时两种模式，使用聚宽原生API获取数据，自动生成可直接在聚宽平台运行的回测代码。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenxyzcyxpp](https://clawhub.ai/user/chenxyzcyxpp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and quantitative strategy authors use this skill to generate JoinQuant backtest code for cross-sectional multi-factor stock selection or time-series technical-timing strategies. It helps select templates, fill strategy parameters, reference JoinQuant APIs, and produce code intended to run on the JoinQuant platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated strategy code may create unsuitable trades if order sizing, rebalance logic, commissions, or execution environment are accepted without review.

Mitigation: Review the generated strategy before running it, especially order sizing, rebalance logic, commissions, and whether the target environment is backtest, paper, or live trading.

Risk: JoinQuant API and factor assumptions can cause runtime errors or misleading backtests when documentation or returned data shapes differ from examples.

Mitigation: Verify API signatures, factor IC data, and get_price or attribute_history return shapes against JoinQuant documentation and the bundled access-pitfalls reference.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenxyzcyxpp/skills/joinquant-strategy-backtest)
- [JoinQuant factor library](https://www.joinquant.com/view/factorlib/list)
- [JoinQuant API documentation endpoint](https://www.joinquant.com/help/api/getContent?name=api)
- [JoinQuant API access pitfalls](references/joinquant-api-access-pitfalls.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with Python strategy code and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated strategy code should be reviewed before running in JoinQuant.]

## Skill Version(s):

0.5.1 (source: server release metadata; artifact frontmatter states 0.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
