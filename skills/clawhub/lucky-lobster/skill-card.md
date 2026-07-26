## Description: <br>
Trade prediction markets on Polymarket. Search markets, place orders, and manage positions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rachelbastian](https://clawhub.ai/user/rachelbastian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent developers use Lucky Lobster to connect an agent to LuckyLobster's Polymarket API, search prediction markets, inspect market data, place or cancel orders, manage positions, and redeem settled outcomes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent persistent authority to spend funds and change wallet positions through Polymarket trading actions. <br>
Mitigation: Require explicit user approval for every trade, position close, token approval, cancellation, and redemption; keep account balances limited. <br>
Risk: API key storage gives ongoing access to trading, cancellation, and redemption permissions. <br>
Mitigation: Store the API key carefully, restrict access to the runtime environment, and revoke the key when the agent no longer needs access. <br>
Risk: Trading and redemption actions may execute immediately or alter positions irreversibly. <br>
Mitigation: Use dry-run or budget checks where available before executing orders, closing positions, approving tokens, or redeeming settlements. <br>


## Reference(s): <br>
- [LuckyLobster Homepage](https://luckylobster.io) <br>
- [Lucky Lobster ClawHub Skill Page](https://clawhub.ai/rachelbastian/skills/lucky-lobster) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with HTTP, JSON, JavaScript, and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LUCKYLOBSTER_API_KEY for authenticated API requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
