## Description: <br>
AIUSD trading and account management skill for cryptocurrency trading and account management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaunceyliu](https://clawhub.ai/user/chaunceyliu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let a personal AI assistant check AIUSD balances, manage trading accounts, execute cryptocurrency trades, stake or unstake AIUSD, withdraw funds, top up gas, and review transaction history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move funds through trades, staking, withdrawals, and gas top-ups. <br>
Mitigation: Require explicit human confirmation for every trade, stake, withdrawal, and gas top-up, including asset, amount, destination, network, fees, and expected result. <br>
Risk: The installers and authentication reset flows can make broad local changes. <br>
Mitigation: Install only from a trusted AIUSD source, inspect the extracted package before running either installer, and treat reauth or reset commands as destructive because they can remove shared local authentication state. <br>
Risk: Local wallet, exchange, API, or authentication credentials could be exposed or affected on shared hosts. <br>
Mitigation: Do not use this skill on a shared host or a machine with unrelated wallet, exchange, or API credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chaunceyliu/skills/aiusd-skill-agent) <br>
- [AIUSD official website](https://aiusd.ai) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and JSON-style tool parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may guide or invoke account, trading, staking, withdrawal, gas top-up, authentication, and troubleshooting workflows.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact build-info reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
