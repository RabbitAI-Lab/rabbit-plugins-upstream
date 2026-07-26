## Description: <br>
Manage AIUSD trading and accounts by checking balances, executing trades, staking, withdrawing funds, topping up gas, and reviewing transaction history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaunceyliu](https://clawhub.ai/user/chaunceyliu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let a personal AI assistant manage AIUSD account queries and initiate trading, staking, withdrawal, gas top-up, recharge guidance, re-authentication, and transaction-history workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate trades, staking, withdrawals, and gas top-ups that may move funds. <br>
Mitigation: Require explicit user confirmation before each sensitive action and verify amounts, assets, chains, and wallet addresses before execution. <br>
Risk: The installer may delete an existing aiusd-skill folder and run npm dependency lifecycle scripts. <br>
Mitigation: Review the unpacked package and dependencies first, install in an isolated directory, and preserve any existing local skill data before installation. <br>
Risk: The re-authentication flow clears cached credentials and starts OAuth login. <br>
Mitigation: Only re-authenticate after explicit user intent, keep tokens local, and avoid exposing authentication URLs or token details in chat. <br>


## Reference(s): <br>
- [ClawHub trade-agent skill page](https://clawhub.ai/chaunceyliu/skills/trade-agent) <br>
- [AIUSD official website](https://aiusd.ai) <br>
- [AIUSD OAuth login](https://mcp.alpha.dev/oauth/login) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and tool-call descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live tool-schema lookup before use and explicit user confirmation for sensitive financial operations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
