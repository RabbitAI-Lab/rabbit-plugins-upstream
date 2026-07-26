## Description: <br>
Trade prediction markets with natural language via Foreseek, matching beliefs to Kalshi contracts and supporting market search, positions, orders, cancellations, balances, and account status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hypegamer007](https://clawhub.ai/user/hypegamer007) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to parse natural-language predictions, find related Kalshi markets, view account and portfolio information, and submit or cancel orders through a Foreseek-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place live Kalshi trades or cancel orders through an agent-controlled Foreseek account. <br>
Mitigation: Use scoped API keys when available, start with read-only or demo actions, and require explicit confirmation of ticker, side, order type, contract count, and estimated cost before live trades or cancellations. <br>
Risk: Natural-language prediction matching may select an unintended market or trade direction. <br>
Mitigation: Review the matched market title, ticker, side, and displayed probability before executing any order. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hypegamer007/skills/foreseekai) <br>
- [Foreseek website](https://foreseek.ai) <br>
- [Foreseek dashboard](https://foreseek.ai/dashboard) <br>
- [Foreseek documentation](https://foreseek.ai/docs) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, JSON, Configuration] <br>
**Output Format:** [Markdown with curl examples and JSON request/response payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires FORESEEK_API_KEY and a Foreseek account with a connected Kalshi account for trading operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
