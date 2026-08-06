## Description: <br>
Futures Quant helps agents support futures quantitative workflows, including market data handling, strategy development, backtesting, risk monitoring, and CTP-based trade execution guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, financial analysts, and trading teams can use this skill to ask an agent for structured futures quant analysis, strategy setup guidance, backtesting support, risk-control suggestions, and trading workflow outputs. Human review is required before connecting broker credentials, changing leverage, or placing orders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill describes live futures order execution and leverage changes without adequate risk gating or user-confirmation boundaries. <br>
Mitigation: Use the skill only for paper trading, sandbox testing, or backtesting until a qualified human has approved the strategy, leverage limits, broker connection, credentials, and risk controls. <br>
Risk: Agent-generated strategy code, trading parameters, or package installation commands could affect real funds if executed directly. <br>
Mitigation: Require explicit human approval before running commands, importing packages, setting leverage, connecting broker APIs, or executing strategies. <br>
Risk: Financial outputs may be incomplete, inaccurate, or unsuitable for a user's jurisdiction, account, or risk tolerance. <br>
Mitigation: Treat outputs as decision support only and validate market data, assumptions, position sizing, and compliance requirements independently before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/futures-quant) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Shanghai Stock Exchange market data](https://www.sse.com.cn/marketdata/) <br>
- [Nasdaq market activity indexes](https://www.nasdaq.com/market-activity/indexes/nasdaq) <br>
- [Euronext market data](https://www.euronext.com/en/market-data) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown, JSON, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON examples, Python snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include trading strategy examples, package installation commands, leverage settings, API key configuration guidance, and structured success/error responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
