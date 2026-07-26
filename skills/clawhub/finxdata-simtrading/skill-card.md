## Description: <br>
Uses a dedicated FinXData Trading Key to manage A-share and Hong Kong stock watchlists, simulated accounts, orders, positions, trades, cash ledgers, assets, and performance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[finxdata](https://clawhub.ai/user/finxdata) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate FinXData A-share and Hong Kong stock simulated trading workflows through a Python CLI or importable client. It supports user-directed watchlist changes, simulated account creation and reset, order placement and cancellation, and portfolio, trade, cash, asset, and performance queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dedicated simulated-trading key could be exposed if pasted into chat, printed, or logged. <br>
Mitigation: Provide FINXDATA_TRADING_KEY through the environment, do not paste it into chat, and rotate the key outside the agent if authentication fails. <br>
Risk: User-directed simulated trading mutations can create or reset accounts, change watchlists, place orders, or cancel orders. <br>
Mitigation: Read current state before writes, confirm order and reset details with the user, require explicit simulated buy/sell intent, and use the required RESET confirmation for account resets. <br>
Risk: Changing FINXDATA_BASE_URL can send requests and the trading key to an unintended endpoint. <br>
Mitigation: Leave FINXDATA_BASE_URL unset unless the user intentionally trusts the alternate endpoint. <br>
Risk: Simulated fills, holdings, fees, and performance may be mistaken for real brokerage activity or investment advice. <br>
Mitigation: State that results are simulated, review quote and fee details, and avoid presenting simulated positions as real holdings or investment recommendations. <br>


## Reference(s): <br>
- [FinXData A-share and Hong Kong simulated trading API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/finxdata/skills/finxdata-simtrading) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell commands; the CLI returns JSON responses and JSON error payloads.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires FINXDATA_TRADING_KEY; mutating simulated trading calls can change watchlists, accounts, orders, and account reset state.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
