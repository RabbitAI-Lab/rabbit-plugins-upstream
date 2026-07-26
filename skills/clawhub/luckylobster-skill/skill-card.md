## Description: <br>
Trade prediction markets on Polymarket. Search markets, place orders, and manage positions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rachelbastian](https://clawhub.ai/user/rachelbastian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use LuckyLobster to discover Polymarket prediction markets, inspect live market data, place or cancel orders, manage positions, redeem settled positions, and configure automated trading strategies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place trades, close positions, approve tokens, redeem funds, and enable automated or copy-trading behavior using real money. <br>
Mitigation: Use narrow API permissions, small budgets, explicit confirmations, and dry-run or preview flows before executing high-impact actions. <br>
Risk: Automated and copy-trading strategies can continue executing after setup and may amplify losses if misconfigured. <br>
Mitigation: Disable recurring and copy-trading features unless intentionally needed, set maxBudget on every strategy, review heartbeat status regularly, and pause or cancel strategies when conditions change. <br>


## Reference(s): <br>
- [LuckyLobster homepage](https://luckylobster.io) <br>
- [ClawHub skill page](https://clawhub.ai/rachelbastian/skills/luckylobster-skill) <br>
- [LuckyLobster agent API base URL](https://luckylobster.io/api/agent/v1) <br>
- [LuckyLobster device authorization endpoint](https://luckylobster.io/api/auth/device) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown guidance with HTTP, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LUCKYLOBSTER_API_KEY and may initiate real-money trading, token approval, position closing, redemption, and automated or copy-trading actions through the LuckyLobster API.] <br>

## Skill Version(s): <br>
0.10.0 (source: server release metadata; artifact openclaw version 10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
