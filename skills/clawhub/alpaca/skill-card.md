## Description: <br>
Trade stocks and crypto via Alpaca API. Use for market data (quotes, bars, news), placing orders (market, limit, stop), checking positions, portfolio management, and account info. Supports both paper and live trading. Use when user asks about stock prices, wants to buy/sell securities, check portfolio, or manage trades. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vamzi](https://clawhub.ai/user/vamzi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users with Alpaca accounts use this skill to fetch market data, review account and portfolio state, manage watchlists and alerts, and place or cancel stock and crypto orders through Alpaca. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can affect live brokerage accounts by placing or cancelling stock and crypto orders. <br>
Mitigation: Use paper trading first, keep live API keys tightly controlled, and require explicit user approval before any live order or cancellation. <br>
Risk: Force mode and cancel-all behavior can bypass or remove safeguards for account actions. <br>
Mitigation: Avoid force mode and cancel-all unless the user explicitly requests the exact account action after reviewing the order or cancellation details. <br>
Risk: Stored Alpaca credentials grant account access if exposed. <br>
Mitigation: Prefer environment-managed secrets or tightly permissioned credential storage, and do not include API keys in prompts, logs, or shared files. <br>


## Reference(s): <br>
- [Alpaca API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/vamzi/skills/alpaca) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, and text or JSON-like CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can invoke Alpaca API operations that read market/account data, manage alerts and watchlists, stream data, place orders, and cancel orders.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
